"""Generate the remaining local wireframe pages; normalize shared navigation.

Run from the project root with Python 3. Existing hand-authored pages are kept.
"""
from pathlib import Path
from html import escape
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
LOREM = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vitae purus '
         'eget sapien feugiat sollicitudin. Nulla facilisi. Donec tincidunt, sapien sed '
         'dignissim consequat, neque arcu malesuada justo, vitae viverra eros enim eget urna.')
MORE = ('Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae. '
        'Aliquam erat volutpat. Morbi commodo, erat ut consequat finibus, tortor lorem posuere nisl.')
template = (ROOT / 'prodotti.html').read_text()
prefix = template[:template.index('<main id="contenuto">')]
suffix = template[template.index('</main>') + len('</main>'):]
plant_template = (ROOT / 'ortensia.html').read_text()
sidebar = re.search(r'<aside class="company-sidebar plant-sidebar"[\s\S]*?</aside>', plant_template)[0]


def page(filename, title, body, section='prodotti', with_sidebar=False):
    head = re.sub(r'<title>.*?</title>', f'<title>{escape(title)} — Vivai Pontini</title>', prefix)
    head = re.sub(r'<body[^>]*>', '<body class="wireframe-page">', head)
    head = head.replace(' aria-current="page"', '').replace(' class="current"', '')
    head = head.replace(f'href="{section}.html">', f'href="{section}.html" class="current">', 1)
    if with_sidebar:
        side = sidebar.replace(' aria-current="page"', '')
        # Normalization below makes category links point to the new pages.
        side = side.replace(f'href="prodotti.html#{filename[:-5]}"', f'href="{filename}" aria-current="page"')
        body = f'<main id="contenuto" class="company-layout container">{side}<div class="company-content category-content">{body}</div></main>'
    else:
        body = '<main id="contenuto">' + body + '</main>'
    (ROOT / filename).write_text(head + body + suffix)


def placeholder(label, extra=''):
    return f'<div class="catalog-placeholder {extra}" role="img" aria-label="{escape(label)} — immagine da inserire"><svg aria-hidden="true"><use href="#i-leaf"/></svg><span>{escape(label)}</span><small>Immagine da inserire</small></div>'


def downloads():
    return '<section class="catalog-downloads" aria-label="Disponibilità e cataloghi"><button class="button gold-button" data-info="disponibilita">Disponibilità settimanale</button><button class="button outline-button" data-info="download-catalogo">Download catalogo<svg class="arrow"><use href="#i-arrow"/></svg></button></section>'


def certs():
    return '<section class="catalog-certifications" aria-labelledby="quality-title"><h2 id="quality-title">Certificazioni di qualità</h2><div class="certification-logos"><img src="assets/grasp.jpg" width="202" height="235" alt="GRASP Global G.A.P." loading="lazy"><img src="assets/globalgap.png" width="300" height="300" alt="GLOBALG.A.P." loading="lazy"></div></section>'


def cta():
    return '<section class="company-cta" aria-labelledby="cta-title"><div><h2 id="cta-title">Parli con noi</h2><p>Il nostro staff è a tua disposizione per informazioni e preventivi.</p></div><a class="button white-button" href="contatti.html">Contattaci<svg class="arrow"><use href="#i-arrow"/></svg></a></section>'


def hero(title):
    return f'<section class="hero catalog-hero" aria-labelledby="page-title"><img class="hero-photo" src="assets/hero.jpg" width="1500" height="524" alt="Coltivazione nelle serre Vivai Pontini" fetchpriority="high"><div class="hero-shade"></div><div class="hero-content container"><h1 id="page-title">{title}</h1><div class="hero-rule"></div><button class="button video-button" data-info="disponibilita">Disponibilità settimanale</button></div></section>'


def video(key, label):
    return f'<button class="tech-media tech-video" data-info="{key}" aria-label="Anteprima video: {label}"><span class="video-play"><span class="play" aria-hidden="true"></span></span><span>{label}</span><small>Video in preparazione</small></button>'


for original, name in [('p14-I2.jpg', 'logistica-europa.jpg')]:
    shutil.copy(ROOT / 'investigacion/wireframe/resources' / original, ROOT / 'assets' / name)
