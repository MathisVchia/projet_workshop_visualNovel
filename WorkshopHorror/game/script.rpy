# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define J = Character('Jason', color="#ffffff")
define J_think = Character(kind = J, what_italic = True, what_xalign = 0.5, what_layout ='subtitle')
define J_shout = Character(kind = J, what_bold = True, what_size = 30) # Kind permet de copier un style de perso, perso qui crie
define K = Character('Kim', color= "#ff00bf")
define B = Character('Bryan', color= "#ff0000")
define A = Character('Anna', color= "#2600ff")
define N = Character('Nancy', color= "#f9fd15")
define I = Character('Voix inconnue', color= "#48ff00")

define E = Character('', color= "#ffdabc", what_italic = True) # bruitage et environnement


# Le jeu commence ici
label start:

    # Mettre toutes les variables ici
    $ relationJtoK = 0
    $ relationJtoB = 0
    $ relationJtoA = 0
    $ relationJtoN = 50
    $ relationKtoB = 0
    $ relationKtoA = 0
    $ relationKtoN = 0
    $ relationBtoA = 0
    $ relationBtoN = 0
    $ relationAtoN = 0

    $ lifeJ = 100
    $ lifeK = 100
    $ lifeB = 100
    $ lifeA = 100
    $ lifeN = 100

      

    J_think "Aujourd'hui, c'est le grand jour. Il ne me reste plus beaucoup de temps avant de devoir partir, et il ne faut pas que je gâche la soirée, sinon Kim ne me le pardonnera jamais."
    J_think " Depuis le temps qu'il s'embête à tout bien organiser, la moindre petite faute de goût pourrait me coûter très cher. Kim et moi, on se connait depuis quelques années maintenant, je sais comment il réagira. Surtout depuis la dispute d’hier."



    scene chambre_jason
    show jason_normal:
        xalign 0.2
        yalign -0.5
    with dissolve

    J "Ce soir, je vais enfin revoir Bryan, mon meilleur ami. Ça fait plusieurs semaines que je ne l’ai pas revu. Je crois que Kim a décidé d’inviter Anna aussi. J’espère que tout va bien se passer entre eux."
    J "Bon, je dois finir de me préparer avant d’arriver en retard. Je ne suis pas très convaincu de ma tenue mais tant pis, pas de temps à perdre."
    
    E "*Bzzzz Bzzzz*"

    # son de vibration, clic sur le portable mis en évidence en arrière plan

    # ouverture interface portable OU fondu au noir avec scène scindé, chaque perso sur son téléphone

    show nancy_normal:
        xalign 0.8
        yalign -0.5
    with dissolve

    N "Hey hey hey, comment tu vas ?"
    J "Ouhla, ça va et toi ? Qu'est-ce qui t'arrives ?"
    N "Ouais ça va, rien, je voulais juste t'appeler parce que je sors de chez le psy, j'avais rendez_vous cet après-midi..."
    J "Déjà ? Ton dernier rendez-vous était il y a à peine quelques semaines, pourquoi voulait-il te revoir si vite ?"
    N "Honnêtement je n'ai pas compris pourquoi mais mes parents ont insistés pour que j'y aille alors que... merde... ça fait je ne sais combien de mois maintenant, il faut qu'ils passent à autre chose."

    menu:
        "Lui conseiller de continuer son traitement ou de l'arrêter ?"
        "Continuer":
            jump continuer
        "Arrêter":
            jump arreter

    label continuer:
        J "Hé, s'ils sentent que tu as besoin de continuer ton traitement, il faut que tu leur fasse confiance Nancy..."
        J "Ça ne va pas durer, tu vas y arriver. Dans le pire des cas, vas-y et raconte lui de la merde, ils seront contents."
        N "Tu crois ?"
        J "Fais moi confiance Nan'..."
        N "..."

        jump suite
        
    label arreter:
        J "Après tu sais, j'ai l'impression que tu vas mieux quand même."
        N "Tu trouves aussi ? J'avais peur de me tromper mais je me sens bien en ce moment."
        J "Bah, tu es un peu plus souriante, tu as vraiment l'air d'être plus heureuse tu sais ?"
        N "Merci ! Je suis contente que tu le remarques ! Tu es le premier à me le dire, ça fait du bien !"
        J "Tu vas continuer de suivre le traitement ?"
        N "Pourquoi, tu crois que je devrais l'arrêter ?"
        J "Je ne sais pas, mais je te vois guérir, tu pourrais peut-être en parler à tes parents."



    label suite:
        N "... Hé dis-moi, ça te dit de sortir ce soir ? J'ai envie de prolonger l'euphorie pour la soirée avant que ça retombe..."
        J "Oh, euh, je ne vais pas pouvoir ce soir. Je dois aller chez Kim, on va enfin se voir avec les autres, depuis le temps."
        N "Les autres ?"
        J "Ouais, Bryan et Anna, même si je ne comprends pas pourquoi on insiste à les faire venir ensemble vu l'ambiance qu'ils foutent les deux."
        N "Ouais, non... si c'est pour continuer de me faire insulter en boucle, je vais éviter de venir ce soir..."

        menu :
            "En parler":
                jump en_parler

            "Être désolé":
                jump desole

            "Lui dire que ça va passer":
                jump passer

    label en_parler:
        J "Attends, Kim et Anna continuent de te faire chier ? Putain, Kim m'avait promis de te laisser tranquille."
        N "Ouais, bah, comme quoi, on ne peut pas lui faire confiance..."
        J "Putain... Bon, je vais essayer de lui en parler ce soir, je ne comprends pas ce qu'il se passe entre vous mais bordel ! Il faut que vous arriviez à vous parler un jour toutes les deux."
        N "Je ne suis pas sûre que ça change grand chose, c'est trop tard maintenant."
        J "Mais non, ça va aller tu verras. Laisse-moi faire, je vais lui en parler. Toi, ne pense plus à ça. Profite de ta soirée, tu le mérites."

        jump suite2

    label desole:
        J "Putain, je suis désolé que tu aies à vivre ça, elle m'avait promis d'arrêter pourtant…"
        N "Mouais, bah si elle était du genre à respecter ses promesses, on le saurait…"
        J "Arrête Nancy..."

        jump suite2

    label passer:
        J "Arrête, tu sais qu'elle dit ça pour rigoler..."
        N "Pardon ? Tu ne l'a jamais vu quand elle est avec Anna, ce n'est pas juste pour rigoler Jason."
        J "Non mais ce n'est pas ce que je voulais dire... Juste, ne prends pas à cœur tout ce qu'elle te dit, elle veut juste s'amuser avec toi, c'est toi qui empire la situation..."
        N "Tu sais quoi, va te faire foutre Jay ! Il faut que tu ouvres les yeux sur elle, ou elle va finir par t'avoir toi aussi."
        J "Ouais, ouais... Je sais… Bon, tu sais quoi ?"

        $ relationJtoN -= 10



    label suite2:
        J "Je vais devoir te laisser Nancy, sinon je vais être en retard. Ça m'a fait plaisir de t'avoir ce soir."
        N "Ouais moi aussi... Bisous !"

        hide nancy_normal with dissolve

        ""

        #$ testVar = True
        
        #if testVar == True:
        


    return # Quitte la partie, partie terminée