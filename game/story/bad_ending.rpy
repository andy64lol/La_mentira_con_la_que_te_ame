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

    scene bg parkday at scale_bg
    with fade

    "Yui se aleja. Sus pasos son firmes. Decididos."

    "No te das la vuelta. No quieres verla irse."

    "Pero escuchas. Cada paso. Cada distancia que crece entre ustedes."

    "Cuando finalmente miras, ya no está ahí."

    scene black
    with fade

    "Esa noche, no puedes dormir."

    scene bg housebedroomnight at scale_bg
    with fade

    "Estás solo en tu cuarto. Las estrellas brillan afuera."

    "Pero todo se siente oscuro."

    "¿Por qué dijiste eso? ¿Por qué la dejaste ir?"

    "Las preguntas te torturan. Pero no hay respuestas."

    "Solo el silencio de una amistad que acabas de destruir."

    scene bg schoolhallway at scale_bg
    with fade

    "Los días siguientes son un infierno."

    "Yui está en la escuela, pero te ignora completamente."

    "No te mira. No te habla. No existe para ella."

    "Y tú... tú no sabes qué hacer."

    show yui angry at yuileft
    with dissolve

    "La ves en el pasillo. Con sus amigas. Riendo."

    "Como si nada hubiera pasado. Como si tú no existieras."

    "Pero cuando tus miradas se cruzan, hay algo en sus ojos."

    "Dolor. Traición. Despedida."

    scene black
    with fade

    "Una semana después..."

    scene bg classroom at scale_bg
    with fade

    "Alguien te dice que Yui no vendrá hoy."

    "Que está empacando. Que se va mañana."

    "Tu corazón se detiene."

    "Mañana. Se va mañana."

    "Y tú... tú no has dicho nada. No has hecho nada."

    menu:
        "Ir a su casa":
            jump bad_ending_last_chance
        "Quedarte en casa":
            jump bad_ending_regret

label bad_ending_last_chance:

    scene bg housebedroomyourday at scale_bg
    with fade

    "Corres a su casa. La puerta está abierta."

    "Cajas por todas partes. El vacío de una vida que se desmonta."

    "Pero Yui no está."

    "Su madre te dice que salió. Que no dijo a dónde."

    "Que se veía triste."

    scene bg parkday at scale_bg
    with fade

    "Corres al parque. El lugar donde solían ir."

    "Donde todo comenzó. Donde todo terminó."

    "Pero el parque está vacío."

    "Las risas de los niños suenan lejanas. Irreales."

    "Yui no está aquí."

    "No está en ningún lado."

    jump bad_ending_departure

label bad_ending_regret:

    scene bg housebedroomnight at scale_bg
    with fade

    "Te quedas en casa. Mirando el techo."

    "Preguntándote qué habría pasado si hubieras hablado."

    "Si hubieras dicho algo diferente."

    "Si hubieras luchado."

    "Pero no lo hiciste."

    "Y ahora es tarde."

    jump bad_ending_departure

label bad_ending_departure:

    scene black
    with fade

    "El día de su partida llega."

    "No vas a despedirte. No te invitó. No espera que vayas."

    "Pero estás despierto. Desde antes del amanecer."

    "Mirando el cielo. Pensando en el avión que la llevará lejos."

    scene bg trainstation at scale_bg
    with fade

    "Vas a la estación de tren. No sabes por qué."

    "Quizás esperas verla. Quizás esperas un milagro."

    "Pero el tren ya se fue."

    show yui worriedsadtalk at yuipos
    with dissolve

    "O eso crees."

    "Pero entonces la ves."

    "Está ahí, en el andén. Sola."

    "Como si te estuviera esperando."

    Yui "Sabía que vendrías."

    show yui serioustalk at yuipos

    Yui "O al menos... esperaba que vendrías."

    show yui worriedsadtalk at yuipos

    Yui "Pero no digas nada. Por favor."

    show yui serioustalk at yuipos

    Yui "No quiero oírlo ahora. Es tarde."

    show yui angry at yuipos

    Yui "Demasiado tarde."

    show yui worriedsadtalk at yuipos

    Yui "Adiós."

    hide yui
    with moveoutright

    "Se sube al tren. No te mira."

    "El tren se aleja. Llevándose a Yui."

    "Llevándose todo lo que pudieron haber sido."

    scene black
    with fade

    "Meses después..."

    scene bg housebedroomnight at scale_bg
    with fade

    "Estás solo en tu cuarto."

    "Las mañanas son silenciosas. Vacías."

    "A veces, medio dormido, escuchas su voz."

    "'¡Oye! ¡Despierta!'"

    "Pero no es real. Solo un recuerdo. Una fantasía."

    "Yui se fue. Y no hay segundas oportunidades."

    "Aprendiste eso de la manera más difícil."

    scene black
    with fade

    "FINAL MALO: La mentira completa"

    "Yui cumplió su palabra. Se fue sin despedirse."

    "Nunca supiste la verdad. Nunca supiste que te amaba."

    "A veces el silencio es la peor mentira de todas."

    "Gracias por jugar."

    return
