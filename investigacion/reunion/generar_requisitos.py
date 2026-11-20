from pathlib import Path
import json

base = Path(__file__).parent
source = Path('/Users/bleras/.codex/attachments/f35fb024-bd6d-407c-82e8-eb1717152a70/Texto pegado.txt')
lines = source.read_text().splitlines()

def ref(start, end=None):
    end = end or start
    return {'fuente': 'transcripcion', 'archivo': str(source), 'lineas': [start, end], 'extracto': '\n'.join(lines[start-1:end])}

def user(part):
    return {'fuente': 'solicitud_usuario', 'apartado': part}

requirements = [
 {'id':'R01','tema':'Alcance actual','estado':'confirmado_usuario','requisito':'Investigar y reunir toda la documentación para preparar el desarrollo. La implementación del primer borrador local vendrá después de este análisis.','fuentes':[user('De momento lo que quiero es que reúnas toda la información')],'implicacion':'Entregar inventario, estructura, flujos, reglas visuales, pendientes y fases; no publicar ni desplegar.'},
 {'id':'R02','tema':'Ruta de entrega','estado':'confirmado_usuario','requisito':'Desarrollar primero en local con HTML/CSS/JavaScript u otra solución local apropiada, después convertir a WordPress editable y finalmente producción.','fuentes':[user('Desarrollarlo primero en local, luego pasarlo a WordPress para que sea editable y luego ya subirlo a producción')],'implicacion':'Preparar componentes y contenidos reutilizables para WordPress; aún no hay constructor o stack aprobado.'},
 {'id':'R03','tema':'Publicación','estado':'confirmado_usuario','requisito':'Trabajo completamente local en esta etapa, sin publicar en GPT Sites ni otro destino.','fuentes':[user('Sin publicar en GPT Sites ni nada de eso, en local completamente')],'implicacion':'La autorización actual no incluye despliegue público.'},
 {'id':'R04','tema':'Fidelidad visual','estado':'confirmado','requisito':'Seguir la estética del brand book y la home diseñada; el wireframe completo rige la estructura de las demás páginas.','fuentes':[ref(36,38),ref(50,52),user('Con el mismo estilo ... cómo quieren que sea la página de home, todo tal cual')],'implicacion':'La maqueta local es una estructura con identidad real, no solo cajas grises genéricas.'},
 {'id':'R05','tema':'Contenido provisional','estado':'confirmado','requisito':'Se puede avanzar con bloques y estructura sin textos definitivos; el usuario permite Lorem Ipsum.','fuentes':[ref(50,52),user('Se puede rellenar todo con Lorem Ipsum')],'implicacion':'Mantener etiquetas de navegación funcionales en italiano y contenido editorial de prueba sustituible.'},
 {'id':'R06','tema':'Idiomas','estado':'confirmado_usuario_y_contexto','requisito':'Italiano principal e inglés secundario; sin versión española.','fuentes':[user('El idioma principal debe ser el italiano'),ref(138,145)],'implicacion':'Resolver el desliz español principal de la línea 143 en favor de la instrucción explícita del usuario.'},
 {'id':'R07','tema':'Secuencia de idiomas','estado':'confirmado','requisito':'Validar el wireframe completo en italiano primero y traducir después.','fuentes':[ref(144,145)],'implicacion':'Preparar estructura bilingüe desde el inicio, sin asumir que el contenido inglés ya está aprobado.'},
 {'id':'R08','tema':'Revisión lingüística','estado':'confirmado_usuario','requisito':'Los textos y revisiones en italiano serán supervisados por un especialista.','fuentes':[user('Todas las revisiones de la web van a estar supervisadas por un especialista en italiano')],'implicacion':'Etiquetar contenido italiano provisional y reservar validación editorial antes de producción.'},
 {'id':'R09','tema':'Categorías de producto','estado':'confirmado','requisito':'Existen cuatro categorías: Destacados, Colección Especial, Planta Verde y Planta de Flor. Los rótulos finales italianos deben tomarse del PDF.','fuentes':[ref(66),ref(157)],'implicacion':'No convertir el desliz tres categorías de las notas o tres primeros de la transcripción en una regla.'},
 {'id':'R10','tema':'Fichas de producto','estado':'confirmado','requisito':'Destacados y Colección Especial tienen fichas completas por planta.','fuentes':[ref(78,88),ref(100)],'implicacion':'Una plantilla de ficha reutilizable con registros editoriales para las plantas de esas dos categorías.'},
 {'id':'R11','tema':'Galerías de plantas','estado':'confirmado','requisito':'Planta Verde y Planta de Flor tienen una página de categoría con texto introductorio y galería; cada foto abre imagen grande en lightbox, sin ficha de especie.','fuentes':[ref(72,78)],'implicacion':'No crear fichas vacías o páginas de detalle para cada imagen de estas galerías.'},
 {'id':'R12','tema':'Destacados','estado':'confirmado_con_lista_pendiente','requisito':'En principio son tres plantas fijas. Hortensia y anturios se nombran claramente; la tercera debe confirmarse con el material visual/listado final.','fuentes':[ref(86,92)],'implicacion':'Pothos aparece en conversación; no fijarlo por esa frase aislada.'},
 {'id':'R13','tema':'Volumen de fichas','estado':'estimacion_reunion','requisito':'Se estima un máximo aproximado de doce fichas entre ambas categorías, probablemente menos. Colección Especial se estima en seis o siete, sin número cerrado.','fuentes':[ref(86,92)],'implicacion':'Es una estimación de alcance, no doce fichas confirmadas ni un límite técnico rígido de la web.'},
 {'id':'R14','tema':'Selección de productos','estado':'confirmado','requisito':'La selección responde a productos importantes de la empresa y no a rotación estacional o de Navidad.','fuentes':[ref(93,100)],'implicacion':'No programar cambios automáticos por temporada.'},
 {'id':'R15','tema':'Altas de fichas','estado':'confirmado','requisito':'Añadir una planta nueva a Destacados o Colección Especial requiere crear su ficha.','fuentes':[ref(81,100)],'implicacion':'No suponer una base oculta de cincuenta o sesenta plantas con fichas preexistentes.'},
 {'id':'R16','tema':'Disponibilidad mensual','estado':'confirmado_semantica','requisito':'La ficha representa los meses del año en los que está disponible esa planta.','fuentes':[ref(105,115)],'implicacion':'Separar este dato editorial de los enlaces a disponibilidad semanal; el ejemplo febrero-diciembre no es un calendario real de ninguna especie.'},
 {'id':'R17','tema':'Testimonios','estado':'confirmado_comportamiento_inclusion_pendiente','requisito':'Si se incluyen, los testimonios serán fijos y mantenidos editorialmente; pueden existir varios. Su inclusión sigue en discusión.','fuentes':[ref(53,56)],'implicacion':'No conectar reseñas a Google ni comprometer el bloque como obligatorio; la flecha indica posible navegación entre varios.'},
 {'id':'R18','tema':'Menús desplegables','estado':'confirmado','requisito':'Quiénes Somos, Productos y Servicio muestran sus opciones o categorías en desplegable. Productos muestra las cuatro categorías.','fuentes':[ref(147,159)],'implicacion':'La interacción exacta para táctil y teclado se define en implementación responsive.'},
 {'id':'R19','tema':'Navegación Quiénes Somos','estado':'confirmado','requisito':'La entrada de Quiénes Somos lleva a la página de la empresa, denominada hacienda en la conversación; sus subpáginas comparten un submenú lateral izquierdo.','fuentes':[ref(147,153)],'implicacion':'Verificar el rótulo italiano exacto (probablemente Azienda) y sus subpáginas en el wireframe; no crear un hub adicional sin necesidad.'},
 {'id':'R20','tema':'Responsive','estado':'confirmado','requisito':'La web debe adaptarse a móvil. Las ocultaciones de bloques se decidirán tras revisar responsive; no se han pedido textos distintos por dispositivo.','fuentes':[ref(122,128)],'implicacion':'Tomar el mismo contenido como base y anotar cualquier cambio aprobado más adelante.'},
 {'id':'R21','tema':'Área reservada','estado':'confirmado_destino_pendiente','requisito':'Área reservada enlaza a una aplicación externa del cliente.','fuentes':[ref(129,133)],'implicacion':'No construir autenticación, panel privado ni integración con su sistema en esta fase.'},
 {'id':'R22','tema':'Disponibilidad semanal','estado':'confirmado_destino_pendiente','requisito':'Los botones de disponibilidad semanal enlazan a un desarrollo externo.','fuentes':[ref(133,137)],'implicacion':'No desarrollar consulta de stock, scraping o sincronización de inventario.'},
 {'id':'R23','tema':'Catálogos','estado':'confirmado_archivos_pendientes','requisito':'Los catálogos se descargan como PDF.','fuentes':[ref(137)],'implicacion':'Recibir archivos y su asignación a los botones; no son páginas de catálogo a programar por inferencia.'},
 {'id':'R24','tema':'Diseños especiales','estado':'confirmado_entrega_pendiente','requisito':'El equipo aportará el diseño de bloques especiales como la etiqueta o banner Capolavoro en dorado. Rafa debe concretar el ancho requerido.','fuentes':[ref(116,121)],'implicacion':'Reservar el bloque y preparar una especificación de dimensiones tras medir el diseño; no convertir una medida provisional en requisito del cliente.'},
 {'id':'R25','tema':'Textos y multimedia','estado':'confirmado_entrega_pendiente','requisito':'El equipo enviará los textos juntos cuando se validen y después recopilará fotos y vídeos por ubicación.','fuentes':[ref(21),ref(35,38),ref(50,52)],'implicacion':'Francesca es el contacto de seguimiento y textos; no asumir que los recursos vistos dentro de PDFs son todos los originales listos para web.'},
 {'id':'R26','tema':'Entorno inicial','estado':'confirmado_reunion_actualizado_usuario','requisito':'La reunión propone empezar en servidores propios al no tener acceso al hosting del cliente; la solicitud actual concreta desarrollo completamente local.','fuentes':[ref(163),user('En local completamente')],'implicacion':'Seguir local ahora; acceso de hosting será dependencia de la fase de producción, no de la investigación.'},
 {'id':'R27','tema':'Organización','estado':'confirmado','requisito':'Francesca lleva seguimiento de la web y redacción; Rafa desarrolla. Eloy lleva aspectos comerciales.','fuentes':[ref(9),ref(21),ref(164)],'implicacion':'No asignar nombres reales a cada Speaker sin verificación; no es necesario para implementar.'}
]

