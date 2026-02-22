﻿define Yui = Character("Yui", color="#239ade")
define You = Character("You", color="#404040")
define Unknown = Character("???", color="#404040")

image bg housebedroomyourday = "bg/housebedroomyourday.png"
image bg parkday = "bg/parkday.jpg"
image bg schoolhallway = "bg/schoolhallway.jpg"
image bg classroom = "bg/classroom.jpg"
image bg yuiroom = "bg/yuiroom.png"
image bg trainstation = "bg/trainstation.jpg"

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
            jump revelation
        "¿Por qué no me dijiste antes?":
            $ yui_affection += 1
            jump revelation

label revelation:

    show yui worriedsadtalk at yuipos

    Yui "En dos semanas. Mi padre consiguió trabajo en el extranjero."

    show yui serioustalk at yuipos

    Yui "No quería decírtelo. No quería ver tu cara cuando..."

    show yui worriedsadtalk at yuipos

    Yui "Cuando te diera la noticia."

    menu:
        "¿Y nosotros?":
            jump emotional_confrontation
        "Voy a extrañarte":
            $ yui_affection += 2
            jump emotional_confrontation

label emotional_confrontation:

    show yui angry at yuipos
    with dissolve

    Yui "¡No digas eso!"

    show yui angrytalk at yuipos

    Yui "No quiero que me extrañes. No quiero que..."

    show yui worriedsadtalk at yuipos

    Yui "No quiero que sufras cuando me vaya."

    show yui serioustalk at yuipos

    Yui "Así que... así que he decidido algo."

    show yui angry at yuipos

    Yui "Voy a alejarme de ti. Ahora. Antes de que sea peor."

    menu push_away_choice:
        "¿Por qué haces esto?":
            jump why_push_away
        "No me dejes":
            jump beg_stay
        "Si eso es lo que quieres...":
            jump accept_distance

label why_push_away:

    show yui angrytalk at yuipos

    Yui "¡Porque no quiero que me recuerdes!"

    show yui worriedsadtalk at yuipos

    Yui "Si te alejo ahora... si te hago odiarme..."

    show yui serioustalk at yuipos

    Yui "Entonces cuando me vaya, no te dolerá."

    menu:
        "Eso no es cierto":
            jump truth_moment
        "Eres una cobarde":
            $ yui_affection -= 1
            jump harsh_truth

label beg_stay:

    show yui worriedsadtalk at yuipos

    Yui "No me pidas eso. No puedo... no puedo decir que no si me lo pides así."

    show yui serioustalk at yuipos

    Yui "Pero tengo que hacerlo. Por los dos."

    menu:
        "Te necesito":
            jump truth_moment
        "Entiendo...":
            jump accept_distance

label accept_distance:

    show yui wtf at yuipos

    Yui "¿Eso es todo? ¿No vas a pelear?"

    show yui angry at yuipos

    Yui "¿No te importa lo suficiente como para discutir?"

    menu:
        "Me importas demasiado para forzarte":
            jump truth_moment
        "Si quieres irte, ve":
            jump bad_ending

label harsh_truth:

    show yui angrytalk at yuipos

    Yui "¡¿Cobarde?! ¡Tú no sabes nada!"

    show yui worriedsadtalk at yuipos

    Yui "He pasado meses llorando por las noches. Meses..."

    show yui serioustalk at yuipos

    Yui "Olvídalo. Esto termina aquí."

    jump bad_ending

label truth_moment:

    show yui worriedsadtalk at yuipos

    Yui "¿Qué quieres que haga? ¿Que te diga la verdad?"

    show yui serioustalk at yuipos

    Yui "La verdad es que..."

    show yui worriedsadtalk at yuipos

    Yui "La verdad es que te amo."

    show yui serioustalk at yuipos

    Yui "Te amo y me voy. Y no puedo soportar la idea de dejarte atrás."

    show yui worriedsadtalk at yuipos

    Yui "Así que prefiero que me odies. Es más fácil."

    menu final_choice:
        "Yo también te amo":
            if yui_affection >= 3:
                jump true_ending
            else:
                jump good_ending
        "Siempre serás mi amiga":
            jump neutral_ending
        "Entonces adiós":
            jump bad_ending