shutil.copy(ROOT / 'investigacion/brand/recursos-referencia/p31-Im0.png', ROOT / 'assets/sansevieria-riferimento.png')

green_names = ['Beaucarnea', 'Ficus', 'Dracaena', 'Sansevieria', 'Spathiphyllum', 'Strelitzia', 'Beaucarnea', 'Ficus', 'Dracaena']
flower_names = ['Ortensia', 'Anthurium', 'Dipladenia', 'Phalaenopsis', 'Ortensia', 'Anthurium', 'Dipladenia', 'Phalaenopsis', 'Ortensia']
galleries = {}
for slug, title, names, values in [
    ('piante-verdi', 'Piante verdi', green_names, ['1.100', '270.000', '43']),
    ('piante-da-fiore', 'Piante da fiore', flower_names, ['—', '—', '—'])
]:
    items = []
    for i, name in enumerate(names):
        image = ('sansevieria-riferimento.png' if name == 'Sansevieria' else None) if slug == 'piante-verdi' else {'Ortensia': 'ortensia.webp', 'Anthurium': 'anthurium.webp'}.get(name)
        items.append({'name': name, 'image': image, 'reference_only': True})
    galleries[slug] = items
    stats = '<dl class="numbers company-numbers">' + ''.join(
        f'<div><span class="round-icon"><svg aria-hidden="true"><use href="#{icon}"/></svg></span><dt>{value}</dt><dd>{label}</dd></div>'
        for value, icon, label in zip(values, ['i-field', 'i-leaf', 'i-greenhouse'], ['m² di superficie<br>produttiva', 'piante prodotte<br>ogni anno', 'formati<br>disponibili'])
    ) + '</dl>'
    cards = ''
    for i, item in enumerate(items):
        media = f'<img src="assets/{item["image"]}" alt="" loading="lazy">' if item['image'] else placeholder(item['name']).replace('<div ', '<span ').replace('</div>', '</span>')
        cards += f'<button class="category-plant" data-lightbox-group="{slug}" data-lightbox-name="{item["name"]}" data-lightbox-image="{("assets/" + item["image"]) if item["image"] else ""}" aria-label="Apri immagine di {item["name"]}, posizione {i+1}"><span class="category-plant-media">{media}</span><span class="category-plant-name">{item["name"]}</span></button>'
    note = 'Valori del wireframe, da confermare.' if slug == 'piante-verdi' else 'Dati tecnici e selezione in aggiornamento.'
    body = f'<h1>{title}</h1>{stats}<p class="plant-data-note">{note}</p><div class="company-copy category-intro"><p>{LOREM}</p></div><p class="reference-note">Selezione dimostrativa · Immagini di riferimento e segnaposto. Tocca una pianta per ingrandirla.</p><section class="category-gallery" aria-label="Galleria {title.lower()}">{cards}</section>{downloads()}{certs()}'
    page(slug + '.html', title, body, with_sidebar=True)
(ROOT / 'data/galleries.json').write_text(json.dumps(galleries, ensure_ascii=False, indent=2))

plants = [('pothos', 'Pothos'), ('ortensia', 'Ortensia (Hydrangea)'), ('anthurium', 'Anthurium')]


def range_grid():
    # Six positions as drawn in the PDF. Repeated names remain sample variations.
    cards = ''
    for row in range(2):
        for slug, name in plants:
            media = f'<img src="assets/{slug}.webp" alt="{name}" loading="lazy">' if row == 0 else placeholder(name).replace('<div ', '<span ').replace('</div>', '</span>')
            cards += f'<a class="product" href="{slug}.html"><span class="product-image">{media}</span><h3>{name}</h3></a>'
    return '<div class="product-grid range-grid">' + cards + '</div>'


