# Mapa de páginas y flujos de Vivai Pontini

El wireframe contiene 15 láminas: 12 páginas de sección, dos fichas de ejemplo y un lightbox abierto. Piante da fiore está previsto en navegación y reunión, pero carece de pantalla propia. Al incorporarlo, el alcance estructural será de 13 páginas de sección más las fichas definitivas.

Con tres Featured y seis o siete Speciale resultarían unas 22 o 23 rutas italianas; con doce fichas serían 25. Es un cálculo de dimensionamiento, pendiente de la lista final, y no incluye futuros documentos legales ni duplica rutas por inglés.

Las páginas W citadas corresponden al [wireframe original](../wireframe-Pontini.pdf). El [inventario estructurado](../investigacion/wireframe/page-inventory.json) conserva bloques y huecos de medios por página.

## Rutas propuestas

Los nombres de ruta son una propuesta técnica. El PDF define pantallas y destinos, no slugs web.

| Pantalla | Ruta italiana propuesta | Fuente y tipo |
| --- | --- | --- |
| Home | / | W 1 y home diseñada H. |
| L’azienda | /chi-siamo/azienda/ | W 2; entrada de Chi siamo. |
| Tecnologie adottate | /chi-siamo/tecnologie/ | W 3. |
| ECO investimenti | /chi-siamo/eco-investimenti/ | W 4. |
| Il team | /chi-siamo/team/ | W 5. |
| Contatti | /contatti/ | W 6; comparte lateral corporativo. |
| Prodotti | /prodotti/ | W 7; portada de catálogo. |
| Featured | /prodotti/#prodotti-featured | Sección de W 7; ancla propuesta. |
| Collezione Speciale | /prodotti/#collezione-speciale | Sección de W 7; ancla propuesta. |
| Ficha por planta | /prodotti/{slug-planta}/ | W 8 y 9 son ejemplos; cada especie con ficha tendrá su ruta. |
| Piante verdi | /prodotti/piante-verdi/ | W 10; categoría con galería. |
| Piante da fiore | /prodotti/piante-da-fiore/ | Requerida; se propone reutilizar la plantilla de W 10. |
| Lightbox | Sin ruta independiente | W 11 es un estado de W 10. |
| Vivai produttori | /servizi/vivai-produttori/ | W 12; destino de Servizi en el PDF. |
| Garden center | /servizi/garden-center/ | W 13. |
| Grossisti | /servizi/grossisti/ | W 14. |
| Capolavoro! | /capolavoro/ | W 15. |

El PDF no representa una portada independiente de Chi siamo ni de Servizi. El menú Chi siamo abre L’azienda y Servizi abre Vivai produttori. Featured y Speciale son bloques de la portada Prodotti; crear listados independientes ampliaría la estructura representada.

## Navegación común

| Elemento | Estructura y destino | Estado |
| --- | --- | --- |
| Logo | Retorno a home. | Propuesta de comportamiento; el logo del PDF es un marcador sin enlace. |
| Chi siamo | L’azienda; desplegable con L’azienda, Tecnologie adottate, ECO investimenti, Il team y Contatti. | Destino principal W 2; desplegable requerido por reunión. |
| Capolavoro! | Página de marca W 15. | Confirmado por enlaces PDF. |
| Prodotti | Portada W 7; desplegable con las cuatro categorías. | Desplegable requerido. Anclas para Featured/Speciale propuestas; verde/flor a sus categorías. |
| Servizi | Entrada W 12; desplegable con Vivai produttori, Garden center y Grossisti. | Destino principal PDF y desplegable requerido. |
| Contatti | W 6. | Confirmado. |
| Area riservata B2B | Aplicación externa del cliente. | Comportamiento confirmado, URL pendiente. El arte escribe «Área», por revisar. |
| IT y EN | Selector de idioma. | Idiomas confirmados; estados y equivalencia de páginas por implementar. |

No se dibujan estados desplegados ni pantallas móviles. Se recomienda separar el enlace de sección del control de apertura del submenú cuando sea necesario, con navegación por teclado y toque. El lateral puede convertirse en un control compacto en móvil, manteniendo acceso a sus opciones; su diseño se revisará con la primera maqueta.

### Lateral de empresa