pending = [
 {'id':'P01','asunto':'Lista final y número de plantas con ficha','detalle':'Confirmar las tres de Destacados y el listado exacto de Colección Especial; no tomar 6–7 o 12 como inventario definitivo.','responsable':'Equipo de cliente / Francesca','bloquea':'Carga final de productos; permite construir la plantilla con ejemplos.'},
 {'id':'P02','asunto':'Datos completos por ficha','detalle':'Textos, nombres, imágenes, variantes/características y meses reales de disponibilidad por especie según campos del wireframe.','responsable':'Equipo de cliente / especialista italiano','bloquea':'Contenido definitivo y validación de fichas.'},
 {'id':'P03','asunto':'Aspecto de disponibilidad mensual','detalle':'Etiqueta final e interacción. Iniciales y tooltip son una propuesta conversada, todavía no un diseño cerrado.','responsable':'Diseño / desarrollo / cliente','bloquea':'Acabado final del componente, no su estructura.'},
 {'id':'P04','asunto':'Testimonios','detalle':'Decidir inclusión, número y textos/autores si se incluyen.','responsable':'Cliente / Francesca','bloquea':'Activación final del bloque.'},
 {'id':'P05','asunto':'Textos italianos validados','detalle':'Entrega conjunta y asignación a páginas/bloques; especialista revisará el italiano.','responsable':'Francesca / especialista','bloquea':'Aprobación editorial; permite Lorem Ipsum en local.'},
 {'id':'P06','asunto':'Producción inglesa','detalle':'Elegir entrega de traducciones o traducción automática con revisión. La mención VML no confirma WPML ni otra herramienta.','responsable':'Cliente / Francesca / desarrollo','bloquea':'Carga y validación EN, no validación inicial IT.'},
 {'id':'P07','asunto':'Fotografía y vídeo','detalle':'Recibir originales finales y mapa de dónde se utiliza cada archivo, con recortes responsive.','responsable':'Equipo de diseño / cliente','bloquea':'Fidelidad y rendimiento finales; permite marcadores.'},
 {'id':'P08','asunto':'Banner y etiqueta Capolavoro','detalle':'Rafa facilita ancho útil y relación de aspecto; el equipo entrega piezas de diseño y posibles adaptaciones móviles.','responsable':'Desarrollo y diseño','bloquea':'Acabado del bloque especial.'},
 {'id':'P09','asunto':'Enlaces externos','detalle':'URL reales de área reservada y disponibilidad semanal; comprobar si existe una URL común o destinos por producto.','responsable':'Cliente','bloquea':'Validación de esos enlaces; permite identificarlos como pendientes en local.'},
 {'id':'P10','asunto':'Catálogos PDF','detalle':'Archivos definitivos, nombres por idioma y asignación a CTA.','responsable':'Cliente / diseño','bloquea':'Descargas reales.'},
 {'id':'P11','asunto':'Ajustes móviles','detalle':'Revisar primera versión responsive antes de decidir ocultaciones; no hay lista aprobada de bloques ocultos.','responsable':'Cliente / diseño','bloquea':'Validación responsive final.'},
 {'id':'P12','asunto':'Editor WordPress','detalle':'Elegir tema, bloques y campos editables. Elementor aparece como ejemplo y no constituye una exigencia aprobada.','responsable':'Desarrollo / usuario','bloquea':'Conversión a WordPress; no la investigación ni el prototipo local.'},
 {'id':'P13','asunto':'Contacto y contenido legal','detalle':'Si el wireframe incluye formulario: confirmar campos, destinatario y comportamiento. Datos societarios, textos legales y consentimiento se revisarán con el contenido final. No aparecen requisitos concretos de backend en la reunión.','responsable':'Cliente / desarrollo','bloquea':'Funcionamiento real del formulario y publicación; no la maquetación.'},
 {'id':'P14','asunto':'Producción','detalle':'Accesos de hosting, dominio, instalación existente, copia y migración se concretan al llegar a la fase final.','responsable':'Cliente / usuario','bloquea':'Despliegue, no el trabajo local.'}
]

