label school_days_pass:

    scene bg classroom at scale_bg
    with fade

    play music "audio/morning.ogg" fadein 2.0

    "Los días pasan demasiado rápido."

    "Cada mañana, Yui te espera en la puerta."

    "Cada almuerzo, comparten comida."

    "Cada tarde, caminan juntos hasta el parque."

    "Es casi como siempre. Casi normal."

    "Pero hay una sombra sobre todo. Una cuenta regresiva silenciosa."

    show yui happynormal at yuileft
    with dissolve

    Yui "¡Oye! ¿Trajiste los apuntes?"

    show yui happytalk at yuileft

    Yui "Me quedé dormida anoche. Estaba... estaba empacando."

    show yui worriedsadtalk at yuileft

    Yui "Hay tantas cosas. Fotos. Regalos. Recuerdos."

    show yui serioustalk at yuileft

    Yui "No sé qué llevarme. No sé qué dejar."

    menu:
        "Llévate lo importante":
            jump important_things
        "Los recuerdos te acompañan":
            $ yui_affection += 1
            jump memories_within

label important_things:

    show yui serioustalk at yuileft

    Yui "¿Lo importante?"

    show yui worriedsadtalk at yuileft

    Yui "Pero todo es importante. Cada cosa tiene una historia."

    show yui serioustalk at yuileft

    Yui "Esta pulsera... me la diste tú. En mi cumpleaños."

    show yui happytalk at yuileft

    Yui "Dijiste que era para que no olvidara quién era."

    show yui happynormal at yuileft

    Yui "Como si pudiera olvidar. Como si pudiera olvidarte."

    jump school_days_continue

label memories_within:

    show yui wtf at yuileft

    Yui "¿En mi corazón?"

    show yui happytalk at yuileft

    Yui "Eso es... eso es muy cursi."

    show yui happynormal at yuileft

    Yui "Pero gracias. Necesitaba escuchar algo cursi hoy."

    show yui serioustalk at yuileft

    Yui "Tienes razón, ¿sabes? No necesito cosas."

    show yui worriedsadtalk at yuileft

    Yui "Necesito... necesito a las personas. A ti."

    jump school_days_continue

label school_days_continue:

    scene bg schoolhallway at scale_bg
    with fade

    "Entre clases, Yui te arrastra al pasillo."

    show yui serioustalk at yuipos
    with dissolve

    Yui "Oye..."

    show yui worriedsadtalk at yuipos

    Yui "¿Puedo preguntarte algo?"

    show yui serioustalk at yuipos

    Yui "¿Alguna vez... alguna vez pensaste en el futuro?"

    show yui worriedsadtalk at yuipos

    Yui "En dónde estarás. En quién serás."

    show yui serioustalk at yuipos

    Yui "¿Pensaste alguna vez que... que yo estaría ahí?"

    menu:
        "Siempre pensé que estarías":
            $ yui_affection += 1
            jump always_thought
        "No me imagino sin ti":
            jump always_thought
        "El futuro es incierto":
            jump uncertain_future

label always_thought:

    show yui happytalk at yuipos

    Yui "¿En serio?"

    show yui happynormal at yuipos

    Yui "Yo también. Siempre pensé... pensé que seríamos viejitos juntos."

    show yui serioustalk at yuipos

    Yui "Que nos burlaríamos de nuestros nietos. Que recordaríamos estos días."

    show yui worriedsadtalk at yuipos

    Yui "Pero ahora... ahora no sé qué pensar."

    show yui serioustalk at yuipos

    Yui "El futuro que imaginé... se desvanece."

    jump final_school_day

label uncertain_future:

    show yui wtf at yuipos

    Yui "¿Incierto?"

    show yui angry at yuipos

    Yui "¡No quiero incertidumbre! ¡Quiero certeza!"

    show yui worriedsadtalk at yuipos

    Yui "Quiero saber que... que aunque me vaya, algo permanece."

    show yui serioustalk at yuipos

    Yui "Que no seré solo un recuerdo. Que no seré olvidada."

    show yui worriedsadtalk at yuipos

    Yui "Prométeme que no me olvidarás. Aunque sea eso."

    menu:
        "Nunca te olvidaré":
            $ yui_affection += 1
            jump promise_remember
        "Eres parte de mí":
            jump promise_remember

label promise_remember:

    show yui happytalk at yuipos

    Yui "Gracias."

    show yui happynormal at yuipos

    Yui "Eso... eso me da fuerzas."

    jump final_school_day

label final_school_day:

    scene black
    with fade

    "El último día de escuela llega."

    "Una semana antes de que Yui se vaya."

    scene bg classroom at scale_bg
    with fade

    "Todo el mundo está emocionado por las vacaciones."

    "Pero tú solo puedes pensar en que es el último día con Yui."

    "El último día de clases juntos."

    show yui serioustalk at yuiright
    with dissolve

    Yui "Oye..."

    show yui worriedsadtalk at yuiright

    Yui "Después de clases... ¿puedes venir al parque?"

    show yui serioustalk at yuiright

    Yui "Necesito... necesito decirte algo importante."

    show yui worriedsadtalk at yuiright

    Yui "Algo que he guardado demasiado tiempo."

    "Asientes. Tu corazón late con fuerza."

    "¿Qué podría ser? ¿Algo bueno? ¿Algo malo?"

    scene black
    with fade

    "Después de clases..."

    jump revelation
