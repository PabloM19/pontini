const header = document.querySelector('.site-header');
const menuButton = document.querySelector('.menu-toggle');
const dropdowns = [...document.querySelectorAll('.dropdown')];
function closeDropdowns(except) {
  dropdowns.forEach(item => {
    if (item === except) return;
    item.classList.remove('open');
    item.querySelector('.submenu-toggle').setAttribute('aria-expanded', 'false');
  });
}
function closeMenu() {
  header.classList.remove('menu-open');
  menuButton.setAttribute('aria-expanded', 'false');
  closeDropdowns();
}
menuButton.addEventListener('click', () => {
  const open = header.classList.toggle('menu-open');
  menuButton.setAttribute('aria-expanded', String(open));
  if (!open) closeDropdowns();
});
dropdowns.forEach(item => {
  const button = item.querySelector('.submenu-toggle');
  let openedByHover = false;
  const setOpen = open => {
    if (open) closeDropdowns(item);
    item.classList.toggle('open', open);
    button.setAttribute('aria-expanded', String(open));
  };
  button.addEventListener('click', () => { setOpen(openedByHover || !item.classList.contains('open')); openedByHover = false; });
  item.addEventListener('mouseenter', () => { if (matchMedia('(hover: hover) and (min-width: 1001px)').matches) { setOpen(true); openedByHover = true; } });
  item.addEventListener('mouseleave', () => { if (matchMedia('(hover: hover) and (min-width: 1001px)').matches) { setOpen(false); openedByHover = false; } });
  item.addEventListener('focusout', event => {
    // On mobile, collapsing a group during pointer focus moves the next button
    // before its click can finish. Explicit controls close the accordion there.
    if (matchMedia('(min-width: 1001px)').matches && !item.contains(event.relatedTarget)) setOpen(false);
  });
});
document.addEventListener('click', event => {
  if (!header.contains(event.target)) closeMenu();
  if (event.target.closest('nav a')) closeMenu();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && !dialog.open) {
    const focusTarget = matchMedia('(max-width: 1000px)').matches ? menuButton : header.querySelector('.dropdown.open .submenu-toggle');
    closeMenu();
    focusTarget?.focus();
  }
});
matchMedia('(min-width: 1001px)').addEventListener('change', closeMenu);

