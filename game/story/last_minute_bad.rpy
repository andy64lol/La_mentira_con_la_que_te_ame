label last_minute_bad_ending:

    stop music fadeout 1.0
    play music "audio/sad.ogg" fadein 2.0

    show yui wtf at yuipos

    Yui "¿Qué... qué acabas de decir?"

    show yui angry at yuipos

    Yui "¿Ahora? ¿Lo dices AHORA?"

    show yui angrytalk at yuipos

    Yui "¡He pasado meses sufriendo! ¡Meses intentando protegerte de esto!"

    show yui worriedsadtalk at yuipos

    Yui "Y ahora... ahora que finalmente acepté que tengo que irme..."

    show yui angrytalk at yuipos

    Yui "¿Cómo puedes decirme que me amas? ¿Cómo puedes hacerme esto?"

    menu:
        "Lo siento, no quise...":
            jump last_minute_bad_continue
        "Es la verdad":
            jump last_minute_bad_continue

label last_minute_bad_continue:

    show yui serioustalk at yuipos

    Yui "La verdad..."

    show yui worriedsadtalk at yuipos

    Yui "La verdad es que ya es tarde. Demasiado tarde."

    show yui serioustalk at yuipos

    Yui "Mi familia ya está en el aeropuerto. Mi vuelo sale en tres horas."

    show yui worriedsadtalk at yuipos

    Yui "No hay tiempo para nada. Ni siquiera para despedirnos como deberíamos."

    show yui angry at yuipos

    Yui "¿Entiendes? Tu confesión... solo hace que todo sea más difícil."

    show yui worriedsadtalk at yuipos

    Yui "Si me hubieras dicho esto antes... si hubiéramos tenido tiempo..."

    show yui serioustalk at yuipos

    Yui "Pero ahora... ahora solo me estás rompiendo el corazón dos veces."

    show yui worriedsadtalk at yuipos

    Yui "Una por irme. Y otra por saber que podríamos haber tenido algo..."

    show yui serioustalk at yuipos

    Yui "Si tan solo hubieras hablado antes."

    scene bg housebedroomnight at scale_bg
    with fade

    "Yui se va del parque. No la detienes."

    "¿Qué podrías decir? ¿Que lo sientes? ¿Que desearías haber hablado antes?"

    "Todo suena vacío ahora."

    "Estás solo en tu cuarto. Mirando el techo."

    "Tres horas. En tres horas, ella estará en un avión."

    "Y tú... tú solo tienes arrepentimiento."

    scene black
    with fade

    "Dos horas después..."

    scene bg housebedroomyourday at scale_bg
    with fade

    "No puedes quedarte quieto."

    "Corres por la casa. Buscas algo. Cualquier cosa."

    "Una foto. Una carta. Alguna prueba de lo que pudieron ser."

    "Pero no hay nada. Solo recuerdos. Solo 'qué hubiera pasado'."

    menu:
        "Ir al aeropuerto":
            jump last_minute_bad_airport_attempt
        "Quedarte en casa":
            jump last_minute_bad_stay_home

label last_minute_bad_airport_attempt:

    scene bg trainstation at scale_bg
    with fade

    "Corres a la estación. El tren está a punto de salir."

    "Subes. El corazón te late en el pecho."

    "Cada minuto es una eternidad. Cada parada, una tortura."

    "Finalmente, llegas al aeropuerto."

    "Pero..."

    show yui worriedsadtalk at yuipos
    with dissolve

    "La ves. Está en la puerta de embarque. Con su familia."

    Yui "¿Qué haces aquí?"

    show yui serioustalk at yuipos

    Yui "Te dije que no vinieras. Que no había tiempo."

    show yui worriedsadtalk at yuipos

    Yui "¿Por qué haces esto más difícil?"

    menu:
        "Quería verte una última vez":
            jump last_minute_bad_final_words
        "No puedo dejarte ir así":
            jump last_minute_bad_final_words

label last_minute_bad_final_words:

    show yui serioustalk at yuipos

    Yui "No... no digas eso."

    show yui worriedsadtalk at yuipos

    Yui "Si dices eso... si me miras así... no podré irme."

    show yui serioustalk at yuipos

    Yui "Y debo irme. Mi familia me espera. Mi futuro me espera."

    show yui worriedsadtalk at yuipos

    Yui "Adiós. Por favor... olvídame."

    hide yui
    with moveoutright

    "Se va. No te mira."

    "El altavoz anuncia el vuelo. La puerta se cierra."

    "Y ella... ella se va."

    jump last_minute_bad_ending_final

label last_minute_bad_stay_home:

    scene bg housebedroomnight at scale_bg
    with fade

    "Te quedas en casa. Mirando el techo."

    "Cada minuto que pasa es un minuto más cerca de su partida."

    "Cada minuto es un minuto que podrías haber estado con ella."

    "Pero no lo estás."

    "Porque tuviste miedo. Porque esperaste demasiado."

    "Y ahora... ahora es tarde."

    jump last_minute_bad_ending_final

label last_minute_bad_ending_final:

    scene black
    with fade

    "Un mes después..."

    scene bg housebedroomnight at scale_bg
    with fade

    "Estás solo en tu cuarto."

    "Las mañanas son silenciosas. Vacías."

    "A veces, cuando estás medio dormido, escuchas su voz."

    "'¡Oye! ¡Despierta!'"

    "Pero no es real. Solo un recuerdo."

    "Yui se fue. Y no hay segundas oportunidades."

    "Aprendiste eso de la manera más difícil."

    scene bg parkday at scale_bg
    with fade

    "Vuelves al parque. Al lugar donde todo terminó."

    "El sol brilla. Los niños juegan."

    "Todo es igual. Pero todo es diferente."

    "Porque ella no está."

    "Y nunca estará."

    scene black
    with fade

    "FINAL MALO: Confesión de último momento fallida"

    "El tiempo no espera por nadie. Ni siquiera por el amor."

    "A veces, el momento perfecto ya pasó. Y lo único que queda es la pregunta..."

    "¿Qué habría pasado si hubieras hablado antes?"

    "Gracias por jugar."

    return