W 2–6 comparten L’azienda, Tecnologie adottate, ECO investimenti, Il team y Contatti, seguidos de Facebook, Instagram y LinkedIn. Debajo aparece el banner Capolavoro!, enlazado a W 15. La opción activa se distingue del resto.

En W 3 faltan anotaciones tanto en opciones que visualmente parecen enlaces como en el banner lateral; en W 5 falta la de Tecnologie. La web debe reconstruir el conjunto completo según la reunión.

### Lateral de productos

W 8–10 muestran Featured con sus tres plantas; Speciale con Dipladenia, Monstera, Phalaenopsis y continuación; Piante verde y Piante da fiore. Debajo aparece el banner Capolavoro!. La lista definitiva de fichas alimentará este menú para mantenerlo coherente con la portada.

### Pie común

W muestra logo, razón social, dirección, teléfono y correo; navegación; redes y newsletter. H amplía la composición con Privacy Policy, Cookie Policy y Gestisci preferenze cookie. Se propone extender el pie diseñado de H al resto de páginas.

Datos presentes: Consorzio Vivai Pontini; Via Migliara, 53 1/2 DX n°245, 04014 Pontinia (LT), Italy; +39 0773 852003; info@vivaipontini.it. Su validación final forma parte de la entrega editorial. Los destinos de redes, newsletter y enlaces legales están pendientes.

## Bloques por página

### Home

H es la referencia visual principal. Orden: cabecera, hero con vídeo, cinco cifras e introducción, selección de tres plantas, banner Capolavoro!, tres públicos profesionales, contacto, certificaciones y asociación, pie. El [documento de marca](03-marca-y-recursos.md) detalla su composición.

W 1 representa la misma familia de bloques con tres cifras, títulos y orden de servicios diferentes. Sus tarjetas Featured llevan a la ficha ejemplo W 8; el CTA «Vedere tutti il catalogo» lleva a W 7; servicios a W 12–14; contacto a W 6; Capolavoro! a W 15. El nuevo texto de H «Scopri il catalogo» debe contrastarse con ese destino de catálogo web.

### Empresa y contacto

| Página | Orden de bloques | Medios previstos en el wireframe |
| --- | --- | --- |
| L’azienda W 2 | Il Consorzio Vivai Pontini; vídeo; presentación; cifras; La famiglia Di Girolamo en bloque alterno; galería; texto adicional; CTA de contacto. | Un vídeo, retrato familiar, una foto horizontal y tres verticales de galería. |
| Tecnologie W 3 | Introducción; seis bloques alternos de texto y medio; CTA de contacto. | Cuatro fotos y dos vídeos. |
| ECO W 4 | Introducción; certificaciones/sostenibilidad; reutilización de agua; energía; reducción de pesticidas; CTA de contacto. | Cuatro fotos y un vídeo. |
| Il team W 5 | Il team Vivai Pontini; foto de grupo; introducción; Gestione e vendite; CTA de contacto. | Foto de grupo y ocho tarjetas de ejemplo en dos columnas. |
| Contatti W 6 | Contacto directo; mapa; dirección; Scrivici; formulario. | Mapa esquemático. No añade CTA de contacto ni certificaciones. |

Tecnologie contiene, en este orden: Serre automatizzate con controllo della temperatura e dell’umidità; Irrigazione con sistema a flusso e riflusso; Bancali di coltivazione robotizzati; Celle frigorifere per il controllo del ciclo produttivo; Gestione delle scorte e delle spedizioni tramite tecnologia RFID; Ricerca e sviluppo di nuove tecniche colturali. Los bloques alternan foto o vídeo a izquierda y derecha, con algunas superficies grises de agrupación.

ECO desarrolla Certificazioni di qualità e sostenibilità, con nombres todavía por indicar; Riutilizzo dell’acqua di irrigazione, con vídeo; Energia da fonti non inquinanti, con dos imágenes; y Riduzione progressiva dell’impiego di pesticidi.

Cada tarjeta de equipo muestra retrato, Nome e cognome, Posizione in azienda, Telefono y Email. Las ocho posiciones son una maqueta, no ocho personas confirmadas.

En Contatti aparecen teléfono, WhatsApp y correo; el mismo número 0773 852003 figura para teléfono y WhatsApp. Hay que confirmar su uso. El mapa es una imagen esquemática y no define proveedor ni integración.