conflicts = [
 {'id':'C01','fragmento':'Tres categorías principales en notas; enumeración de cuatro.','resolucion':'Usar cuatro: confirmado explícitamente en l.66 y l.157.','certeza':'alta'},
 {'id':'C02','fragmento':'Los 3 primeros ... destacados y colecciones especiales (l.68).','resolucion':'Solo dos categorías con ficha, conforme aclaración l.78–100. No crear una tercera categoría con detalle.','certeza':'alta'},
 {'id':'C03','fragmento':'En español principal e inglés en secundario (l.143).','resolucion':'Italiano principal e inglés secundario: instrucción explícita actual del usuario y l.139–145.','certeza':'alta'},
 {'id':'C04','fragmento':'Esas fotos, hortensia y anturios (l.92); pothos se menciona en ejemplo de cambio (l.83).','resolucion':'Hortensia y anturios son identificaciones claras de la transcripción; tercera especie no queda confirmada solo por el audio transcrito. Verificar visualmente con el PDF y después con listado final. Ficus es un ejemplo hipotético.','certeza':'media'},
 {'id':'C05','fragmento':'Capolaboro / Topologo (l.116 y l.119).','resolucion':'Las notas del usuario lo normalizan a Capolavoro. Verificar texto exacto y grafismo en PDF o arte final.','certeza':'media'},
 {'id':'C06','fragmento':'Traductor de VML (l.143).','resolucion':'Podría aludir a una herramienta de traducción pero no acredita elección de plugin. No registrar WPML como requisito confirmado.','certeza':'alta_en_no_eleccion'},
 {'id':'C07','fragmento':'Hacienda y cuando compres un producto (l.151–155).','resolucion':'Se habla de navegación de empresa y menú de productos; no demuestra administración tributaria ni comercio electrónico. Nombre italiano exacto en wireframe.','certeza':'alta'},
 {'id':'C08','fragmento':'Entre hoy y mañana y reunión a las 12:30 (l.166).','resolucion':'Son referencias relativas de una reunión sin fecha establecida. No convertirlas en una fecha actual o compromiso nuevo.','certeza':'alta'},
 {'id':'C09','fragmento':'Proyectos inferiores a 2000 son pago único (l.164).','resolucion':'Es una condición comercial general; no establece precio exacto, alcance extra ni fecha de pago de este proyecto.','certeza':'alta'}
]

