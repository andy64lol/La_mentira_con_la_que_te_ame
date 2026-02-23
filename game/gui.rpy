################################################################################
## Inicialización
################################################################################

## La sentencia 'init offset' da preferencia a las sentencias de inicialización
## de este archivo respecto a otros archivos.
init offset = -2

## Llamando 'gui.init' se resetean los estilos a los valores por defecto y se
## establecen la anchura y altura del juego.
init python:
    gui.init(1920, 1080)

## Habilitar comprobaciones de propiedades no válidas o inestables en pantallas
## o transformaciones.
define config.check_conflicting_properties = True


################################################################################
## Variables de configuración de la interfaz.
################################################################################


## Colores #####################################################################
##
## Los colores del texto de la interfaz se han ajustado para una mejor legibilidad
## y contraste visual.

## El color enfatizado usado en la interfaz para subrayar texto (optimizado para accesibilidad).
define gui.accent_color = '#d32f2f'  ## Rojo más suave para mejor contraste

## El color del botón de texto cuando no está seleccionado ni enfocado.
define gui.idle_color = '#5d5d5d'  ## Gris más oscuro para mejor legibilidad

## El color 'small' se usa para el texto pequeño, que necesita destacar más.
define gui.idle_small_color = '#4a4a4a'  ## Ajustado para contraste

## El color usado en botones y barras que ganan foco.
define gui.hover_color = '#ff5252'  ## Rojo más brillante para interacción clara

## El color del botón de texto seleccionado pero no enfocado.
define gui.selected_color = '#333333'  ## Gris más oscuro para indicar selección

## El color de los botones de texto que no pueden ser seleccionados.
define gui.insensitive_color = '#aaaaaa7f'  ## Semitransparente para estado deshabilitado

## Colores de la parte vacía de las barras. Optimizados para gradientes suaves.
define gui.muted_color = '#f8bbd0'  ## Rosa claro para fondos
define gui.hover_muted_color = '#ffcdd2'  ## Rosa más claro para hover

## Colores del texto del diálogo y menú.
define gui.text_color = '#212121'  ## Casi negro para mejor legibilidad
define gui.interface_text_color = '#212121'  ## Consistente con el texto


## Tipos y tamaños de letra ####################################################
##
## Se ajustan tamaños para mejor escalabilidad en pantallas grandes.

## El tipo de letra del texto del juego (usar fuentes estándar para compatibilidad).
define gui.text_font = "DejaVuSans.ttf"

## El tipo de letra de los nombres de personajes.
define gui.name_text_font = "DejaVuSans.ttf"

## El tipo de letra del texto externo al juego.
define gui.interface_text_font = "DejaVuSans.ttf"

## El tamaño normal del texto del diálogo (aumentado para 1080p).
define gui.text_size = 36

## El tamaño de los nombres de los personajes.
define gui.name_text_size = 50

## El tamaño del texto en la interfaz.
define gui.interface_text_size = 34

## El tamaño de etiquetas en la interfaz.
define gui.label_text_size = 38

## El tamaño del texto en las notificaciones.
define gui.notify_text_size = 28

## El tamaño del título del juego.
define gui.title_text_size = 80


## Menú principal y menús del juego ############################################
##
## Imágenes del menú principal y menús del juego (rutas relativas optimizadas).
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Diálogo #####################################################################
##
## Variables ajustadas para un diseño más equilibrado en pantallas widescreen.

## Altura de la caja de texto que contiene el diálogo.
define gui.textbox_height = 300

## Colocación vertical de la caja de texto en la pantalla.
define gui.textbox_yalign = 1.0

## Colocación del nombre del personaje hablante.
define gui.name_xpos = 380
define gui.name_ypos = -20  ## Ajustado para superposición estética

## La alineación horizontal del nombre del personaje.
define gui.name_xalign = 0.0

## La anchura, altura y bordes de la caja del nombre.
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(10, 10, 10, 10)  ## Bordes más amplios

## Si el fondo de la caja del nombre será en mosaico.
define gui.namebox_tile = False

## Colocación del diálogo relativa a la caja de texto.
define gui.dialogue_xpos = 420
define gui.dialogue_ypos = 80

## La anchura máxima del texto del diálogo.
define gui.dialogue_width = 1150  ## Aumentado para mejor uso del espacio

## La alineación horizontal del texto del diálogo.
define gui.dialogue_text_xalign = 0.0


## Botones #####################################################################
##
## Aspecto de botones optimizado para tacto y accesibilidad.

## La anchura y altura del botón (valores por defecto para escalabilidad).
define gui.button_width = None
define gui.button_height = 50  ## Altura fija para consistencia

## Los bordes del botón.
define gui.button_borders = Borders(8, 8, 8, 8)  ## Bordes más gruesos

## Si la imagen de fondo será en mosaico.
define gui.button_tile = False

## Tipo de letra del botón.
define gui.button_text_font = gui.interface_text_font

## Tamaño de letra del botón.
define gui.button_text_size = gui.interface_text_size

## Colores del texto del botón.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## La alineación horizontal del texto del botón.
define gui.button_text_xalign = 0.5  ## Centrado para mejor apariencia

