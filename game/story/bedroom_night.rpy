label bedroom_night:

    scene black
    with fade

    stop music fadeout 2.0

    "La noche cae. Las estrellas aparecen una a una."

    "Pero tú no puedes dormir."

    scene bg housebedroomnight at scale_bg
    with fade

    play music "audio/sad.ogg" fadein 3.0

    "Yui se va. En dos semanas."

    "Diez años de amistad. Diez años de mañanas juntos."

    "¿Cómo se supone que debo despertarme sin ella gritándome?"

    "Recuerdas el primer día que la conociste."

    "Tenía coletas azules y una sonrisa que iluminaba todo el cuarto."

    "Dijo que sería tu amiga para siempre."

    "¿Dónde quedó ese 'para siempre'?"

    "Miras tu teléfono. Hay un mensaje de Yui."

    "'¿Duermes?'"

    "Escribes una respuesta, la borras, la vuelves a escribir."

    menu:
        "No puedo dormir":
            jump night_message_continue
        "Estoy pensando en ti":
            $ yui_affection += 1
            jump night_message_continue

label night_message_continue:

    "Esperas su respuesta. Los minutos pasan como horas."

    "Finalmente, el teléfono vibra."

    "'Yo tampoco.'"

    "'¿Puedo ir a tu casa?'"

    menu:
        "Claro, ven":
            jump yui_visits_night
        "Es tarde, deberías dormir":
            jump yui_stays_home

label yui_visits_night:

    "Veinte minutos después, escuchas una piedra contra tu ventana."

    "La señal de siempre."

    show yui worriedsadtalk at yuipos
    with dissolve

    Yui "¿Me dejas entrar? Hice escalar la cerca."

    show yui serioustalk at yuipos

    Yui "No quería que mis padres supieran. Están... están empacando todo."

    show yui worriedsadtalk at yuipos

    Yui "El cuarto está lleno de cajas. No puedo dormir ahí."

    show yui serioustalk at yuipos

    Yui "No puedo dormir pensando que... que todo está terminando."

    menu:
        "Quédate aquí esta noche":
            jump night_together
        "Hablemos un rato":
            jump night_talk

label yui_stays_home:

    "Escribes que es tarde, que debería descansar."

    "La respuesta tarda en llegar."

    "'Tienes razón. Buenas noches.'"

    "Pero no puedes dormir. La culpa te carcome."

    "¿Deberías haberla dejado venir?"

    "¿Deberías haber dicho algo más?"

    "Pasas la noche dando vueltas en la cama, preguntándote qué está haciendo ella."

    "Si también está despierta. Si también está sufriendo."

    "Solo."

    jump bedroom_evening

label night_together:

    $ yui_affection += 1

    show yui happytalk at yuipos

    Yui "¿En serio? ¿No te importa?"

    show yui happynormal at yuipos

    Yui "Eres el único que... que me hace sentir que todo estará bien."

    show yui serioustalk at yuipos

    Yui "Aunque sé que no estará bien. Aunque sé que me voy."

    show yui worriedsadtalk at yuipos

    Yui "Quiero quedarme aquí. Contigo. Aunque sea solo esta noche."

    "Yui se acuesta en el suelo, cerca de tu cama."

    show yui happynormal at yuipos

    Yui "Buenas noches, idiota."

    show yui happytalk at yuipos

    Yui "Gracias por dejarme quedar."

    scene black
    with fade

    "Duermes mejor que en semanas."

    "Sabiendo que ella está ahí. Cerca."

    jump bedroom_evening

label night_talk:

    show yui serioustalk at yuipos

    Yui "¿De qué quieres hablar?"

    show yui worriedsadtalk at yuipos

    Yui "¿De cómo me voy? ¿De cómo todo termina?"

    show yui serioustalk at yuipos

    Yui "No quiero hablar de eso. No quiero pensar en eso."

    show yui worriedsadtalk at yuipos

    Yui "Quiero hablar de... de cuando éramos niños."

    show yui happytalk at yuipos

    Yui "¿Recuerdas cuando construimos esa casita en el árbol?"

    show yui happynormal at yuipos

    Yui "Dijiste que sería nuestro castillo. Que viviríamos ahí para siempre."

    show yui serioustalk at yuipos

    Yui "Eres un tonto. Un tonto que hace promesas que no puede cumplir."

    show yui worriedsadtalk at yuipos

    Yui "Pero... pero gracias por intentarlo."

    "Hablan hasta tarde. Recuerdos, risas, algunas lágrimas."

    "Cuando Yui se va, el amanecer ya asoma."

    jump bedroom_evening