def testimonials():
    return f'''<section class="testimonials container" aria-labelledby="testimonials-title" aria-roledescription="carosello">
    <h2 class="section-title" id="testimonials-title">Testimonianze</h2>
    <p class="reference-note">Contenuto dimostrativo · Blocco da confermare.</p>
    <div class="testimonial-stage"><div class="team-avatar" aria-hidden="true"><svg viewBox="0 0 64 64"><circle cx="32" cy="22" r="10"/><path d="M12 56v-5a20 20 0 0 1 40 0v5"/></svg></div>
    <div class="testimonial-copy"><h3 data-testimonial-name>Nome e cognome</h3><p class="team-role">Posizione in azienda</p><blockquote data-testimonial-quote>{LOREM}</blockquote></div>
    <div class="testimonial-controls"><button type="button" data-testimonial-step="-1" aria-label="Testimonianza precedente">‹</button><button type="button" data-testimonial-step="1" aria-label="Testimonianza successiva">›</button><p data-testimonial-counter role="status">1 / 2</p></div></div></section>'''


services = [
    ('vivai-produttori', 'Vivai produttori', 'Piante semilavorate per vivai produttori', 'Specialisti in ortensie prefinite', 'Gamma di specie semilavorate', video('video-ortensie', 'Ortensie prefinite')),
    ('garden-center', 'Garden center', 'Piante finite per garden center', 'Capolavoro! Il brand per il consumatore', 'Gamma di piante per garden center', video('video-capolavoro', 'Capolavoro!')),
    ('grossisti', 'Grossisti e distributori', 'Fornitura di piante per grossisti', 'Il miglior servizio logistico', 'Gamma di piante per grossisti', '<figure class="service-map"><img src="assets/logistica-europa.jpg" width="1200" height="675" alt="Mappa illustrativa dell’Europa" loading="lazy"><figcaption>Mappa illustrativa · Copertura da confermare.</figcaption></figure>')
]
for slug, title, headline, specialty, range_title, medium in services:
    action = '<a href="capolavoro.html" class="button gold-button">Scopri di più<svg class="arrow"><use href="#i-arrow"/></svg></a>' if slug == 'garden-center' else ''
    body = hero(headline) + f'<div class="catalog-intro container"><p><strong>Vivai Pontini</strong> — {LOREM}</p></div>'
    body += f'<section class="service-specialty container" aria-labelledby="specialty-title"><h2 class="section-title" id="specialty-title">{specialty}</h2><div class="service-split"><div class="company-copy"><p>{LOREM}</p><p>{MORE}</p>{action}</div>{medium}</div></section>'
    body += f'<section class="service-range container" aria-labelledby="range-title"><h2 class="section-title" id="range-title">{range_title}</h2><p class="reference-note">Selezione e immagini dimostrative.</p>{range_grid()}</section>{testimonials()}<div class="container">{downloads()}{certs()}</div>'
    page(slug + '.html', title, body, section='vivai-produttori')

cap_hero = '''<section class="cap-brand-hero" aria-labelledby="cap-title"><h1 id="cap-title" class="sr-only">Capolavoro! The Art of Italian Plants</h1><img class="cap-hero-art" src="assets/capolavoro-banner.webp" width="2160" height="560" alt="Vivai Pontini Capolavoro! The Art of Italian Plants. Ogni esemplare è una vera opera maestra!" fetchpriority="high"><div class="container"><p>Il marchio di Vivai Pontini pensato per conquistare il consumatore</p><button class="button cap-video-button" data-info="video-capolavoro"><span class="play" aria-hidden="true"></span>Scopri di più</button></div></section>'''
triptych = '<div class="cap-triptych container" aria-label="Immagini di riferimento Capolavoro!">'
for src, alt in [('azienda-coltivazione.webp', 'La coltivazione'), ('azienda-vasi.webp', 'Dettaglio di vasi in terracotta'), ('anthurium.webp', 'Anthurium')]:
    triptych += f'<figure><img src="assets/{src}" alt="{alt}, immagine di riferimento" loading="lazy"></figure>'
