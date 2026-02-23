define Yui = Character("Yui", color="#239ade")
define You = Character("Tú", color="#404040")
define Unknown = Character("???", color="#404040")

image bg housebedroomyourday = "bg/Bedroom_Day.png"
image bg parkday = "bg/parkday.jpg"
image bg schoolhallway = "bg/schoolhallway.jpg"
image bg classroom = "bg/Classroom_Day.png"
image bg yuiroom = "bg/yuiroom.png"
image bg trainstation = "bg/trainstation.jpg"
image bg housebedroomnight = "bg/Bedroom_Night.png"
image bg housebedroomevening = "bg/Bedroom_Evening.png"

image yui happytalk = "yui/yui happytalk.png"
image yui happynormal = "yui/yui happynormal.png"
image yui angrytalk = "yui/yui angrytalk.png"
image yui angry = "yui/yui angry.png"
image yui serioustalk = "yui/yui serioustalk.png"
image yui worriednormaltalk = "yui/yui worriednormaltalk.png"
image yui worriedsadtalk = "yui/yui worriedsadtalk.png"
image yui wtf = "yui/yui wtf.png"

image black = Solid("#000000")

transform scale_bg:
    xysize (1920, 1080)
    xpos 0
    ypos 0

define config.default_text_cps = 40

transform yuipos:
    zoom 0.8
    xalign 0.5
    yalign 0.5

transform yuileft:
    zoom 0.8
    xalign 0.3
    yalign 0.5

transform yuiright:
    zoom 0.8
    xalign 0.7
    yalign 0.5

transform shake:
    xoffset 0
    pause 0.05
    xoffset 5
    pause 0.05
    xoffset -5
    pause 0.05
    xoffset 5
    pause 0.05
    xoffset 0

label start:

    scene black
    with fade

    "La mentira con la que te amé"
    "Hecho por andy64lolxd"

    play music "audio/sad.ogg" fadein 2.0

    "Hace diez años, una niña con coletas azules apareció en mi puerta."
    "Desde ese día, Yui ha sido mi sombra, mi voz de alarma, mi razón para levantarme cada mañana."
    "Pero últimamente... algo ha cambiado."

    stop music fadeout 2.0

    scene bg housebedroomyourday at scale_bg
    with fade

    play music "audio/morning.ogg" fadein 1.0

    Unknown "¡Oye! ¡Despierta!"

    show yui angrytalk at yuipos
    with dissolve

    Yui "¡Son las siete y media! ¡Ya es tarde!"

    show yui angry at yuipos

    You "Cinco minutos más..."

    show yui wtf at yuipos

    Yui "¡NO! ¡Ahora!"

    show yui angrytalk at yuipos

    Yui "Levanta esa perezosa cabeza o te arrastro yo misma."

    scene black
    with fade

    "Te levantas a regañadientes. El ritual de siempre."

    scene bg schoolhallway at scale_bg
    with fade

    show yui happynormal at yuileft
    with moveinleft

    Yui "¿Trajiste el almuerzo?"

    menu:
        "Sí, lo tengo":
            $ yui_affection += 1
            show yui happytalk at yuileft
            Yui "Bien. No quiero que te desmayes en clase otra vez."
        "No, lo olvidé":
            show yui angrytalk at yuileft
            Yui "¡Idiota! ¿Qué vas a comer?"
            show yui worriednormaltalk at yuileft
            Yui "...Puedes compartir el mío. Pero solo hoy."

    scene bg classroom at scale_bg
    with fade

    "Las horas pasan. Yui está sentada a tu lado como siempre."
    "Pero notas que mira por la ventana más de lo habitual."

    show yui serioustalk at yuiright
    with dissolve

    Yui "Oye..."

    show yui worriednormaltalk at yuiright

    Yui "¿Recuerdas cuando éramos pequeños? ¿Cuando decías que nunca te irías de mi lado?"

    menu:
        "Claro que lo recuerdo":
            $ yui_affection += 1
            show yui happytalk at yuiright
            Yui "Eres un tonto sentimental."
        "Eso fue hace mucho":
            show yui serioustalk at yuiright
            Yui "Sí... mucho."

    scene black
    with fade

    stop music fadeout 2.0

    "Después de clases, Yui te arrastra al parque."

    scene bg parkday at scale_bg
    with fade

    play music "audio/music-for-videos-deep-feel-sensitive-piano-music-164514.mp3" fadein 2.0

    show yui happynormal at yuipos
    with dissolve

    Yui "¡Por fin! Aire libre."

    show yui serioustalk at yuipos

    Yui "Necesito... necesito decirte algo."

    show yui worriedsadtalk at yuipos

    Yui "Mi familia... se muda. A otro país."

    menu:
        "¿Cuándo?":
            jump bedroom_night
        "¿Por qué no me dijiste antes?":
            $ yui_affection += 1
            jump bedroom_night

init python:
    yui_affection = 0
