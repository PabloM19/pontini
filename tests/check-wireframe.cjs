const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const coverage = require('./wireframe-coverage.json');
const root = path.resolve(__dirname, '..');
const base = process.env.PONTINI_PREVIEW || 'http://127.0.0.1:4173/';
const widths = [320, 390, 600, 768, 801, 1024, 1440];
const report = { date: new Date().toISOString(), pages: [], layouts: [], interactions: [], errors: [] };
function check(value, message) { assert.ok(value, message); }

(async () => {
  const browser = await chromium.launch({ headless: true });
  const output = path.join(root, 'investigacion/qa/completo');
  fs.mkdirSync(output, { recursive: true });
  try {
    const p = await browser.newPage();
    p.setDefaultTimeout(6000);
    p.on('pageerror', error => report.errors.push(error.message));
    p.on('response', response => { if (response.status() >= 400) report.errors.push(`${response.status()} ${response.url()}`); });
    // All pages, assets, source-derived blocks and anchors, rather than just the new templates.
    const documents = {};
    for (const [file, entry] of Object.entries(coverage)) {
      const response = await p.goto(base + file);
      assert.equal(response.status(), 200, file);
      const doc = await p.evaluate(() => ({
        ids: [...document.querySelectorAll('[id]')].map(e => e.id),
        links: [...document.querySelectorAll('a[href]')].map(e => e.getAttribute('href')),
        h1: document.querySelectorAll('h1').length,
        lang: document.documentElement.lang,
        emptyButtons: [...document.querySelectorAll('button')].filter(e => !e.textContent.trim() && !e.getAttribute('aria-label')).length
      }));
      assert.equal(doc.h1, 1, `${file}: h1`);
      assert.equal(doc.lang, 'it', `${file}: Italian`);
      assert.equal(doc.emptyButtons, 0, `${file}: unlabeled controls`);
      assert.equal(new Set(doc.ids).size, doc.ids.length, `${file}: duplicate IDs`);
      for (const [selector, count] of Object.entries(entry.sections)) {
        assert.equal(await p.locator(selector).count(), count, `${file}: ${selector}`);
      }
      const headings = await p.locator('h1,h2,h3').allTextContents();
      for (const title of entry.headings || []) check(headings.includes(title), `${file}: missing ${title}`);
      documents[file] = doc;
      report.pages.push({ file, source: entry.source, sectionsChecked: Object.keys(entry.sections).length });
    }
    let linkCount = 0;
    for (const [file, doc] of Object.entries(documents)) {
      for (const href of doc.links) {
        const url = new URL(href, base + file);
        if (url.origin !== new URL(base).origin) continue;
        const target = decodeURIComponent(url.pathname.slice(1)) || 'index.html';
        check(documents[target], `${file}: unknown route ${href}`);
        if (url.hash) check(documents[target].ids.includes(decodeURIComponent(url.hash.slice(1))), `${file}: missing anchor ${href}`);
        linkCount++;
      }
    }
    report.internalLinksChecked = linkCount;
    const expectedFiles = Object.keys(coverage).sort();
    assert.deepEqual(fs.readdirSync(root).filter(f => f.endsWith('.html')).sort(), expectedFiles, 'All local routes must be in coverage');
    for (const file of expectedFiles) {
      for (const width of widths) {
        await p.setViewportSize({ width, height: 900 });
        await p.goto(base + file);
        await p.evaluate(async () => {
          await document.fonts.ready;
          await Promise.all([...document.images].map(i => { i.loading = 'eager'; return i.decode(); }));
          document.documentElement.style.scrollBehavior = 'auto';
        });
        const state = await p.evaluate(() => ({
          overflow: document.documentElement.scrollWidth > innerWidth,
          broken: [...document.images].some(i => !i.complete || !i.naturalWidth),
          sidebar: document.querySelector('.company-sidebar') ? getComputedStyle(document.querySelector('.company-sidebar')).position : null,
          cardColumns: document.querySelector('.product-grid') ? getComputedStyle(document.querySelector('.product-grid')).gridTemplateColumns.split(' ').length : null
        }));
        check(!state.overflow && !state.broken, `${file}: layout/assets at ${width}`);
        if (width <= 600 && state.cardColumns) assert.equal(state.cardColumns, 1, `${file}: mobile plant cards`);
        if (state.sidebar) {
          assert.equal(state.sidebar, width > 800 ? 'sticky' : 'static', `${file}: sidebar at ${width}`);
          if (width > 800) {
            await p.evaluate(() => scrollTo(0, 400));
            check(Math.abs(await p.locator('.company-sidebar').evaluate(e => e.getBoundingClientRect().top) - 24) < 2, `${file}: sticky position`);
            await p.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
            check(await p.evaluate(() => document.querySelector('.company-sidebar').getBoundingClientRect().bottom <= document.querySelector('footer').getBoundingClientRect().top), `${file}: sidebar overlaps footer`);
          }
        }
        await p.evaluate(() => scrollTo(0, 0));
        if ([1440,390].includes(width)) await p.screenshot({ path: path.join(output, `${file.slice(0,-5)}-${width}.png`), fullPage:true });
        report.layouts.push({ file, width, ...state });
      }
      process.stdout.write(`Layout OK: ${file}\n`);
    }
    // Full green/flower gallery sequences: placeholders and actual photos obey identical controls.
    for (const file of ['piante-verdi.html','piante-da-fiore.html']) {
      for (const width of [390,1440]) {
        await p.setViewportSize({width,height:900});
        await p.goto(base+file);
        const cards = p.locator('[data-lightbox-group]');
        for(let i=0;i<9;i++) {
          const trigger=cards.nth(i);
          const name=await trigger.getAttribute('data-lightbox-name');
          await trigger.click();
          check(await p.locator('dialog').isVisible(), `${file}: lightbox ${i}`);
          assert.equal(await p.locator('#dialog-title').innerText(), name);
          assert.equal(await p.locator('#lightbox-counter').innerText(), `${i+1} / 9`);
          await p.keyboard.press('Escape');
          check(await trigger.evaluate(e => e===document.activeElement), `${file}: return focus`);
        }
        await cards.first().click();
        await p.getByRole('button',{name:'Immagine successiva',exact:true}).click();
        assert.equal(await p.locator('#lightbox-counter').innerText(),'2 / 9');
        await p.keyboard.press('ArrowRight');
        assert.equal(await p.locator('#lightbox-counter').innerText(),'3 / 9');
        await p.keyboard.press('ArrowLeft');
        await p.getByRole('button',{name:'Immagine precedente',exact:true}).click();
        assert.equal(await p.locator('#lightbox-counter').innerText(),'1 / 9');
        await p.getByRole('button',{name:'Immagine precedente',exact:true}).click();
        assert.equal(await p.locator('#lightbox-counter').innerText(),'9 / 9');
        await p.screenshot({path:path.join(output,`${file.slice(0,-5)}-lightbox-${width}.png`)});
        await p.getByRole('button',{name:'Chiudi finestra',exact:true}).click();
      }
    }
    report.interactions.push('18 gallery cards at desktop/mobile; previous, next, wrap, arrows, Escape and focus restoration');
    // Demonstrative months still provide accurate full labels and keyboard/touch detail.
    for(const slug of ['pothos','ortensia','anthurium','dipladenia','monstera','phalaenopsis']) {
      await p.goto(base+slug+'.html');
      for(let i=0;i<12;i++) {
        const month=p.locator('.availability-month').nth(i);
        const name=await month.getAttribute('data-month-name');
        await month.focus(); await p.keyboard.press('Enter');
        check((await p.locator('.month-feedback').innerText()).includes(name), `${slug}: month ${i}`);
      }
    }
    report.interactions.push('72 monthly labels, states and keyboard activation');
    // Exercise every pending action: no dead controls or broken promises of real integrations.
    let actions=0;
    for(const file of expectedFiles) {
      await p.setViewportSize({width:1440,height:900});
      await p.goto(base+file);
      const keys=await p.locator('main [data-info]').evaluateAll(es=>[...new Set(es.map(e=>e.dataset.info))]);
      for(const key of keys) {
        await p.locator(`main [data-info="${key}"]`).first().click();
        check(await p.locator('dialog').isVisible(), `${file}: ${key}`);
        check((await p.locator('#dialog-title').innerText()).length>0, `${file}: dialog title`);
        await p.keyboard.press('Escape'); actions++;
      }
    }
    report.interactions.push(`${actions} page-level provisional video, contact and external-link controls`);
    for(const file of ['vivai-produttori.html','garden-center.html','grossisti.html']) {
      await p.goto(base+file);
      const quote=await p.locator('[data-testimonial-quote]').innerText();
      await p.getByRole('button',{name:'Testimonianza successiva'}).click();
      check((await p.locator('[data-testimonial-quote]').innerText())!==quote, 'Testimonial change');
      assert.equal(await p.locator('[data-testimonial-counter]').innerText(),'2 / 2');
      await p.getByRole('button',{name:'Testimonianza precedente'}).click();
      assert.equal(await p.locator('[data-testimonial-counter]').innerText(),'1 / 2');
    }
    report.interactions.push('Three editorial testimonial carousels, next and previous');
    for(const file of expectedFiles) {
      await p.setViewportSize({width:390,height:844}); await p.goto(base+file);
      await p.locator('.menu-toggle').click();
      assert.equal(await p.locator('.menu-toggle').getAttribute('aria-expanded'),'true');
      for(const name of ['Chi siamo','Prodotti','Servizi']) {
        const control=p.getByRole('button',{name:`Apri sottomenu ${name}`,exact:true});
        await control.click(); assert.equal(await control.getAttribute('aria-expanded'),'true');
        const id=await control.getAttribute('aria-controls');
        check(await p.locator('#'+id).isVisible(), `${file}: ${id}`);
      }
      await p.keyboard.press('Escape');
      assert.equal(await p.locator('.menu-toggle').getAttribute('aria-expanded'),'false');
    }
    report.interactions.push('Mobile hamburger and all three dropdowns on all 19 pages');
    await p.goto(base+'contatti.html');
    await p.locator('#contact-form button[type=submit]').click();
    check(!await p.locator('#contact-name').evaluate(e=>e.validity.valid),'Required name');
    await p.locator('#contact-name').fill('Prova locale');
    await p.locator('#contact-email').fill('non-email');
    await p.locator('#contact-subject').fill('Prova');
    await p.locator('#contact-message').fill('Messaggio dimostrativo');
    check(!await p.locator('#contact-email').evaluate(e=>e.validity.valid),'Email validation');
    await p.locator('#contact-email').fill('preview@example.com'); await p.locator('[name=privacy]').check();
    await p.locator('#contact-form button[type=submit]').click();
    check((await p.locator('.form-status').innerText()).includes('non è stato inviato'),'Local-only submit');
    report.interactions.push('Contact required/email validation and demonstrative non-sending submission');
    // One extra short desktop viewport: the entire sidebar remains reachable by scrolling it.
    await p.setViewportSize({width:1366,height:600}); await p.goto(base+'piante-verdi.html');
    check(await p.locator('.company-sidebar').evaluate(e=>e.scrollHeight>e.clientHeight),'Short-screen sidebar scrolling');
    check(!report.errors.length, report.errors.join('\n'));
    report.status='passed';
    fs.writeFileSync(path.join(output,'verifica-completa.json'),JSON.stringify(report,null,2));
    console.log(`PASS: ${report.pages.length} pages, ${report.layouts.length} layouts, ${linkCount} internal links, complete interaction checks. No browser errors.`);
  } catch(error) {
    report.status='failed'; report.failure=error.stack;
    fs.writeFileSync(path.join(output,'verifica-completa.json'),JSON.stringify(report,null,2));
    throw error;
  } finally { await browser.close(); }
})();
