# Fases y entregas para desarrollar la web de Vivai Pontini

**Estado final local:** las fases de maqueta ya están implementadas y verificadas en 19 páginas. Consultar [cobertura final](05-wireframe-completo.md) y el README para el estado vigente. La planificación que sigue se conserva como referencia inicial; las siguientes etapas son revisión editorial e integración en staging.

Actualización del 19 de noviembre de 2026: el usuario ha elegido integrar WordPress directamente en el servidor de pruebas de Hostinger, manteniendo el diseño en local. El [entorno de pruebas](../staging/estado-servidor.md) ya tiene idiomas, páginas base y menús preparados. En la fase 7, el entorno de integración será staging en lugar de WordPress local.

Se propone avanzar por familias de páginas, validando primero la home y los componentes comunes. El contenido provisional permite resolver estructura e interacción mientras llegan textos, fotografías y originales de marca. La conversión a WordPress reutilizará esas decisiones y su modelo de contenido.

## Fases propuestas originalmente

| Fase | Trabajo | Resultado y criterio de cierre |
| --- | --- | --- |
| 0 Investigación | Revisar las fuentes, inventariar pantallas y enlaces, documentar identidad, requisitos y pendientes. | Dossier y evidencia local reunidos en esta carpeta. Investigación completada; las decisiones abiertas quedan registradas. |
| 1 Base local y home | Preparar HTML, CSS y JavaScript, estilos de marca, header/footer, menús y home italiana siguiendo H. Usar contenido provisional de proporciones realistas. | Home navegable en escritorio y móvil, con revisión visual de tipografía, espaciado, colores, imágenes y CTA. |
| 2 Contacto | Construir Contatti, lateral de empresa, mapa provisional y formulario visual. | Campos, validación de interfaz y navegación comprobados. El envío real se incorporará al preparar el backend. |
| 3 Empresa | L’azienda, Tecnologie adottate, ECO investimenti e Il team. | Alternancia de bloques, vídeos, galería y equipo; navegación lateral completa. |
| 4 Productos | Portada, Featured/Speciale como secciones, plantilla de ficha, disponibilidad mensual y galerías verde/flor. | Cada tipo de tarjeta abre el destino adecuado; lightbox operativo y datos de ejemplo separados de la presentación. |
| 5 Servicios y Capolavoro | Tres páginas de servicio, bloques de vídeo/logística, catálogo y página Capolavoro!. Preparar testimonios como bloque opcional. | Flujos italianos completos; destinos y piezas pendientes identificados para revisión. |
| 6 Validación italiana | Cargar textos revisados, medios, cifras, plantas y banners finales; revisar responsive y decidir ocultaciones. | Estructura italiana validada y revisión lingüística del especialista incorporada. |
| 7 WordPress editable | Convertir la maqueta a plantillas y bloques/campos del editor elegido, en entorno local. Preparar menús, medios, fichas y ajustes globales. | Una persona editora puede cambiar textos, imágenes, meses, productos y enlaces sin tocar código. |
| 8 Inglés e integraciones | Incorporar EN y sus equivalencias; completar formulario, descargas, redes, newsletter y destinos externos según entregas. | Versiones IT/EN y funcionalidades completas, revisadas en el entorno acordado. |
| 9 Producción | Preparar respaldo, migración, dominio, configuración y comprobación final cuando se llegue a esta etapa. | Web publicada y verificada con contenido y WordPress aprobados. |

El orden de contacto y empresa responde a la propuesta del usuario. Si WordPress se inicia después de validar las plantillas, la carga final de contenido puede hacerse directamente allí para evitar duplicarla; la estructura italiana seguirá validándose antes de traducirla. No se asignan plazos hasta concretar entregas y volumen de contenido.

## Preparación técnica recomendada

Para la maqueta basta una base local de HTML semántico, CSS con variables y JavaScript modular. Separar datos de plantas, navegación y textos del código de presentación facilitará la conversión. No es necesario decidir ahora un framework, constructor o plugin.

Las familias reutilizables serán cabecera y desplegables, pie, laterales, hero, cifras, bloque alterno de texto y medio, tarjeta de planta, galería, lightbox, meses disponibles, CTA, certificaciones y testimonio opcional. Una plantilla de ficha común cubre Featured y Speciale, variando contenido y estado activo del menú.

La propuesta de rutas usa raíz italiana y /en/ para inglés. Cada contenido debe conservar un identificador estable y su equivalencia de idioma. Los slugs y la solución multilingüe se cerrarán antes de configurar WordPress.

## Modelo de contenido propuesto para WordPress

Es una propuesta de implementación, no una elección de editor o plugin.

| Contenido | Campos editables previstos | Regla |
| --- | --- | --- |
| Ajustes globales | Logos, contacto, dirección, redes, área B2B, disponibilidad semanal, catálogos y navegación. | Reutilizar los mismos valores en todas las plantillas. |
| Página | Título, introducción, bloques, fotografías, vídeos y CTA; relación con versión inglesa. | Ofrecer composiciones coherentes con el diseño. |
| Ficha de planta | Identificador, nombre comercial y botánico, categoría editorial, imagen principal, descripción, superficie, producción anual, formatos, meses, galería, orden y CTA. | Solo publicar detalle cuando exista contenido de ficha. La categoría nueva con detalle necesita ese contenido. |
| Entrada de galería | Nombre, imagen, texto alternativo, categoría verde/flor y orden. | Abrir lightbox; no generar fichas vacías para cada imagen. |
| Equipo | Nombre, puesto, retrato, teléfono, email y orden. | Las ocho tarjetas del PDF son posiciones de muestra, no una lista final. |
| Testimonio | Texto, autor, puesto, imagen y orden. | Editable y activable si el cliente confirma inclusión. |
| Certificación o asociación | Nombre, logo y posible enlace. | Reutilizar el bloque según las páginas que lo muestran. |

