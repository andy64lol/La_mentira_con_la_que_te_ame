define Yui = Character("Yui", color="#239ade")
define Unknown = Character("???")
define You = Character("You", color="#239ade")
image bg housebedroomyourday = "bg/housebedroomyourday.png"
image yui happytalk = "yui/yui happytalk.png"
image yui happynormal = "yui/yui happynormal.png"
image yui angrytalk = "yui/yui angrytalk.png"
image bg parkday = "bg/parkday.jpg"
image yui serioustalk = "yui/yui serioustalk.png"
image black = Solid("#000000")

define config.default_text_cps = 20

label start:

    "La mentira con la que te amé"
    "Hecho por andy64lol"

    Unknown "¡Oye! ¡Despierta! ¡Tienes que ir a la escuela!"
    Unknown "¡Vamos! ¡Rápido! ¡No quiero llegar tarde!"

    scene bg housebedroomyourday:
        xysize (1920, 1080)

    "Ella es tu amiga de la infancia, Yui, y te ha estado despertando desde que eras un niño."

    show yui happytalk:
        zoom 0.8
        xalign 0.5
        yalign 0.5
    Yui "¿Me estás escuchando acaso? ¡Vamos! ¡Rápido!"

    show yui happynormal:
        zoom 0.8
        xalign 0.5
        yalign 0.5
    "Te levantas de la cama y te vistes rápidamente, sin querer perder más tiempo."

    show yui happytalk:
        zoom 0.8
        xalign 0.5
        yalign 0.5
    Yui "Venga, que por tu culpa no llegamos a clase y nos van a echar una bronca que no veas."

    show black

    jump afterschool

label afterschool:

    show black

    "Después de la escuela, te encuentras con Yui en el parque."

    hide black

    show bg parkday:
        xysize (1920, 1080)

    show yui happynormal:
        zoom 0.8
        xalign 0.5
        yalign 0.5
    Yui "¡Hola! ¿Cómo te fue en la escuela hoy?"

    "Le cuentas a Yui sobre tu día, pero ella parece distraída."

    show yui serioustalk:
        zoom 0.8
        xalign 0.5
        yalign 0.5
    Yui "¿Sabes? He estado pensando en algo últimamente..."
    Yui "¿Alguna vez has sentido que hay algo que no te estoy diciendo?"

    menu choose_yes_no:
        "¿Crees que ella te está ocultando algo?"
        "No creo la verdad, ella nunca me ocultaría nada...":
            jump afterschool_accept
        "Sí, siento que hay algo raro con ella últimamente...":
            jump afterschool_deny
    
label afterschool_deny:

    show yui worriednormaltalk:
        zoom 0.8
        xalign 0.5
        yalign 0.5

    Yui "Bueno, es que... no es nada importante, solo cosas de la escuela y eso."
    You "¿De verdad? ¿Entonces por qué te ves tan preocupada últimamente?"
    Yui "No es nada, de verdad. No quiero que te preocupes por mí."
    
    menu interrogate_yui:
        "¿La interrogas para que te diga la verdad?"
        "No":
            "Está bien, no quiero presionarte. Si quieres hablar de ello, estaré aquí para escucharte."
            return
        "Sí":
            "Vamos, dime qué es lo que te está pasando. No me gusta verte así."
            return

label afterschool_accept:
    
    show yui serioustalk:
        zoom 0.8
        xalign 0.5
        yalign 0.5
    
    Yui "Bueno... no es nada grave, solo que... nada, déjalo."
    return