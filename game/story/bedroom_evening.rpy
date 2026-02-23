label bedroom_evening:

    scene black
    with fade

    "El día siguiente. La tarde llega demasiado rápido."

    scene bg housebedroomevening at scale_bg
    with fade

    play music "audio/bittersweet.ogg" fadein 2.0

    "Estás en tu cuarto, intentando hacer tarea."

    "Pero no puedes concentrarte. La imagen de Yui no deja tu mente."

    "Su sonrisa. Su voz. La forma en que te grita cada mañana."

    "Todo eso... ¿se acaba?"

    "Hay un golpe en la puerta."

    menu:
        "Abrir":
            jump door_opens
        "¿Quién es?":
            jump door_opens

label door_opens:

    show yui happynormal at yuipos
    with dissolve

    Yui "¡Sorpresa!"

    show yui happytalk at yuipos

    Yui "Traje... traje algo."

    show yui serioustalk at yuipos

    Yui "Mi madre hizo mucha comida. Dijo que... que debería compartirla contigo."

    show yui worriedsadtalk at yuipos

    Yui "Antes de que... ya sabes."

    show yui happynormal at yuipos

    Yui "¿Puedo pasar?"

    menu:
        "Claro, pasa":
            jump yui_enters_room
        "¿Qué traes?":
            jump yui_enters_room

label yui_enters_room:

    show yui happytalk at yuipos

    Yui "Onigiri. Los que más te gustan."

    show yui happynormal at yuipos

    Yui "Con atún. Y algunos con salmón. Por si acaso."

    show yui serioustalk at yuipos

    Yui "Mi madre se acordó de que te gustan. Después de todos estos años..."

    show yui worriedsadtalk at yuipos

    Yui "Ella también está triste. Por irse. Por dejar atrás tantos recuerdos."

    show yui serioustalk at yuipos

    Yui "Pero dice que es lo mejor. Para el futuro de la familia."

    "Te sientas juntos en el suelo. Los onigiri están deliciosos."

    show yui happynormal at yuipos

    Yui "Oye..."

    show yui serioustalk at yuipos

    Yui "¿Recuerdas cuando éramos pequeños y comíamos esto en el parque?"

    show yui happytalk at yuipos

    Yui "Tú siempre te ensuciabas la cara. Tenía que limpiarte con mi pañuelo."

    show yui happynormal at yuipos

    Yui "Eras un niño muy desordenado."

    menu:
        "Tú también te ensuciabas":
            jump messy_memory
        "Tú siempre me cuidabas":
            $ yui_affection += 1
            jump caring_memory

label messy_memory:

    show yui angry at yuipos

    Yui "¡Yo no! Yo era... era perfecta."

    show yui happytalk at yuipos

    Yui "Bueno, tal vez una vez. O dos."

    show yui happynormal at yuipos

    Yui "Pero tú... tú eras un desastre. ¿Recuerdas cuando te caíste del árbol?"

    show yui worriedsadtalk at yuipos

    Yui "Lloraste tanto. Pensé que... que te habías hecho daño de verdad."

    show yui serioustalk at yuipos

    Yui "No quiero que te caigas de nuevo. Cuando me vaya..."

    show yui worriedsadtalk at yuipos

    Yui "Cuando me vaya, ten cuidado. ¿Sí?"

    jump evening_continues

label caring_memory:

    show yui wtf at yuipos

    Yui "¿Yo? ¿Cuidarte?"

    show yui happytalk at yuipos

    Yui "Alguien tenía que hacerlo. Tú solo... solo te metías en problemas."

    show yui happynormal at yuipos

    Yui "Siempre. Cada día. Un problema nuevo."

    show yui serioustalk at yuipos

    Yui "Pero... pero me gustaba."

    show yui worriedsadtalk at yuipos

    Yui "Me gustaba cuidarte. Me hacía sentir... útil. Importante."

    show yui serioustalk at yuipos

    Yui "¿Quién cuidará de ti cuando me vaya?"

    jump evening_continues

label evening_continues:

    show yui serioustalk at yuipos

    Yui "Oye..."

    show yui worriedsadtalk at yuipos

    Yui "¿Puedo pedirte algo?"

    show yui serioustalk at yuipos

    Yui "Antes de que me vaya... quiero hacer todo lo que solíamos hacer."

    show yui happytalk at yuipos

    Yui "Quiero ir al parque. Al cine. Comer helado."

    show yui worriedsadtalk at yuipos

    Yui "Quiero crear recuerdos. Buenos recuerdos. Para... para reemplazar los malos."

    show yui serioustalk at yuipos

    Yui "¿Lo harás conmigo? ¿Estas dos semanas?"

    menu:
        "Por supuesto":
            $ yui_affection += 1
            jump promise_made
        "Haré todo lo que quieras":
            jump promise_made

label promise_made:

    show yui happytalk at yuipos

    Yui "Gracias."

    show yui happynormal at yuipos

    Yui "Eres... eres la mejor persona que conozco."

    show yui serioustalk at yuipos

    Yui "Aunque seas un idiota. Un tonto. Un desastre."

    show yui happytalk at yuipos

    Yui "Eres mi idiota favorito."

    "Yui se queda un rato más. Hablan de cosas sin importancia."

    "El clima. La escuela. Los vecinos."

    "Cualquier cosa menos el futuro. Menos la despedida."

    show yui worriedsadtalk at yuipos

    Yui "Debo irme. Mis padres se preocuparán."

    show yui serioustalk at yuipos

    Yui "Nos vemos mañana. En la escuela."

    show yui happytalk at yuipos

    Yui "No llegues tarde, ¿sí?"

    hide yui
    with moveoutright

    "Yui se va. La habitación se siente vacía sin ella."

    "Pero hay algo diferente. Una promesa. Dos semanas de recuerdos."

    "¿Será suficiente?"

    scene black
    with fade

    "Días después..."

    jump school_days_pass