const dialog = document.getElementById('preview-dialog');
const content = document.getElementById('dialog-content');
const info = {
  'video-ortensie': ['Ortensie prefinite', 'Video in preparazione.', 'Il video dedicato alla coltivazione delle ortensie sarà inserito dopo la consegna del materiale definitivo.'],
  'video-capolavoro': ['Capolavoro!', 'The Art of Italian Plants', 'Il video dedicato al marchio Capolavoro! sarà inserito prossimamente.'],
  disponibilita: ['Disponibilità settimanale', 'Elenco in aggiornamento.', 'Il collegamento al servizio di disponibilità settimanale sarà inserito prossimamente. Per conoscere le piante disponibili puoi contattarci ai recapiti qui sotto.'],
  'download-catalogo': ['Download catalogo', 'Catalogo in preparazione.', 'Il catalogo PDF sarà disponibile prossimamente. Nel frattempo puoi richiedere informazioni al Consorzio.'],
  'contatto-team': ['Contatti del team', 'Recapiti in aggiornamento.', 'I nomi, i ruoli e i recapiti individuali saranno inseriti prossimamente. Nel frattempo puoi contattare il Consorzio ai recapiti generali qui sotto.'],
  'video-acqua': ['Riutilizzo dell’acqua di irrigazione', 'Video in preparazione.', 'Il video dedicato al riutilizzo dell’acqua sarà inserito prossimamente.'],
  'video-irrigazione': ['Sistema a flusso e riflusso', 'Video in preparazione.', 'Il video dedicato al sistema di irrigazione sarà inserito prossimamente.'],
  'video-rfid': ['Gestione e logistica RFID', 'Video in preparazione.', 'Il video dedicato alla gestione delle scorte e delle spedizioni sarà inserito prossimamente.'],
  whatsapp: ['WhatsApp', 'Restiamo in contatto.', 'Il collegamento WhatsApp sarà disponibile dopo la conferma del numero dedicato. Nel frattempo puoi chiamarci o scriverci via email.'],
  video: ['Video corporate', 'La nostra passione, ogni giorno.', 'Il video di presentazione del Consorzio Vivai Pontini sarà disponibile prossimamente.'],
  b2b: ['Area riservata B2B', 'Uno spazio dedicato ai nostri partner.', 'L’accesso all’area riservata sarà disponibile prossimamente. Per informazioni puoi contattarci direttamente.'],
  catalogo: ['Il nostro catalogo', 'Una selezione coltivata con passione.', 'Prodotti Featured, Collezione Speciale, Piante verdi e Piante da fiore: il catalogo completo e i PDF da scaricare saranno disponibili prossimamente.'],
  speciale: ['Collezione Speciale', 'Varietà dal carattere unico.', 'La selezione completa è in preparazione. Contattaci per conoscere le nostre piante e la loro disponibilità.'],
  verdi: ['Piante verdi', 'La natura, in tutte le sue forme.', 'La galleria completa delle nostre piante verdi sarà disponibile prossimamente.'],
  fiore: ['Piante da fiore', 'Il colore prende vita.', 'La galleria completa delle nostre piante da fiore sarà disponibile prossimamente.'],
  tecnologie: ['Tecnologie adottate', 'Tradizione e innovazione si incontrano.', 'Una sezione dedicata alle nostre serre, ai sistemi di irrigazione e alle tecnologie di coltivazione. Contenuti in preparazione.'],
  eco: ['ECO investimenti', 'Coltivare guardando al futuro.', 'La sezione dedicata a sostenibilità, acqua ed energia è in preparazione.'],
  team: ['Il team', 'Le persone dietro ogni pianta.', 'Presto potrai conoscere il team del Consorzio Vivai Pontini.'],
  privacy: ['Privacy Policy', 'Informativa in preparazione.', 'Il testo definitivo sarà inserito prima della pubblicazione del sito.'],
  cookies: ['Cookie Policy', 'Informativa in preparazione.', 'Questa anteprima utilizza risorse locali, senza strumenti di analisi o contenuti esterni incorporati.'],
  preferenze: ['Preferenze cookie', 'Nessuna preferenza da configurare.', 'Questa anteprima non installa cookie di analisi o pubblicità.'],
  social: ['Restiamo in contatto', 'Seguici, cresciamo insieme.', 'I collegamenti ai profili ufficiali saranno disponibili prossimamente.'],
  newsletter: ['La newsletter Vivai Pontini', 'Novità, piante e ispirazioni.', 'Le iscrizioni apriranno prossimamente. Nel frattempo puoi scriverci per ricevere informazioni.']
};
const plants = {
  dipladenia: {name:'Dipladenia (Mandevilla)',image:null,copy:'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean tempus sem arcu, sit amet mattis ex tempor non.'},
  monstera: {name:'Monstera',image:null,copy:'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis massa purus, ornare et auctor eu, rutrum et turpis.'},
  phalaenopsis: {name:'Phalaenopsis',image:null,copy:'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas scelerisque, ligula non imperdiet bibendum.'},
  pothos: {name:'Pothos',image:'pothos.webp',copy:'Foglie generose e sfumature di verde. Una delle piante protagoniste della nostra selezione.'},
  ortensia: {name:'Ortensia',image:'ortensia.webp',copy:'Fioriture ricche e una palette naturale di colori, dal rosa all’azzurro. Scopri la nostra passione per le ortensie.'},
  anthurium: {name:'Anthurium',image:'anthurium.webp',copy:'Forme eleganti e colori intensi. Una presenza distintiva nella nostra selezione di piante ornamentali.'}
};
let returnFocus;
function openDialog(html) {
  dialog.classList.remove('gallery-dialog');
  returnFocus = document.activeElement;
  if (header.contains(returnFocus)) {
    returnFocus = matchMedia('(max-width: 1000px)').matches ? menuButton : (returnFocus.closest('.dropdown')?.querySelector('.submenu-toggle') || returnFocus);
    closeMenu();
  }
  content.innerHTML = html;
  dialog.showModal();
  document.body.style.overflow = 'hidden';
}
document.querySelectorAll('[data-info]').forEach(button => button.addEventListener('click', () => {
  const [title, lead, description] = info[button.dataset.info];
  openDialog(`<p class="eyebrow">Vivai Pontini</p><h2 id="dialog-title">${title}</h2><p><strong>${lead}</strong></p><p>${description}</p><div class="dialog-links"><a href="mailto:info@vivaipontini.it">Scrivici</a><a href="tel:+390773852003">+39 0773 852003</a></div>`);
}));
document.querySelectorAll('[data-plant]').forEach(button => button.addEventListener('click', () => {
  const plant = plants[button.dataset.plant];
  const media = plant.image
    ? `<img class="dialog-image" src="assets/${plant.image}" alt="${plant.name}">`
    : '<div class="catalog-placeholder dialog-placeholder"><svg aria-hidden="true"><use href="#i-leaf"/></svg><span>Immagine da inserire</span></div>';
  openDialog(`${media}<p class="eyebrow">Selezione di piante ornamentali</p><h2 id="dialog-title">${plant.name}</h2><p>${plant.copy}</p><p>La scheda completa sarà disponibile prossimamente. Contattaci per maggiori informazioni.</p><div class="dialog-links"><a href="mailto:info@vivaipontini.it">Richiedi informazioni</a></div>`);
}));
document.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => {
  const rect = dialog.getBoundingClientRect();
  if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
});
dialog.addEventListener('close', () => {
  document.body.style.overflow = '';
  dialog.classList.remove('gallery-dialog');
  lightboxItems = [];
  returnFocus?.focus();
});

