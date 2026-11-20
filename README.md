# Vivai Pontini · wireframe local completo

Maqueta navegable en italiano: **19 páginas**, siguiendo las 15 pantallas del wireframe, el diseño de home y el manual de marca. Responsive, menús desplegables, laterales sticky en escritorio, fichas con calendario mensual y galerías con lightbox. Los iconos y las tarjetas se apilan en una columna en móvil.

[Abrir la web local](http://127.0.0.1:4173/) · [Inventario completo y pendientes](docs/05-wireframe-completo.md)

## Arrancar

Desde esta carpeta: `npm run dev` o `python3 -m http.server 4173 --bind 127.0.0.1`. Abrir http://127.0.0.1:4173/. No requiere instalación ni compilación para usar la web. El servidor solo escucha en este equipo.

HTML estático, `styles.css` y `app.js` compartidos; imágenes y fuentes en `assets/`, inventarios de referencia en `data/`. `scripts/complete-wireframe.py` genera las dos categorías de galería, las tres páginas de servicios y Capolavoro, y normaliza los enlaces comunes. Si se modifican esas seis páginas manualmente, actualizar también el generador antes de ejecutarlo de nuevo.

## Estado verificado

Se han contrastado las páginas con los bloques del PDF y revisado capturas de escritorio y móvil. La comprobación automatizada cubre 19 páginas a 320, 390, 600, 768, 801, 1024 y 1440 px: **133 layouts y 640 enlaces internos**. Revisa recursos, desbordamientos, bloques esperados, laterales, desplegables, galerías, meses, testimonios y validación del formulario. Informe y capturas en [investigacion/qa/completo](investigacion/qa/completo/).

`npm run check` valida la sintaxis de JavaScript. `npm run qa` ejecuta `tests/check-wireframe.cjs`: necesita Playwright y Chromium disponibles en Node y el servidor local arrancado. En esta sesión se ha utilizado el runtime de Node/Playwright de Codex mediante `NODE_PATH`. El origen se puede cambiar con `PONTINI_PREVIEW`.

## Contenido provisional e integración

Lorem Ipsum, imágenes de referencia y huecos identificados donde falta material. Los meses son demostrativos; cifras, nombres botánicos y variedad definitiva requieren validación. Se han implementado las seis especies identificadas en los materiales: no se han inventado más fichas para alcanzar una estimación de catálogo. Piante da fiore reutiliza la estructura de Piante verdi porque no tiene pantalla propia en el PDF.

Outfit se sirve localmente con licencia OFL. Georgia sustituye provisionalmente a Acta Display Bold. Logotipos, mármol y arte Capolavoro proceden de los materiales suministrados. Los vídeos, descargas y servicios externos sin destino muestran un aviso. El formulario valida en el navegador y **no envía ni guarda mensajes**. Testimonios y personas son muestras, sin atribuciones inventadas.

La siguiente etapa es revisar diseño y textos italianos, sustituir contenido provisional e integrar el diseño en WordPress de pruebas. Inglés después de validar italiano. Esta entrega no publica ni carga páginas en staging. El entorno previamente preparado se documenta en [staging/estado-servidor.md](staging/estado-servidor.md).

## Desplegar en Vercel

Importar el repositorio `PabloM19/pontini` desde GitHub, con la raíz del repositorio como Root Directory. `vercel.json` fija Framework Preset `Other`, Build Command `npm run build` y Output Directory `dist`. No necesita variables de entorno ni dependencias de producción. Cada push a la rama de producción configurada en Vercel podrá generar un nuevo despliegue al conectar el repositorio.

El build copia las 19 páginas, CSS, JavaScript y `assets/`; los PDF originales, la investigación y la documentación quedan fuera de la web publicada. Se conservan las rutas `.html` existentes. El formulario y los enlaces pendientes mantienen su comportamiento de demostración. Comprobar localmente con `npm run build` y `python3 -m http.server 4174 --bind 127.0.0.1 --directory dist`.

## Fuentes y documentación de referencia

- [Requisitos y alcance](docs/01-requisitos-y-alcance.md).
- [Mapa y flujos de referencia](docs/02-mapa-y-flujos.md).
- [Marca y recursos](docs/03-marca-y-recursos.md).
- [Plan inicial y pendientes de contenido](docs/04-fases-y-pendientes.md).
- [Cobertura final del wireframe](docs/05-wireframe-completo.md).

Fuentes originales: `wireframe-Pontini.pdf`, `Diseño_web_Pontini_version_escritorio.pdf`, `FESAEECT0001_Brand_Book_Pontini_WEB.pdf` y transcripción de la reunión. Extracciones, inventario de enlaces y referencias visuales en `investigacion/`.
