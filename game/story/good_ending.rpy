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

    scene bg parkday at scale_bg
    with fade

    "Los días siguientes son extraños."

    "Yui sigue a tu lado, pero hay una distancia invisible."

    "Una barrera que ella construyó para protegerte."

    show yui serioustalk at yuileft
    with dissolve

    Yui "Oye... ¿puedo pedirte algo?"

    show yui worriedsadtalk at yuileft

    Yui "Estas últimas semanas... quiero que seamos normales."

    show yui serioustalk at yuileft

    Yui "No quiero lágrimas. No quiero despedidas tristes."

    show yui happytalk at yuileft

    Yui "Quiero reír. Quiero que me grites cuando llegue tarde."

    show yui happynormal at yuileft

    Yui "Quiero que todo sea como siempre."

    menu:
        "Lo intentaré":
            jump good_ending_normal_days
        "No puedo fingir":
            jump good_ending_honest_days

label good_ending_normal_days:

    show yui happytalk at yuileft

    Yui "Gracias."

    show yui happynormal at yuileft

    Yui "Eres fuerte. Más fuerte de lo que crees."

    scene bg housebedroomyourday at scale_bg
    with fade

    "Intentas ser normal. Intentas sonreír."

    "Pero cada mañana, cuando Yui aparece en tu puerta, sientes un nudo en el estómago."

    "Cada '¡Despierta!' es un recordatorio del tiempo que se acaba."

    scene bg classroom at scale_bg
    with fade

    "En la escuela, todo parece igual."

    "Yui sigue sentada a tu lado. Sigue robándote los lápices."

    "Sigue siendo ella."

    "Pero tú la miras diferente. Ahora sabes lo que siente. Lo que sientes."

    "Y ninguno de los dos dice nada."

    jump good_ending_final_moments

label good_ending_honest_days:

    show yui worriedsadtalk at yuileft

    Yui "Lo sé. No puedo pedirte eso."

    show yui serioustalk at yuileft

    Yui "Entonces seamos honestos. Al menos entre nosotros."

    scene bg housebedroomevening at scale_bg
    with fade

    "Pasas las noches hablando."

    "De todo. De nada. De lo que vendrá."

    show yui serioustalk at yuipos
    with dissolve

    Yui "¿Crees que el amor de verdad existe?"

    show yui worriedsadtalk at yuipos

    Yui "Quiero decir... el amor que dura. Que sobrevive a la distancia."

    menu:
        "Creo que sí":
            jump good_ending_believe_love
        "No lo sé":
            jump good_ending_uncertain_love

label good_ending_believe_love:

    show yui happytalk at yuipos

    Yui "Espero que tengas razón."

    show yui happynormal at yuipos

    Yui "Porque yo... yo también lo creo."

    show yui serioustalk at yuipos

    Yui "Aunque a veces me cueste."

    jump good_ending_final_moments

label good_ending_uncertain_love:

    show yui serioustalk at yuipos

    Yui "La honestidad... a veces duele."

    show yui worriedsadtalk at yuipos

    Yui "Pero prefiero eso a las mentiras."

    show yui happynormal at yuipos

    Yui "Gracias por ser real conmigo."

    jump good_ending_final_moments

label good_ending_final_moments:

    scene black
    with fade

    "La última semana llega demasiado rápido."

    scene bg housebedroomnight at scale_bg
    with fade

    "Es tu última noche juntos."

    "Yui está en tu cuarto. Están sentados en el suelo, como cuando eran niños."

    show yui happynormal at yuipos
    with dissolve

    Yui "Mañana... mañana me voy."

    show yui worriedsadtalk at yuipos

    Yui "Mi vuelo sale al amanecer."

    show yui serioustalk at yuipos

    Yui "No quiero que vengas al aeropuerto. No quiero una despedida larga."

    show yui happytalk at yuipos

    Yui "Quiero que el último recuerdo sea aquí. En tu cuarto. Donde todo comenzó."

    menu:
        "Entiendo":
            jump good_ending_goodbye
        "Quiero ir":
            jump good_ending_airport_refused

label good_ending_airport_refused:

    show yui serioustalk at yuipos

    Yui "No. Por favor."

    show yui worriedsadtalk at yuipos

    Yui "Si te veo llorar... si te veo sufriendo... no podré irme."

    show yui serioustalk at yuipos

    Yui "Y debo irme. Por mi familia. Por mi futuro."

    show yui happytalk at yuipos

    Yui "Quédate aquí. Piensa en mí. Eso es suficiente."

    jump good_ending_goodbye

label good_ending_goodbye:

    show yui happynormal at yuipos

    Yui "Eres mi mejor amigo. Mi primera persona."

    show yui happytalk at yuipos

    Yui "Nunca te olvidaré. Nunca."

    show yui serioustalk at yuipos

    Yui "Y si algún día... si algún día encuentras a alguien..."

    show yui worriedsadtalk at yuipos

    Yui "Alguien que te haga feliz..."

    show yui happytalk at yuipos

    Yui "No dudes. No esperes. Sé feliz."

    "Yui se levanta. Camina hacia la puerta."

    show yui happynormal at yuipos

    Yui "Buenas noches, idiota."

    show yui happytalk at yuipos

    Yui "Gracias por todo."

    hide yui
    with moveoutright

    "Se va. No te das la vuelta. No quieres verla partir."

    "Escuchas la puerta cerrarse. El silencio que sigue es ensordecedor."

    scene black
    with fade

    "Un mes después..."

    scene bg housebedroomnight at scale_bg
    with fade

    "Estás solo en tu cuarto."

    "Las mañanas son diferentes ahora. Más silenciosas."

    "Pero Yui tenía razón. El recuerdo permanece."

    "Cada amanecer, piensas en ella."

    "Y sonríes. Porque la tuviste. Porque la amaste."

    "Y eso es suficiente."

    scene black
    with fade

    "FINAL BUENO: El primer amor"

    "A veces amar a alguien significa dejarlo ir."

    "Yui se fue, pero su recuerdo permanece vivo en cada amanecer."

    "Gracias por jugar."

    return