recommendations = [
 {'id':'A01','tema':'Navegación','criterio_recomendado':'Todos los enlaces del mapa de páginas llevan al destino previsto; menús operables con ratón, teclado y móvil; el lateral mantiene acceso a todas las subpáginas de empresa.','no_confirmado_en_reunion':'Detalles de accesibilidad y gesto táctil.'},
 {'id':'A02','tema':'Galerías','criterio_recomendado':'Las imágenes de Planta Verde/Flor abren lightbox, con cierre visible, tecla Escape y devolución de foco; no llevan a una ficha vacía.','no_confirmado_en_reunion':'Mecanismos de teclado y gestión de foco son recomendación de implementación.'},
 {'id':'A03','tema':'Meses','criterio_recomendado':'Mostrar doce posiciones con etiquetas italianas claras y estado disponible distinguible además de color. Preferir abreviaturas de tres letras a iniciales ambiguas. Si se usa tooltip debe funcionar también con foco y toque.','no_confirmado_en_reunion':'La elección de abreviaturas de tres letras es propuesta técnica; iniciales y tooltip tampoco estaban cerrados.'},
 {'id':'A04','tema':'Contenido de prueba','criterio_recomendado':'Usar textos y medios provisionales con longitud y proporciones próximas a las previstas; mantenerlos identificados para no publicarlos por error.','no_confirmado_en_reunion':'Método de identificación de contenido provisional.'},
 {'id':'A05','tema':'Preparación WordPress','criterio_recomendado':'Separar datos y presentación, usar una plantilla de ficha común y un esquema explícito de meses, colecciones, galerías, CTA y traducciones; definir en la fase WordPress quién edita cada bloque.','no_confirmado_en_reunion':'Modelo concreto de datos, plugin de campos y editor.'},
 {'id':'A06','tema':'Validación visual','criterio_recomendado':'Aprobar primero home en escritorio y móvil, después familias de plantillas y páginas; cotejar el orden y jerarquía de los bloques con el wireframe y tokens con el brand book.','no_confirmado_en_reunion':'Orden exacto de validación entre familias.'},
 {'id':'A07','tema':'Idiomas','criterio_recomendado':'Raíz en italiano y ruta /en/ para inglés; el selector conserva la página equivalente cuando exista traducción.','no_confirmado_en_reunion':'La estructura de URL es propuesta y se deberá confirmar al elegir solución WordPress.'},
 {'id':'A08','tema':'Prototipo local','criterio_recomendado':'Formulario y enlaces externos incompletos se identifican con estado pendiente; no fingir un envío ni inventar URL reales.','no_confirmado_en_reunion':'Presentación concreta del estado pendiente.'}
]