Guardar los meses como números del 1 al 12 permite traducir sus etiquetas sin cambiar el dato. Las cifras corporativas y las de cada planta necesitan unidades explícitas. La previsión de unas doce fichas dimensiona el trabajo editorial; no se propone convertirla en una restricción rígida del CMS.

## Entregas y decisiones pendientes

| Prioridad y momento | Pendiente | Responsable orientativo | Qué permite avanzar |
| --- | --- | --- | --- |
| Inicio de home | Logos oficiales y variantes; fuentes web y condiciones de uso. | Diseño / cliente. | Fidelidad de identidad. Se puede estructurar con recursos provisionales identificados. |
| Inicio de home | Contrastar negro de H frente a Nero del manual y aprobar composición de home. | Diseño / usuario. | Consolidar estilos comunes. |
| Primera revisión | Concretar medidas de banners especiales y su versión móvil. | Rafa y diseño. | Entrega de arte final de Capolavoro!; medidas propuestas en el documento de marca. |
| Productos | Confirmar Featured, nombre Photos/Pothos, lista y número de Speciale. | Francesca / cliente. | Inventario final de fichas. La plantilla puede adelantarse. |
| Productos | Datos, nombres botánicos, imágenes y meses por especie. | Cliente / especialista. | Contenido real de fichas y galerías. |
| Productos | Aprobar reutilización de Piante verdi para Piante da fiore; elegir presentación de meses. | Diseño / cliente / desarrollo. | Completar pantalla ausente y acabado del componente. |
| Contenido italiano | Textos validados asignados a cada bloque; cifras definitivas y unidades. | Francesca / cliente / especialista. | Revisión editorial completa. |
| Medios | Fotos, vídeos, iconos, certificados, mapa logístico y piezas Capolavoro! con ubicación. | Diseño / cliente. | Sustituir marcadores y preparar recortes y formatos finales. |
| Equipo y testimonios | Personas reales; decisión de testimonios y sus datos si se incluyen. | Francesca / cliente. | Carga de esos módulos. |
| Contacto | Confirmar teléfono WhatsApp, destinatario de formulario, obligatorios y mensajes. | Cliente / desarrollo. | Función de contacto real. El mismo número de teléfono aparece en ambos usos en W. |
| Destinos | URL de área B2B, disponibilidad semanal, redes, vídeos y newsletter; archivos PDF por idioma. | Cliente / Francesca. | Completar los enlaces. Ningún PDF entrega esas URL externas. |
| Enlaces de catálogo | Confirmar si «Scopri il catalogo» de H mantiene el destino a portada Prodotti que tiene W. | Diseño / cliente. | Evitar confundir navegación a catálogo web con descarga PDF. |
| Pie y contacto | Textos y destinos de privacidad, cookies y preferencias; definir newsletter y mapa. | Cliente / desarrollo. | Implementar los controles que H añade al pie y W muestra parcialmente. |
| Responsive | Decidir ocultaciones tras ver la maqueta. | Diseño / cliente. | Cierre de móvil; no hay lista previa de bloques ocultos. |
| WordPress | Elegir editor, alcance de edición y solución de idiomas. | Usuario / desarrollo. | Conversión a CMS. Elementor y WPML no están fijados por las fuentes. |
| Inglés | Entrega traducida o método asistido con revisión y responsable de aprobación. | Francesca / cliente. | Versión inglesa después de validar IT. |
| Producción | Accesos, dominio, instalación existente y condiciones de migración. | Cliente / usuario. | Preparar publicación cuando corresponda. |

## Criterios recomendados para revisar la maqueta

- **Home:** orden y jerarquía de H, identidad coherente con B, contraste y legibilidad de textos y controles, y CTA con destino definido o pendiente visible durante la revisión.
- **Navegación:** desplegables con ratón, teclado y toque; activo claro; acceso lateral completo en empresa y productos; logo con retorno a home.
- **Productos:** ficha propia para cada Featured/Speciale; ampliación para cada verde/flor. Cierre visible, Escape, anterior/siguiente y retorno de foco en lightbox.
- **Meses:** doce posiciones legibles, disponibles y no disponibles distinguibles sin depender solo del color. Propuesta inicial: gen, feb, mar, apr, mag, giu, lug, ago, set, ott, nov, dic; etiquetas finales revisadas.
- **Responsive:** revisar al menos móvil estrecho, tableta y escritorio; sin desbordamiento horizontal, con laterales adaptados y controles utilizables. Las anchuras concretas se eligen al implementar.
- **Contenido:** identificar Lorem Ipsum, cifras de muestra y medios pendientes en el registro de revisión. Los meses dibujados en W no se toman como datos reales.
- **Contacto:** etiquetas de campo claras y estados de error; el prototipo local no debe confirmar un envío real sin backend. Completar destinatario y probar la entrega en la fase funcional.
- **Idiomas:** italiano por defecto; cambio a equivalente inglés cuando esté disponible; botones, formularios y meses también traducidos.
- **WordPress:** comprobar edición real de una página, ficha, galería, mes y enlace global sin alterar el diseño.

## Primer bloque de trabajo preparado

La siguiente fase puede construir la home y su estructura común con H como referencia visual, el oro exacto del manual y nombres de menú italianos. Debe incluir estados de desplegable y móvil, reservar el vídeo corporativo y el banner Capolavoro!, y registrar las sustituciones temporales de fuentes y medios.

Al cerrar ese bloque se revisarán la escala tipográfica, el ancho de contenido y las medidas definitivas de las piezas especiales. Así las siguientes páginas reutilizarán una base visual ya contrastada.
