label revelation:

    show yui worriedsadtalk at yuipos

    Yui "En dos semanas. Mi padre consiguió trabajo en el extranjero."

    show yui serioustalk at yuipos

    Yui "No quería decírtelo. No quería ver tu cara cuando..."

    show yui worriedsadtalk at yuipos

    Yui "Cuando te diera la noticia."

    menu:
        "¿Y nosotros?":
            jump emotional_confrontation
        "Voy a extrañarte":
            $ yui_affection += 2
            jump emotional_confrontation

label emotional_confrontation:

    show yui angry at yuipos
    with dissolve

    Yui "¡No digas eso!"

    show yui angrytalk at yuipos

    Yui "No quiero que me extrañes. No quiero que..."

    show yui worriedsadtalk at yuipos

    Yui "No quiero que sufras cuando me vaya."

    show yui serioustalk at yuipos

    Yui "Así que... así que he decidido algo."

    show yui angry at yuipos

    Yui "Voy a alejarme de ti. Ahora. Antes de que sea peor."

    menu push_away_choice:
        "¿Por qué haces esto?":
            jump why_push_away
        "No me dejes":
            jump beg_stay
        "Si eso es lo que quieres...":
            jump accept_distance

label why_push_away:

    show yui angrytalk at yuipos

    Yui "¡Porque no quiero que me recuerdes!"

    show yui worriedsadtalk at yuipos

    Yui "Si te alejo ahora... si te hago odiarme..."

    show yui serioustalk at yuipos

    Yui "Entonces cuando me vaya, no te dolerá."

    menu:
        "Eso no es cierto":
            jump truth_moment
        "Eres una cobarde":
            $ yui_affection -= 1
            jump harsh_truth

label beg_stay:

    show yui worriedsadtalk at yuipos

    Yui "No me pidas eso. No puedo... no puedo decir que no si me lo pides así."

    show yui serioustalk at yuipos

    Yui "Pero tengo que hacerlo. Por los dos."

    menu:
        "Te necesito":
            jump truth_moment
        "Entiendo...":
            jump accept_distance

label accept_distance:

    show yui wtf at yuipos

    Yui "¿Eso es todo? ¿No vas a pelear?"

    show yui angry at yuipos

    Yui "¿No te importa lo suficiente como para discutir?"

    menu:
        "Me importas demasiado para forzarte":
            jump truth_moment
        "Si quieres irte, ve":
            jump bad_ending

label harsh_truth:

    show yui angrytalk at yuipos

    Yui "¡¿Cobarde?! ¡Tú no sabes nada!"

    show yui worriedsadtalk at yuipos

    Yui "He pasado meses llorando por las noches. Meses..."

    show yui serioustalk at yuipos

    Yui "Olvídalo. Esto termina aquí."

    jump bad_ending

label truth_moment:

    show yui worriedsadtalk at yuipos

    Yui "¿Qué quieres que haga? ¿Que te diga la verdad?"

    show yui serioustalk at yuipos

    Yui "La verdad es que..."

    show yui worriedsadtalk at yuipos

    Yui "La verdad es que te amo."

    show yui serioustalk at yuipos

    Yui "Te amo y me voy. Y no puedo soportar la idea de dejarte atrás."

    show yui worriedsadtalk at yuipos

    Yui "Así que prefiero que me odies. Es más fácil."

    menu final_choice:
        "Yo también te amo":
            if yui_affection >= 3:
                jump true_ending
            else:
                jump good_ending
        "Siempre serás mi amiga":
            jump neutral_ending
        "Entonces adiós":
            jump bad_ending