phases = [
 {'fase':0,'nombre':'Investigación y cierre del alcance','objetivo':'Inventario de fuentes, sitemap, bloques, flujos, tokens visuales, matriz de contenido y decisiones pendientes.','salida':'Dossier local revisable.','dependencias':'Los tres PDF, notas y transcripción ya disponibles.','estado':'fase_actual'},
 {'fase':1,'nombre':'Base local y home en italiano','objetivo':'Preparar estructura local, estilos de marca, header/footer y home fiel al diseño con marcadores de contenido.','salida':'Home navegable en escritorio y móvil.','dependencias':'Revisión del dossier; logo/fuentes web originales o sustitución provisional explícita.','estado':'propuesta_futura'},
 {'fase':2,'nombre':'Páginas informativas y contacto','objetivo':'Implementar familia de empresa con lateral y subpáginas, servicios y contacto según sitemap real.','salida':'Navegación completa y bloques reutilizables.','dependencias':'Base común; el orden contacto/empresa puede ajustarse con el usuario.','estado':'propuesta_futura'},
 {'fase':3,'nombre':'Productos y comportamientos','objetivo':'Crear cuatro categorías, plantilla de ficha para dos categorías y galerías lightbox para dos; representar disponibilidad mensual y reservar CTA externos/descargas.','salida':'Flujos de producto completos con datos de ejemplo.','dependencias':'Campos del wireframe; listas finales solo para carga definitiva.','estado':'propuesta_futura'},
 {'fase':4,'nombre':'Contenido y validación en italiano','objetivo':'Sustituir marcadores por textos, fotografía, vídeo y bloques especiales; ajustar responsive y decidir testimonios.','salida':'Versión italiana revisada por especialista y aprobada visualmente.','dependencias':'Entregas P01–P11.','estado':'propuesta_futura'},
 {'fase':5,'nombre':'WordPress editable y segunda lengua','objetivo':'Convertir componentes y datos al editor elegido; cargar inglés con revisión y verificar equivalencias, formularios, descargas y enlaces.','salida':'Sitio editable validado en entorno local o staging acordado.','dependencias':'Elección de editor y traducción; italiano validado antes de traducir. La conversión puede adelantarse tras aprobar estructuras si el usuario lo decide.','estado':'propuesta_futura'},
 {'fase':6,'nombre':'Producción','objetivo':'Preparar respaldo y migración, publicar cuando corresponda y verificar páginas, formulario, idiomas y recursos en el dominio final.','salida':'Sitio publicado y comprobado.','dependencias':'Accesos y acuerdo de publicación; contenido final y WordPress validados.','estado':'fuera_de_autorizacion_actual_de_publicacion'}
]