El formulario dispone de **Nome, Email y Oggetto** a izquierda, **Messaggio** a derecha, texto **Informativa Privacy** y botón **Inviare** debajo. No especifica campos obligatorios, casilla de privacidad, destinatario, transporte de correo ni estados de éxito y error. Estos aspectos se concretarán para su funcionamiento real.

### Portada de productos

W 7 ordena: hero «Produzione di piante ornamentali» con Disponibilità settimanale; introducción; Featured con tres tarjetas; Speciale con tres tarjetas de ejemplo; banda Piante verdi; banda Piante da fiore; CTA de disponibilidad y descarga; certificaciones; pie.

Featured muestra Photos, Ortensia (Hydrangea) y Anthurium. Speciale muestra Dipladenia (Mandevilla), Monstera y Phalaenopsis. Las fotos de esta página son verticales, mientras las tres Featured de H son horizontales; los recortes deben adaptarse al contexto.

### Plantilla de ficha

W 8 y 9 comparten estructura: lateral; nombre comercial y botánico; tres cifras; imagen principal horizontal; disponibilidad mensual; descripción; seis fotos verticales en tres columnas y dos filas; disponibilidad semanal y catálogo PDF; certificaciones; pie.

| Ejemplo | Nombre botánico literal | Cifras dibujadas |
| --- | --- | --- |
| Ortensia W 8 | Hydrangea macrophyla | 1.500 m² de superficie, 300.000 plantas anuales, 12 formatos. |
| Dipladenia W 9 | Mandevilla | 800 m², 150.000 plantas anuales, 21 formatos. |

Son datos de ejemplo por validar; «Hydrangea macrophyla» requiere revisión de nomenclatura. Los doce segmentos del calendario no tienen rótulos y sus rellenos no se tomarán como disponibilidad real. La reunión añade la necesidad de identificar claramente los meses; el aspecto definitivo sigue abierto.

La galería dentro de una ficha está representada como imágenes, pero no define un estado de ampliación específico. Reutilizar el lightbox también aquí sería una mejora propuesta que se puede decidir al implementar la plantilla.

### Galerías de plantas verdes y de flor

W 10 contiene lateral, título, tres cifras, introducción, nueve tarjetas verticales en tres columnas, CTA de disponibilidad y catálogo, certificaciones y pie. Cada tarjeta tiene un pie negro con nombre blanco.

Los nombres son Beaucarnea, Ficus, Dracaena, Sansevieria, Sphatiphyllum, Strelitzia y tres repeticiones de Beaucarnea, Ficus y Dracaena. No equivalen a nueve especies distintas. La formulación Piante verde/Piante verdi y el nombre Sphatiphyllum se dejan para revisión editorial. Las cifras 1.100 m², 270.000 plantas anuales y 43 formatos son muestras.

W 11 representa el lightbox de Beaucarnea: fondo atenuado, foto vertical, nombre, flechas anterior/siguiente y cierre X. Solo la primera tarjeta enlaza a ese estado en el PDF. La reunión confirma foto ampliada para todas las plantas verdes y de flor. La X y las flechas están dibujadas sin enlaces PDF; necesitan interacción real en la web.

Piante da fiore reutilizaría esta familia de estructura y comportamiento con su propio contenido. La repetición de diseño es propuesta; la existencia de la categoría y su lightbox está confirmada.

### Servicios profesionales

Las tres páginas comparten hero con disponibilidad semanal, introducción, bloque de especialidad, seis tarjetas horizontales de planta, testimonio, CTA de disponibilidad y catálogo, certificaciones y pie.

| Página | Hero | Bloque específico |
| --- | --- | --- |
| Vivai produttori W 12 | Piante semilavorate per vivai produttori. | Specialisti in ortensie prefinite; texto y vídeo. Gamma di specie semilavorate. |
| Garden center W 13 | Piante finite per garden center. | Capolavoro! Il brand per il consumatore; texto, vídeo y Scoprire piu. Gamma di piante per garden center. |
| Grossisti W 14 | Fornitura di piante per grossisti. | Il miglior servizio logistico; texto y mapa de Europa. Gamma di piante per grossisti. |

