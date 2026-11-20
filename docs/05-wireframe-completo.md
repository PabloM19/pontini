# Cobertura final del wireframe local

Estado: 19 de noviembre de 2026. Las 15 pantallas del PDF están representadas: 14 diseños de página y un estado de lightbox. Se añaden la categoría de flor, ausente del PDF pero confirmada en reunión, y cuatro fichas derivadas de las dos plantillas originales. Total: **19 páginas HTML navegables**. El prototipo completo se revisa desde [la home local](http://127.0.0.1:4173/).

## Inventario página por página

| Página local | Fuente | Secciones y estados implementados |
| --- | --- | --- |
| [Home](http://127.0.0.1:4173/) | W1 y diseño final de home | Hero y vídeo provisional, cinco cifras, selección de tres plantas, banner Capolavoro, tres servicios enlazados, contacto, certificaciones y pie completo. |
| [L’azienda](http://127.0.0.1:4173/azienda.html) | W2 | Vídeo, introducción, tres cifras, familia Di Girolamo, retrato provisional, foto de serre, tres fotos de detalle, texto y contacto. |
| [Tecnologie adottate](http://127.0.0.1:4173/tecnologie.html) | W3 | Serre, irrigazione, bancali, celle frigorifere, RFID, ricerca; dos vídeos provisionales, fotos/huecos y contacto. |
| [ECO investimenti](http://127.0.0.1:4173/eco-investimenti.html) | W4 | Certificazioni, acqua con vídeo, energía con dos imágenes, pesticidi y contacto. |
| [Il team](http://127.0.0.1:4173/team.html) | W5 | Imagen de grupo, introducción, ocho tarjetas, controles de teléfono/email y contacto. |
| [Contatti](http://127.0.0.1:4173/contatti.html) | W6 | Canales de contacto, mapa ilustrativo, dirección, formulario con privacidad y validación local. |
| [Prodotti](http://127.0.0.1:4173/prodotti.html) | W7 | Hero, introducción, Featured, Speciale, verde, flor, disponibilidad, descarga y certificados. |
| [Ortensia](http://127.0.0.1:4173/ortensia.html) | W8 | Nombre, tres datos, foto, doce meses, leyenda y respuesta accesible, descripción, seis espacios de galería, disponibilidad, descarga y certificados. |
| [Pothos](http://127.0.0.1:4173/pothos.html) | Plantilla W8 | Mismos bloques; datos provisionales y fotografía disponible. |
| [Anthurium](http://127.0.0.1:4173/anthurium.html) | Plantilla W8 | Mismos bloques; datos provisionales y fotografía disponible. |
| [Dipladenia](http://127.0.0.1:4173/dipladenia.html) | W9 | Ficha completa con la misma estructura; foto principal y galería pendientes. |
| [Monstera](http://127.0.0.1:4173/monstera.html) | Plantilla W9 | Ficha completa con contenido provisional. |
| [Phalaenopsis](http://127.0.0.1:4173/phalaenopsis.html) | Plantilla W9 | Ficha completa con contenido provisional. |
| [Piante verdi](http://127.0.0.1:4173/piante-verdi.html) | W10–11 | Introducción y cifras, nueve tarjetas, ampliación modal con nombre, contador, anterior/siguiente, flechas de teclado, Escape y retorno del foco; CTA y certificados. |
| [Piante da fiore](http://127.0.0.1:4173/piante-da-fiore.html) | Reunión y plantilla W10–11 | Nueve muestras y el mismo lightbox. Sin fichas de detalle desde esta categoría. |
| [Vivai produttori](http://127.0.0.1:4173/vivai-produttori.html) | W12 | Hero, introducción, especialidad de ortensie prefinite con vídeo, seis tarjetas, testimonios con controles, disponibilidad, descarga y certificados. |
| [Garden center](http://127.0.0.1:4173/garden-center.html) | W13 | Hero, introducción, Capolavoro con vídeo y enlace, seis tarjetas, testimonios, disponibilidad, descarga y certificados. |
| [Grossisti e distributori](http://127.0.0.1:4173/grossisti.html) | W14 | Hero, introducción, logística con mapa europeo, seis tarjetas, testimonios, disponibilidad, descarga y certificados. |
| [Capolavoro!](http://127.0.0.1:4173/capolavoro.html) | W15 y arte de marca | Hero oficial, vídeo provisional, introducción, tres imágenes, Etichettatura, Cartellonistica, seis tarjetas de gama y contacto. |

Cabecera, navegación y pie compartidos por las 19 páginas. Menús Chi siamo, Prodotti y Servizi con sus destinos locales. Laterales corporativos y de productos sticky en escritorio, desplazables si falta altura y dentro del flujo en móvil. Tarjetas e iconos en una columna en teléfono.

## Comprobación

La matriz verificable de bloques está en [tests/wireframe-coverage.json](../tests/wireframe-coverage.json), y el recorrido de navegador en [tests/check-wireframe.cjs](../tests/check-wireframe.cjs). El [informe de ejecución](../investigacion/qa/completo/verifica-completa.json) registra el resultado y los tamaños probados. Las capturas completas de las 19 páginas en escritorio y móvil se guardan junto al informe.

- 19 páginas con respuesta 200, idioma italiano y un título principal; sin IDs duplicados ni botones sin nombre.
- 133 layouts, siete anchuras entre 320 y 1440 px; sin desbordamientos horizontales ni imágenes rotas.
- 640 enlaces internos y sus anclas comprobados.
- Lightbox de ambas categorías en móvil/escritorio: tarjetas, anterior/siguiente, vuelta al comienzo, teclado, cierre y foco.
- Los 72 meses de las seis fichas accesibles con teclado y mensaje de disponibilidad demostrativa.
- Menú móvil y los tres submenús en las 19 páginas. Corregido el cierre prematuro al pasar entre grupos.
- Vídeos y destinos provisionales con diálogo; tres carruseles de testimonios editoriales; formulario con campos obligatorios, email y confirmación explícita de no envío.
- Revisión visual de capturas de todas las páginas y lateral desplazable en escritorio de poca altura.

## Pendientes de contenido y siguiente fase

La estructura del wireframe está completa. Quedan sustituciones editoriales y conexiones reales: textos italianos validados; fotografías/vídeos definitivos; personas, testimonios, cifras y disponibilidad; archivos PDF y enlaces externos; legales; fuentes y artes finales. Pothos normaliza provisionalmente «Photos» del PDF. La lista de Speciale de seis o siete especies estimada en reunión no se ha entregado: están las tres identificadas y su plantilla lista para duplicar.

Las fotos de referencia y el mapa de Europa no acreditan instalaciones, personas ni cobertura logística reales. Las disponibilidades no son comerciales. El formulario es local, sin backend. Los controles pendientes explican su estado y no simulan descargas ni envíos. La tipografía Acta Display queda pendiente de original/licencia; se usa Georgia provisionalmente.

No se ha integrado esta maqueta en WordPress ni publicado. Se conserva el flujo acordado: revisar italiano y diseño local, integrar en staging editable y después incorporar inglés y producción.