triptych += '</div>'
label_img = '<figure class="cap-label-image"><img src="assets/sansevieria-riferimento.png" alt="Esempio di etichetta Capolavoro! applicata a una Sansevieria, dal manuale di marca" loading="lazy"></figure>'
body = cap_hero + f'<div class="catalog-intro container"><p>{LOREM}</p></div>' + triptych
body += f'<section class="cap-materials container" aria-labelledby="materials-title"><h2 class="section-title" id="materials-title">Etichettatura e cartellonistica per il punto vendita</h2><div class="tech-blocks"><section class="tech-block" aria-labelledby="label-title"><h3 id="label-title">Etichettatura</h3><div class="tech-row"><div class="company-copy"><p>{LOREM}</p><p>{MORE}</p></div><div class="tech-media">{label_img}</div></div></section><section class="tech-block" aria-labelledby="signage-title"><h3 id="signage-title">Cartellonistica</h3><div class="tech-row"><div class="company-copy"><p>{LOREM}</p><p>{MORE}</p></div>{placeholder('Cartellonistica per il punto vendita', 'tech-media')}</div></section></div></section>'
body += f'<section class="service-range container" aria-labelledby="cap-range-title"><h2 class="section-title" id="cap-range-title">Gamma di piante Capolavoro!</h2><p class="reference-note">Selezione e immagini dimostrative.</p>{range_grid()}</section><div class="container cap-cta">{cta()}</div>'
page('capolavoro.html', 'Capolavoro!', body, section='capolavoro')

# Shared destinations: make every existing page enter the real route.
for path in ROOT.glob('*.html'):
    html = path.read_text()
    for old, new in [
        ('index.html#capolavoro', 'capolavoro.html'), ('#capolavoro', 'capolavoro.html'),
        ('index.html#servizi', 'vivai-produttori.html'), ('#servizi', 'vivai-produttori.html'),
        ('index.html#vivai', 'vivai-produttori.html'), ('#vivai', 'vivai-produttori.html'),
        ('index.html#grossisti', 'grossisti.html'), ('#grossisti', 'grossisti.html'),
        ('index.html#garden', 'garden-center.html'), ('#garden', 'garden-center.html'),
        ('prodotti.html#piante-verdi', 'piante-verdi.html'), ('prodotti.html#piante-da-fiore', 'piante-da-fiore.html'),
    ]:
        html = html.replace(f'href="{old}"', f'href="{new}"')
    html = html.replace('<button class="button category-button" data-info="verdi">', '<a class="button category-button" href="piante-verdi.html">')
    html = html.replace('<button class="button category-button" data-info="fiore">', '<a class="button category-button" href="piante-da-fiore.html">')
    html = re.sub(r'(<a class="button category-button"[\s\S]*?)</button>', r'\1</a>', html)
    # Use standard active states; parent section links use a visual class only.
    html = re.sub(r'(<a href="(?:capolavoro|vivai-produttori|prodotti)\.html") (?:class="current"|aria-current="page")', r'\1', html)
    section = 'prodotti' if path.stem in ['prodotti', 'piante-verdi', 'piante-da-fiore', 'ortensia', 'pothos', 'anthurium', 'dipladenia', 'monstera', 'phalaenopsis'] else 'capolavoro' if path.stem == 'capolavoro' else 'vivai-produttori' if path.stem in ['vivai-produttori', 'garden-center', 'grossisti'] else None
    if section:
        html = html.replace(f'<a href="{section}.html">', f'<a href="{section}.html" class="current">', 1)
    # No accidental nested tags in placeholder button cards.
    html = html.replace('href="#"', 'href="index.html"')
    path.write_text(html)

# Home's services and Capolavoro banner must be clickable as in the wireframe.
home = (ROOT / 'index.html').read_text()
for id_, target in [('vivai', 'vivai-produttori'), ('grossisti', 'grossisti'), ('garden', 'garden-center')]:
    pattern = rf'(<article id="{id_}">)([\s\S]*?)(</article>)'
    home = re.sub(pattern, lambda m: m[1] + f'<a class="service-card-link" href="{target}.html">' + m[2] + '</a>' + m[3] if 'service-card-link' not in m[2] else m[0], home)
if 'class="cap-banner-link"' not in home:
    home = home.replace('<h2 class="sr-only">Vivai Pontini Capolavoro!</h2>', '<a class="cap-banner-link" href="capolavoro.html"><h2 class="sr-only">Vivai Pontini Capolavoro!</h2>')
    home = home.replace('</div>\n  </section>\n  <section class="services', '</div></a>\n  </section>\n  <section class="services')
(ROOT / 'index.html').write_text(home)
print('Generated 6 remaining pages and normalized navigation across all 19 local pages.')