data = {
 'titulo':'Requisitos de la reunión de Pontini para preparar el desarrollo web',
 'fecha_analisis':'2026-11-19',
 'fecha_reunion':'no consta; no inferir por las referencias hoy y mañana',
 'fuentes':{'transcripcion':str(source),'notas':'Mensaje del usuario, apartado notas vivai dudas','solicitud':'Mensaje del usuario en este chat'},
 'precedencia':'La instrucción explícita actual del usuario prevalece sobre deslices de la transcripción. Las aclaraciones posteriores de la reunión resuelven las primeras hipótesis. El PDF aporta rótulos y estructura exactos.',
 'requisitos':requirements,
 'pendientes':pending,
 'contradicciones_y_errores_de_interpretacion':conflicts,
 'criterios_de_aceptacion_recomendados':recommendations,
 'fases_propuestas':phases,
 'fuera_de_alcance_no_pedido':['Publicar ahora','Comercio electrónico, cesta, checkout o pagos web','Autenticación o panel privado propio para el área reservada','Sincronización de stock o disponibilidad semanal','Importar reseñas de Google','Rotación estacional automática de productos','Versión en español','Base oculta de fichas de todas las plantas','Elección obligatoria de Elementor o WPML','Diferentes textos editoriales por dispositivo'],
 'nota_comercial':'Se mencionó pago único para proyectos inferiores a 2.000 euros; no se dispone del precio de este proyecto, calendario de cobro ni contrato. No condiciona el análisis técnico.'
}

(base/'requisitos.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

out = [data['titulo'], 'Análisis: '+data['fecha_analisis'], '', 'REQUISITOS CONFIRMADOS Y ESTIMACIONES', '']
for r in requirements:
    out += [f"{r['id']} — {r['tema']} [{r['estado']}]", r['requisito'], 'Implicación: '+r['implicacion']]
    for s in r['fuentes']:
        if s['fuente']=='transcripcion': out += [f"Fuente: transcripción, líneas {s['lineas'][0]}–{s['lineas'][1]}."]
        else: out += ['Fuente: solicitud del usuario, '+s['apartado']+'.']
    out += ['']
out += ['PENDIENTES', '']
for p in pending:
    out += [f"{p['id']} — {p['asunto']}",p['detalle'],'Responsable: '+p['responsable']+'.','Impacto: '+p['bloquea'],'']
out += ['CONTRADICCIONES Y ERRORES DE INTERPRETACIÓN', '']
for c in conflicts: out += [c['id']+' — '+c['fragmento'], c['resolucion'], '']
out += ['CRITERIOS DE ACEPTACIÓN RECOMENDADOS, NO ACUERDOS DE REUNIÓN', '']
for a in recommendations: out += [a['id']+' — '+a['tema'], a['criterio_recomendado'],'Propuesta: '+a['no_confirmado_en_reunion'],'']
out += ['FASES PROPUESTAS, SIN FECHAS NI ESTIMACIÓN DE HORAS', '']
for p in phases: out += [str(p['fase'])+' — '+p['nombre'],p['objetivo'],'Salida: '+p['salida'],'Dependencias: '+p['dependencias'],'']
out += ['FUERA DEL ALCANCE ACTUAL O NO SOLICITADO', *data['fuera_de_alcance_no_pedido'], '',data['nota_comercial']]
(base/'requisitos.txt').write_text('\n'.join(out)+'\n')
print(json.dumps({'requisitos':len(requirements),'pendientes':len(pending),'contradicciones':len(conflicts),'criterios_recomendados':len(recommendations),'fases':len(phases)},ensure_ascii=False))