Las seis plantas de cada maqueta repiten Photos, Ortensia y Anthurium; no son listas definitivas ni acreditan seis contenidos diferentes. En W 12–14, las tres tarjetas superiores enlazan a W 8 y las tres inferiores carecen de anotación. Se propone enlazar las que pertenezcan a Featured/Speciale a su ficha propia; cualquier otra tarjeta necesita definir su destino sin crear fichas por inferencia.

Testimonianze muestra retrato, autor, puesto, texto y una flecha. Será contenido fijo editable si se incluye. La decisión de presencia y el número de testimonios siguen abiertos. La flecha sugiere navegación entre varios, no una conexión a Google.

El mapa de Europa es un recurso ilustrativo de logística. Sus colores no acreditan cobertura comercial real por país. El CTA Scoprire piu de Garden center no tiene enlace en esa posición; llevarlo a Capolavoro! es una propuesta coherente por confirmar.

### Capolavoro

W 15 ordena: hero de marca con claim y «Il marchio di Vivai Pontini pensato per conquistare il consumatore»; botón Scoprire piu con icono play; introducción; tres fotos horizontales; Etichettatura e cartellonistica per il punto vendita; bloque de etiquetado con foto a izquierda; bloque de cartelería con foto a derecha; Gamma di piante Capolavoro! con seis tarjetas; CTA de contacto; pie.

El hero sugiere vídeo por su icono, pero el comportamiento de ese botón no está definido. La página no muestra certificaciones al pie. Las seis tarjetas repiten ejemplos de planta: las tres superiores enlazan a W 8 y las inferiores no tienen anotación. Su lista y destinos requieren la misma validación que las gamas de servicios.

## Flujos de interacción

| Inicio | Acción | Resultado previsto |
| --- | --- | --- |
| Home o Prodotti | Pulsar planta Featured/Speciale. | Ficha de esa especie, no la ficha ejemplo repetida del PDF. |
| Categoría verde/flor | Pulsar una foto. | Lightbox con foto grande y nombre, manteniendo la categoría debajo. |
| Lightbox | Cerrar; anterior/siguiente. | Volver a galería; recorrer sus imágenes. Escape y devolución de foco son criterios recomendados. |
| Menú Chi siamo | Abrir sección o elegir subpágina. | L’azienda como entrada; desplazamiento entre páginas con menú y lateral. |
| Menú Servizi | Abrir sección o elegir público. | Vivai como entrada PDF; acceso a las tres páginas del desplegable. |
| Home | Pulsar CTA de catálogo. | W lleva a portada Prodotti. Confirmar que el texto de H conserva esa intención. |
| Página con Download catalogo | Pulsar descarga. | PDF real asignado al botón y al idioma. |
| Disponibilità settimanale | Pulsar CTA. | Destino externo entregado por el cliente; no usa el calendario mensual de la ficha. |
| Area riservata | Pulsar CTA B2B. | Aplicación externa. |
| Vídeo | Activar control. | Reproducción según fuente y presentación pendientes; H no define modal ni reproducción automática. |
| Contacto | Completar y enviar. | Validación y resultado reales cuando exista backend; en maqueta, interacción identificada como demostración. |
| Idiomas | Cambiar IT/EN. | Página equivalente cuando esté traducida, según estructura propuesta. |

## Enlaces del prototipo y destinos pendientes

El [grafo de navegación](../investigacion/wireframe/link-graph.json) recoge **524 anotaciones**, todas GoTo internas. No hay URI externa en el PDF. Los destinos están almacenados como índices desde cero; el inventario los convierte a páginas desde uno. Se han contrastado contra las 15 páginas existentes.

Los enlaces permiten recorrer las secciones y los ejemplos de ficha. No definen por sí solos URL de área B2B, disponibilidad semanal, catálogos, vídeos, redes, newsletter, teléfono, correo o documentos legales. Tampoco resuelven los estados de móvil, menús abiertos, envío de formulario o cierre de lightbox.

Los [recursos incrustados](../investigacion/wireframe/embedded-images.json) incluyen Capolavoro!, certificaciones, AssoFloro, el mapa esquemático de contacto y el mapa de Europa. Son recursos recuperados del documento para referencia y maqueta; su presencia no confirma una integración externa.
