label neutral_ending:

    show yui wtf at yuipos

    Yui "¿Amiga?"

    show yui serioustalk at yuipos

    Yui "Sí... supongo que eso es lo que soy."

    show yui worriedsadtalk at yuipos

    Yui "Una amiga que se va. Que te abandonará."

    show yui angry at yuipos

    Yui "Adiós entonces. Olvida que existí."

    scene bg parkday at scale_bg
    with fade

    "Yui se aleja. No la detienes."

    "¿Qué podrías decir? ¿Que la amas? ¿Que quieres que se quede?"

    "Las palabras se atoran en tu garganta."

    "Y ella se va."

    scene black
    with fade

    "Los días siguientes son extraños."

    scene bg schoolhallway at scale_bg
    with fade

    "Yui sigue en la escuela. Pero ahora hay una distancia entre ustedes."

    "Un muro invisible que ninguno de los dos cruza."

    show yui serioustalk at yuileft
    with dissolve

    Yui "Oye..."

    show yui worriedsadtalk at yuileft

    Yui "Mi vuelo es el viernes. En tres días."

    show yui serioustalk at yuileft

    Yui "Quería que lo supieras. Por si... por si quieres despedirte."

    menu:
        "Claro que sí":
            jump neutral_farewell
        "Si eso es lo que quieres":
            jump neutral_uncertain

label neutral_farewell:

    show yui happytalk at yuileft

    Yui "Gracias."

    show yui happynormal at yuileft

    Yui "Eso... eso significa mucho."

    jump neutral_ending_days

label neutral_uncertain:

    show yui wtf at yuileft

    Yui "¿Si es lo que quiero?"

    show yui serioustalk at yuileft

    Yui "No lo sé. No sé qué quiero."

    show yui worriedsadtalk at yuileft

    Yui "Pero supongo que... supongo que quiero que estés ahí."

    jump neutral_ending_days

label neutral_ending_days:

    scene bg housebedroomevening at scale_bg
    with fade

    "Pasas los últimos días juntos."

    "Pero todo es diferente. Forzado. Incómodo."

    "Como dos extraños que solían conocerse."

    show yui serioustalk at yuipos
    with dissolve

    Yui "¿Recuerdas cuando éramos niños?"

    show yui worriedsadtalk at yuipos

    Yui "Cuando todo era simple. Cuando éramos simples."

    show yui serioustalk at yuipos

    Yui "Ahora todo es complicado. Los sentimientos. Las palabras."

    show yui happynormal at yuipos

    Yui "A veces desearía volver a esa época."

    menu:
        "Yo también":
            jump neutral_nostalgia
        "Todo cambia":
            jump neutral_acceptance

label neutral_nostalgia:

    show yui happytalk at yuipos

    Yui "¿Verdad?"

    show yui happynormal at yuipos

    Yui "Eras más fácil de entonces. Más simple."

    show yui serioustalk at yuipos

    Yui "Ahora... ahora no sé qué sientes. Qué piensas."

    show yui worriedsadtalk at yuipos

    Yui "Y eso me asusta."

    jump neutral_final_goodbye

label neutral_acceptance:

    show yui serioustalk at yuipos

    Yui "Sí. Todo cambia."

    show yui worriedsadtalk at yuipos

    Yui "Nosotros cambiamos. La vida cambia."

    show yui happynormal at yuipos

    Yui "Quizás eso no es malo. Quizás es necesario."

    jump neutral_final_goodbye

label neutral_final_goodbye:

    scene black
    with fade

    "El día de la despedida llega."

    scene bg trainstation at scale_bg
    with fade

    "Estás en la estación. Yui está ahí, con una maleta y una sonrisa forzada."

    show yui happynormal at yuipos
    with dissolve

    Yui "Bueno... esto es."

    show yui serioustalk at yuipos

    Yui "Gracias por venir. Por estos años. Por todo."

    show yui worriedsadtalk at yuipos

    Yui "Eres... eras importante para mí."

    show yui happynormal at yuipos

    Yui "Cuídate, ¿sí?"

    menu:
        "Tú también":
            jump neutral_final_words
        "Adiós":
            jump neutral_final_words

label neutral_final_words:

    show yui happytalk at yuipos

    Yui "Adiós."

    hide yui
    with moveoutright

    "Se va. No hay lágrimas. No hay abrazos."

    "Solo una despedida silenciosa entre dos personas que solían ser amigas."

    scene black
    with fade

    "Un mes después..."

    scene bg housebedroomnight at scale_bg
    with fade

    "Estás en tu cuarto. Solo."

    "Las mañanas son más silenciosas sin Yui."

    "Pero la vida continúa. La escuela continúa."

    "A veces piensas en ella. ¿Dónde estará? ¿Cómo será su vida?"

    "Pero no hay respuestas. Solo preguntas."

    "Y la distancia que crece entre ustedes, kilómetro a kilómetro."

    scene black
    with fade

    "FINAL NEUTRAL: La distancia"

    "Yui se alejó ese día. Nunca supiste si llegó bien a su destino."

    "Las mañanas son más silenciosas ahora."

    "Gracias por jugar."

    return