## Personalizaciones para tipos de botones específicos.
define gui.radio_button_borders = Borders(30, 8, 8, 8)
define gui.check_button_borders = Borders(30, 8, 8, 8)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(20, 8, 20, 8)
define gui.quick_button_borders = Borders(20, 8, 20, 0)
define gui.quick_button_text_size = 24
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color


## Botones de opción ###########################################################
##
## Optimizados para menús de juego legibles.

define gui.choice_button_width = 1200
define gui.choice_button_height = 60  ## Altura fija para consistencia
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(160, 10, 160, 10)  ## Bordes más amplios
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#5d5d5d'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#aaaaaa7f'


## Botones de partidas #########################################################
##
## Ajustes para miniaturas y texto en partidas guardadas.

define gui.slot_button_width = 420
define gui.slot_button_height = 315
define gui.slot_button_borders = Borders(20, 20, 20, 20)
define gui.slot_button_text_size = 22
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Tamaño de miniaturas de partidas guardadas.
define config.thumbnail_width = 390
define config.thumbnail_height = 220

## Número de columnas y filas de la cuadrícula.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Posicionamiento y espacios ##################################################
##
## Espaciado y posiciones revisados para un diseño más limpio.

define gui.navigation_xpos = 70
define gui.skip_ypos = 20
define gui.notify_ypos = 75
define gui.choice_spacing = 35
define gui.navigation_spacing = 10  ## Aumentado para mejor separación
define gui.pref_spacing = 20
define gui.pref_button_spacing = 5
define gui.page_spacing = 5
define gui.slot_spacing = 20
define gui.main_menu_text_xalign = 1.0


## Marcos ######################################################################
##
## Bordes de marcos ajustados para consistencia visual.

define gui.frame_borders = Borders(8, 8, 8, 8)
define gui.confirm_frame_borders = Borders(70, 70, 70, 70)
define gui.skip_frame_borders = Borders(30, 10, 80, 10)
define gui.notify_frame_borders = Borders(30, 10, 70, 10)
define gui.frame_tile = False


## Barras, barras de desplazamiento y deslizadores #############################
##
## Dimensiones optimizadas para interacción táctil y de ratón.

define gui.bar_size = 40
define gui.scrollbar_size = 20
define gui.slider_size = 40
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False
define gui.bar_borders = Borders(8, 8, 8, 8)
define gui.scrollbar_borders = Borders(8, 8, 8, 8)
define gui.slider_borders = Borders(8, 8, 8, 8)
define gui.vbar_borders = Borders(8, 8, 8, 8)
define gui.vscrollbar_borders = Borders(8, 8, 8, 8)
define gui.vslider_borders = Borders(8, 8, 8, 8)
define gui.unscrollable = "hide"


## Historial ###################################################################
##
## Ajustes para una pantalla de historial más legible.

define config.history_length = 300  ## Aumentado para más entradas

define gui.history_height = 220
define gui.history_spacing = 5
define gui.history_name_xpos = 250
define gui.history_name_ypos = 0
define gui.history_name_width = 250
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 270
define gui.history_text_ypos = 5
define gui.history_text_width = 1120
define gui.history_text_xalign = 0.0


## Modo-NVL ####################################################################
##
## Optimizado para modo narrativo.

define gui.nvl_borders = Borders(0, 20, 0, 35)
define gui.nvl_list_length = 8  ## Más entradas visibles
define gui.nvl_height = 180
define gui.nvl_spacing = 20
define gui.nvl_name_xpos = 660
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 240
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 690
define gui.nvl_text_ypos = 15
define gui.nvl_text_width = 900
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 380
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1180
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 690
define gui.nvl_button_xalign = 0.0


## Localización ################################################################

define gui.language = "unicode"


################################################################################
## Dispositivos Móviles
################################################################################
##
## Mejoras significativas para tablets y teléfonos, con tamaños más grandes y
## espaciado optimizado.

init python:

    @gui.variant
    def touch():
        ## Aumenta el tamaño de botones rápidos para tacto.
        gui.quick_button_borders = Borders(70, 25, 70, 0)

    @gui.variant
    def small():
        ## Ajustes para pantallas pequeñas (teléfonos).
        gui.text_size = 50
        gui.name_text_size = 58
        gui.notify_text_size = 42
        gui.interface_text_size = 50
        gui.button_text_size = 50
        gui.label_text_size = 55

        gui.textbox_height = 380
        gui.name_xpos = 130
        gui.dialogue_xpos = 145
        gui.dialogue_width = 1700

        gui.slider_size = 58

        gui.choice_button_width = 1880
        gui.choice_button_text_size = 50

        gui.navigation_spacing = 35
        gui.pref_button_spacing = 20

        gui.history_height = 300
        gui.history_text_width = 1050

        gui.quick_button_text_size = 35

        gui.file_slot_cols = 2
        gui.file_slot_rows = 3  ## Aumentado para más filas en móviles

        gui.nvl_height = 270
        gui.nvl_name_width = 470
        gui.nvl_name_xpos = 500
        gui.nvl_text_width = 1380
        gui.nvl_text_xpos = 530
        gui.nvl_text_ypos = 10
        gui.nvl_thought_width = 1880
        gui.nvl_thought_xpos = 40
        gui.nvl_button_width = 1880
        gui.nvl_button_xpos = 40