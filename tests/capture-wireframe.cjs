const { chromium } = require('playwright');
const fs = require('node:fs');
(async () => {
  const browser = await chromium.launch({headless:true});
  try {
    const page = await browser.newPage();
    const errors=[];
    page.on('pageerror', e=>errors.push(e.message));
    page.on('response', r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`)});
    const output=[];
    for (const file of ['piante-verdi','piante-da-fiore','vivai-produttori','garden-center','grossisti','capolavoro']) {
      for(const width of [1440,390]) {
        await page.setViewportSize({width,height:900});
        await page.goto(`http://127.0.0.1:4173/${file}.html`);
        await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>{i.loading='eager';return i.decode()}));});
        output.push({file,width,overflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth)});
        await page.screenshot({path:`investigacion/qa/${file}-${width}.png`,fullPage:true});
      }
    }
    console.log(JSON.stringify({output,errors},null,2));
  } finally {await browser.close()}
})();