label true_ending:

    stop music fadeout 1.0
    play music "audio/happy.ogg" fadein 2.0

    show yui wtf at yuipos

    Yui "¿...Qué?"

    show yui happytalk at yuipos

    Yui "¿De verdad? ¿No estás bromeando?"

    show yui happynormal at yuipos

    You "Nunca te dejaría ir sin decírtelo."

    show yui worriedsadtalk at yuipos

    Yui "Pero... pero me voy. En dos semanas."

    show yui serioustalk at yuipos

    You "Entonces tenemos dos semanas. Y luego... nos las arreglaremos."

    show yui happytalk at yuipos

    Yui "Eres un idiota. Un idiota hermoso."

    scene black
    with fade

    "Dos semanas después..."

    scene bg trainstation at scale_bg
    with fade

    show yui worriedsadtalk at yuipos
    with dissolve

    Yui "Es hora."

    show yui serioustalk at yuipos

    Yui "Prométeme que no olvidarás lo que dijimos aquí."

    show yui happytalk at yuipos

    Yui "Prométeme que vendrás a verme."

    You "Lo prometo."

    show yui happynormal at yuipos

    Yui "Entonces... no es un adiós. Es un hasta luego."

    scene black
    with fade

    "FINAL VERDADERO: La promesa"

    "Aunque la distancia nos separa, nuestros corazones permanecen juntos."

    "Gracias por jugar."

    return

label good_ending:

    stop music fadeout 1.0
    play music "audio/bittersweet.ogg" fadein 2.0

    show yui happytalk at yuipos

    Yui "¿De verdad lo sientes así?"

    show yui happynormal at yuipos

    Yui "Eso... eso significa mucho para mí."

    show yui serioustalk at yuipos

    Yui "Pero aún así me voy. Y no quiero que esperes."

    show yui worriedsadtalk at yuipos

    Yui "Quiero que seas feliz. Con o sinmigo."

    show yui happytalk at yuipos

    Yui "Gracias por estos años. Por cada mañana."

    scene black
    with fade

    "FINAL BUENO: El primer amor"

    "A veces amar a alguien significa dejarlo ir."

    "Yui se fue, pero su recuerdo permanece vivo en cada amanecer."

    "Gracias por jugar."

    return

label neutral_ending:

    show yui wtf at yuipos

    Yui "¿Amiga?"

    show yui serioustalk at yuipos

    Yui "Sí... supongo que eso es lo que soy."

    show yui worriedsadtalk at yuipos

    Yui "Una amiga que se va. Que te abandonará."

    show yui angry at yuipos

    Yui "Adiós entonces. Olvida que existí."

    scene black
    with fade

    "FINAL NEUTRAL: La distancia"

    "Yui se alejó ese día. Nunca supiste si llegó bien a su destino."

    "Las mañanas son más silenciosas ahora."

    "Gracias por jugar."

    return

label bad_ending:

    stop music fadeout 1.0
    play music "audio/sad.ogg" fadein 2.0

    show yui angry at yuipos

    Yui "Bien."

    show yui angrytalk at yuipos

    Yui "Eso es lo que quería oír."

    show yui serioustalk at yuipos

    Yui "No te preocupes. En dos semanas, habré desaparecido de tu vida."

    show yui worriedsadtalk at yuipos

    Yui "Como si nunca hubiera existido."

    scene black
    with fade

    "FINAL MALO: La mentira completa"

    "Yui cumplió su palabra. Se fue sin despedirse."

    "Nunca supiste la verdad. Nunca supiste que te amaba."

    "A veces el silencio es la peor mentira de todas."

    "Gracias por jugar."

    return

init python:
    yui_affection = 0
