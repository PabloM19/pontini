# Entorno de pruebas de Vivai Pontini

Preparado el 19 de noviembre de 2026 mediante el navegador integrado de Codex.

Administración: https://tan-gnat-680645.hostingersite.com/wp-admin/

## Flujo de desarrollo

El diseño se construye y revisa en local. La integración editable con WordPress se hará directamente en este servidor de pruebas. No se preparará un WordPress local. La home diseñada no se ha subido; solo existe una página Home vacía en borrador.

## Configuración realizada

- Polylang ya estaba instalado. Se añadió Italiano it_IT como idioma principal y se conservó English en_GB como secundario. Se retiraron los idiomas español y francés anteriores.
- WordPress usa Italiano como idioma del sitio, nombre Vivai Pontini, descripción Specialisti nella produzione di piante ornamentali, zona Europe/Rome, fecha d/m/Y y hora H:i. El idioma del usuario administrador permanece en español.
- La estructura de enlaces permanentes ya era /%postname%/. Polylang ya usaba directorios por idioma, ocultando el del idioma principal: italiano en raíz e inglés bajo /en/. La detección automática del idioma del navegador está desactivada.
- Se activó la opción de pedir a los motores de búsqueda que no indexen el sitio de pruebas.
- Se instaló el importador oficial de WordPress y se importó struttura-pontini.xml: 13 páginas vacías en borrador, todas asignadas al italiano, y cinco menús con 36 elementos en total. No se importaron adjuntos, diseños, fichas ni traducciones.
- Se activó Twenty Twenty-One como tema oficial provisional para administrar menús clásicos. El tema anterior, Twenty Twenty-Five, no permitía acceder a ese editor. El tema de Pontini se integrará después.

## Menús preparados

| Menú | Contenido | Ubicación |
| --- | --- | --- |
| Principale IT | Chi siamo con cinco subopciones; Capolavoro!; Prodotti con cuatro categorías; Servizi con tres públicos; Contatti; Area riservata B2B. | Menú principal Italiano. |
| Footer IT | Empresa, marca, productos, servicios, contacto y área reservada. | Menú secundario Italiano. |
| Azienda IT | L’azienda, Tecnologie adottate, ECO investimenti, Il team y Contatti. | Preparado para lateral del futuro tema. |
| Prodotti IT | Featured, Speciale, Piante verdi y Piante da fiore. | Preparado para lateral del futuro tema. |
| Servizi IT | Vivai produttori, Grossisti e distributori y Garden center. | Preparado para el futuro tema. |

Las ubicaciones inglesas quedan sin asignar mientras no haya traducciones. Featured y Speciale apuntan a anclas de la futura portada Prodotti. El área reservada conserva un ancla provisional hasta recibir su URL externa.

## Páginas vacías creadas

Home; L’azienda con Tecnologie adottate, ECO investimenti e Il team como hijas; Contatti; Prodotti con Piante verdi y Piante da fiore como hijas; Vivai produttori; Grossisti e distributori; Garden center; Capolavoro!.

La entrada L’azienda usa el slug chi-siamo, de modo que las subpáginas quedan bajo /chi-siamo/. Las páginas de servicios tienen slugs propios sin crear una portada Servizi adicional. Estos slugs concretan la propuesta inicial de rutas del dossier.

La lista de páginas confirmó 14 borradores: los 13 nuevos en italiano y Privacy Policy, un borrador previo que se conserva. No se creó una portada estática publicada ni se cargó contenido de la home local.

## Comprobación y próximos pasos

El importador mostró finalización correcta; la lista de páginas confirmó los 13 borradores italianos. El editor mostró la jerarquía de Principale IT y las cinco opciones de menú. La pantalla de ubicaciones confirmó Principale IT y Footer IT asignados al italiano.

La evidencia está en menus-wordpress.jpg. El XML y el JSON de esta carpeta describen la estructura importada; no deben reimportarse sin comprobar antes el estado actual.

Después de validar la home italiana: preparar el tema de Pontini, incorporar su diseño en staging, integrar los menús existentes y convertir los bloques en contenido editable. La Home se publicará y asignará como portada cuando se integre. El inglés, las URL externas, los catálogos y los textos definitivos siguen pendientes de su fase correspondiente. Los plugins preexistentes, incluido Catálogo Plantas, se revisarán al concretar el modelo editorial; no se ha cambiado su configuración.

Las credenciales no se guardan en los archivos del proyecto.