document.querySelectorAll('.availability-month').forEach(button => {
  button.addEventListener('click', () => {
    const feedback = button.closest('.plant-availability').querySelector('.month-feedback');
    feedback.textContent = `${button.dataset.monthName}: ${button.dataset.monthState}. Dato dimostrativo, da confermare.`;
  });
});

// A single accessible lightbox covers real photographs and missing-image slots.
let lightboxItems = [];
let lightboxIndex = 0;
function showLightboxItem() {
  const item = lightboxItems[lightboxIndex];
  const media = document.getElementById('lightbox-media');
  media.replaceChildren();
  if (item.image) {
    const img = document.createElement('img');
    img.src = item.image;
    img.alt = item.name;
    media.append(img);
  } else {
    const placeholder = document.createElement('div');
    placeholder.className = 'catalog-placeholder lightbox-placeholder';
    const leaf = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    leaf.setAttribute('aria-hidden', 'true');
    const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    use.setAttribute('href', '#i-leaf');
    leaf.append(use);
    const label = document.createElement('span');
    label.textContent = 'Immagine da inserire';
    placeholder.append(leaf, label);
    media.append(placeholder);
  }
  document.getElementById('dialog-title').textContent = item.name;
  document.getElementById('lightbox-counter').textContent = `${lightboxIndex + 1} / ${lightboxItems.length}`;
}
function moveLightbox(step) {
  lightboxIndex = (lightboxIndex + step + lightboxItems.length) % lightboxItems.length;
  showLightboxItem();
}
function openLightbox(items, index) {
  openDialog('<div id="lightbox-media"></div><div class="lightbox-caption"><h2 id="dialog-title"></h2><p>Immagine di riferimento · Contenuto provvisorio.</p></div><div class="lightbox-controls"><button type="button" aria-label="Immagine precedente" data-lightbox-step="-1">‹</button><p id="lightbox-counter" role="status"></p><button type="button" aria-label="Immagine successiva" data-lightbox-step="1">›</button></div>');
  lightboxItems = items;
  lightboxIndex = index;
  dialog.classList.add('gallery-dialog');
  dialog.querySelectorAll('[data-lightbox-step]').forEach(button => button.addEventListener('click', () => moveLightbox(Number(button.dataset.lightboxStep))));
  showLightboxItem();
}
document.querySelectorAll('[data-lightbox-group]').forEach(button => {
  button.addEventListener('click', () => {
    const group = [...document.querySelectorAll('[data-lightbox-group]')].filter(item => item.dataset.lightboxGroup === button.dataset.lightboxGroup);
    openLightbox(group.map(item => ({ name: item.dataset.lightboxName, image: item.dataset.lightboxImage })), group.indexOf(button));
  });
});
document.querySelectorAll('[data-gallery-image]').forEach(button => {
  button.addEventListener('click', () => openLightbox([{ name: button.dataset.galleryAlt, image: button.dataset.galleryImage }], 0));
});
dialog.addEventListener('keydown', event => {
  if (!lightboxItems.length) return;
  if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
    event.preventDefault();
    moveLightbox(event.key === 'ArrowLeft' ? -1 : 1);
  }
});

document.querySelectorAll('.testimonials').forEach(section => {
  const quotes = [
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vitae purus eget sapien feugiat sollicitudin. Nulla facilisi. Donec tincidunt, sapien sed dignissim consequat, neque arcu malesuada justo.',
    'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae. Aliquam erat volutpat. Morbi commodo, erat ut consequat finibus, tortor lorem posuere nisl.'
  ];
  let current = 0;
  section.querySelectorAll('[data-testimonial-step]').forEach(button => button.addEventListener('click', () => {
    current = (current + Number(button.dataset.testimonialStep) + quotes.length) % quotes.length;
    section.querySelector('[data-testimonial-quote]').textContent = quotes[current];
    section.querySelector('[data-testimonial-counter]').textContent = `${current + 1} / ${quotes.length}`;
  }));
});

const contactForm = document.getElementById('contact-form');
contactForm?.addEventListener('submit', event => {
  event.preventDefault();
  if (!contactForm.reportValidity()) return;
  const status = contactForm.querySelector('.form-status');
  status.textContent = 'Anteprima completata. Il messaggio non è stato inviato: per contattarci, scrivi a info@vivaipontini.it.';
  status.focus();
});
