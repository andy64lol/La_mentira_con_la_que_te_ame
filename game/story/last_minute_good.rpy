label last_minute_good_ending:

    stop music fadeout 1.0
    play music "audio/happy.ogg" fadein 2.0

    show yui wtf at yuipos

    Yui "¿Qué... qué acabas de decir?"

    show yui worriedsadtalk at yuipos

    Yui "No... no puedes decir eso ahora. No es justo."

    show yui serioustalk at yuipos

    Yui "Voy a irme. En dos semanas estaré en otro país. ¿Lo entiendes?"

    menu:
        "Entonces ven conmigo":
            jump last_minute_good_continue
        "No me importa la distancia":
            jump last_minute_good_continue

label last_minute_good_continue:

    show yui worriedsadtalk at yuipos

    Yui "¿Cómo puedes ser tan... tan tonto?"

    show yui happytalk at yuipos

    Yui "¿Cómo puedes hacerme sentir así cuando intentaba protegerte?"

    show yui happynormal at yuipos

    Yui "Pensé que si te alejaba, no te dolería cuando me fuera."

    show yui happytalk at yuipos

    Yui "Pero tú... tú nunca me dejas elegir el camino fácil, ¿verdad?"

    show yui serioustalk at yuipos

    Yui "Mi vuelo es en dos semanas. Mi familia ya tiene todo preparado."

    show yui worriednormaltalk at yuipos

    Yui "Pero... hay algo que no te he dicho."

    show yui serioustalk at yuipos

    Yui "Mi padre... él aceptó que me quede un año más. Para terminar la escuela."

    show yui happytalk at yuipos

    Yui "Siempre estuvo dispuesto. Yo... yo solo tenía que decir que quería quedarme."

    show yui worriedsadtalk at yuipos

    Yui "Y ahora que sé que sientes lo mismo..."

    show yui happytalk at yuipos

    Yui "Quiero quedarme. Contigo."

    scene bg parkday at scale_bg
    with fade

    "Un mes después..."

    show yui happynormal at yuileft
    with dissolve

    Yui "¡Oye, despierta! ¡Son las siete y media!"

    show yui happytalk at yuileft

    Yui "¿Qué? ¿Esperabas que cambiara solo porque confesamos nuestros sentimientos?"

    show yui happynormal at yuileft

    Yui "Vamos, vamos a llegar tarde. Y hoy tenemos planes después de clases."

    scene bg housebedroomevening at scale_bg
    with fade

    "Esa tarde, Yui viene a tu casa como siempre."

    "Pero ahora todo es diferente. Ahora son algo más que amigos."

    show yui serioustalk at yuipos
    with dissolve

    Yui "Oye... ¿puedo preguntarte algo?"

    show yui worriedsadtalk at yuipos

    Yui "¿Te arrepientes? ¿De haberme dicho lo que sentías?"

    show yui serioustalk at yuipos

    Yui "Si no lo hubieras hecho... yo me habría ido. Habría seguido mi vida."

    show yui worriedsadtalk at yuipos

    Yui "Pero tú arriesgaste todo. Por mí."

    menu:
        "No me arrepiento":
            jump last_minute_no_regret
        "Me arrepiento de no haberlo dicho antes":
            jump last_minute_wish_earlier

label last_minute_no_regret:

    show yui happytalk at yuipos

    Yui "Eres un idiota. Un idiota valiente."

    show yui happynormal at yuipos

    Yui "Me alegro de que hayas hablado. Aunque fuera en el último momento."

    show yui serioustalk at yuipos

    Yui "A veces el último momento es el único momento que tenemos."

    jump last_minute_ending_continue

label last_minute_wish_earlier:

    show yui wtf at yuipos

    Yui "¿Antes?"

    show yui happytalk at yuipos

    Yui "Sí, eso habría sido ideal. Pero..."

    show yui happynormal at yuipos

    Yui "Pero al menos lo dijiste. Eso es lo importante."

    show yui serioustalk at yuipos

    Yui "Muchas personas nunca dicen lo que sienten. Y se arrepienten toda la vida."

    show yui happytalk at yuipos

    Yui "Tú no serás una de ellas."

    jump last_minute_ending_continue

label last_minute_ending_continue:

    scene bg housebedroomnight at scale_bg
    with fade

    "Esa noche, Yui se queda hasta tarde."

    "Están sentados en el balcón, mirando las estrellas."

    show yui happynormal at yuipos
    with dissolve

    Yui "¿Sabes? Mi padre está feliz."

    show yui happytalk at yuipos

    Yui "Dijo que siempre sospechó que me quedaría. Que me conocía demasiado bien."

    show yui serioustalk at yuipos

    Yui "Mi madre lloró. Pero eran lágrimas de felicidad."

    show yui worriedsadtalk at yuipos

    Yui "Dijo que una madre siempre sabe cuándo su hija está enamorada."

    show yui happytalk at yuipos

    Yui "Y tenía razón. Estoy enamorada. De ti."

    "El viento sopla suavemente. Las estrellas brillan."

    "Todo es perfecto. Todo es como debería ser."

    show yui serioustalk at yuipos

    Yui "Oye... prométeme algo."

    show yui worriedsadtalk at yuipos

    Yui "Prométeme que cada día me dirás lo que sientes. No importa qué."

    show yui serioustalk at yuipos

    Yui "No quiero que volvamos a estar en silencio. A tener miedo."

    show yui happytalk at yuipos

    Yui "Quiero que hablemos. Siempre."

    menu:
        "Lo prometo":
            jump last_minute_promise
        "Cada día":
            jump last_minute_promise

label last_minute_promise:

    show yui happytalk at yuipos

    Yui "Gracias."

    show yui happynormal at yuipos

    Yui "Por todo. Por hablar. Por quedarte. Por amarme."

    show yui serioustalk at yuipos

    Yui "Eres mi persona favorita. Mi idiota favorito."

    show yui happytalk at yuipos

    Yui "Y siempre lo serás."

    scene black
    with fade

    "Años después..."

    scene bg parkday at scale_bg
    with fade

    "Están en el mismo parque. El parque donde todo comenzó."

    "Ahora son adultos. Ahora tienen una vida juntos."

    show yui happynormal at yuipos
    with dissolve

    Yui "¿Recuerdas ese día?"

    show yui happytalk at yuipos

    Yui "Cuando casi me dejas ir. Cuando casi perdemos todo."

    show yui serioustalk at yuipos

    Yui "Gracias por no rendirte. Por hablar en el último momento."

    show yui happytalk at yuipos

    Yui "Por salvarnos."

    scene black
    with fade

    "FINAL BUENO: Confesión de último momento"

    "A veces, el momento perfecto es el último momento."

    "Yui se quedó. No por un año, sino para siempre."

    "Y cada mañana, sigue siendo mi voz de alarma, mi sombra, mi razón para sonreír."

    "Gracias por jugar."

    return
