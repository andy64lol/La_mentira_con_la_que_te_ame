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

    scene bg parkday at scale_bg
    with fade

    "Las dos semanas siguientes son un regalo."

    "Cada día con Yui es un tesoro que guardas en tu corazón."

    show yui happynormal at yuileft
    with dissolve

    Yui "¡Vamos! ¡El cine empieza en veinte minutos!"

    show yui happytalk at yuileft

    Yui "Y esta vez no me importa si te quedas dormido. Te despertaré con un codazo."

    scene bg housebedroomevening at scale_bg
    with fade

    "Las noches son diferentes ahora."

    "Yui viene a tu casa. Estudia en tu cuarto. Se queda hasta tarde."

    show yui serioustalk at yuipos
    with dissolve

    Yui "Oye... ¿puedo pedirte algo?"

    show yui worriedsadtalk at yuipos

    Yui "Esta noche... quiero quedarme. Hasta el amanecer."

    show yui serioustalk at yuipos

    Yui "Quiero ver el amanecer contigo. Una última vez."

    menu:
        "Por supuesto":
            jump true_ending_night_together
        "Siempre":
            jump true_ending_night_together

label true_ending_night_together:

    scene bg housebedroomnight at scale_bg
    with fade

    play music "audio/bittersweet.ogg" fadein 2.0

    "Están sentados en el balcón. Las estrellas brillan sobre ustedes."

    show yui happynormal at yuipos
    with dissolve

    Yui "¿Recuerdas cuando éramos niños y contábamos estrellas?"

    show yui happytalk at yuipos

    Yui "Tú siempre perdías la cuenta. Decías que había infinitas."

    show yui serioustalk at yuipos

    Yui "Ahora sé que tenías razón."

    show yui worriedsadtalk at yuipos

    Yui "Hay infinitas. Infinitos recuerdos. Infinitos momentos."

    show yui happytalk at yuipos

    Yui "Y aunque me vaya... seguirán ahí. Contigo."

    "El amanecer llega lentamente. Colores de rosa y naranja pintan el cielo."

    show yui happynormal at yuipos

    Yui "Es hermoso."

    show yui happytalk at yuipos

    Yui "Gracias. Por todo. Por estos diez años. Por estas dos semanas."

    show yui serioustalk at yuipos

    Yui "Por amarme."

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

    "Un mes después..."

    scene bg housebedroomnight at scale_bg
    with fade

    "Estás en tu cuarto. Solo."

    "Pero no del todo solo."

    "Tu teléfono vibra. Un mensaje de Yui."

    "'¿Estás despierto?'"

    "'Aquí es de día. Estoy en el parque. El mismo donde solíamos ir.'"

    "'Te extraño.'"

    "Sonríes. Escribes una respuesta."

    "'Yo también te extraño. Siempre.'"

    scene black
    with fade

    "FINAL VERDADERO: La promesa"

    "Aunque la distancia nos separa, nuestros corazones permanecen juntos."

    "Cada noche, las estrellas nos recuerdan que el amor verdadero no conoce fronteras."

    "Gracias por jugar."

    return
