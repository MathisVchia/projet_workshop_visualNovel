# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define J = Character('Jason', color="#ffffff")
define J_think = Character(kind = J, what_italic = True, what_xalign = 0.5, what_layout ='subtitle')
define J_shout = Character(kind = J, what_bold = True, what_size = 30) # Kind permet de copier un style de perso, perso qui crie
define K = Character('Kim', color= "#ff00bf")
define B = Character('Bryan', color= "#ff0000")
define B_murmure = Character(kind = B, what_size = 10)
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

    play music "audio/Music/Prologue1.mp3" loop

    J_think "Aujourd'hui, c'est le grand jour. Il ne me reste plus beaucoup de temps avant de devoir partir, et il ne faut pas que je gâche la soirée, sinon Kim ne me le pardonnera jamais."
    J_think " Depuis le temps qu'elle s'embête à tout bien organiser, la moindre petite faute de goût pourrait me coûter très cher."
    J_think "On se connait déjà depuis plusieurs années, et je n'ai pas envie de savoir comment elle réagira... Surtout depuis la dispute d’hier."



    scene chambre_jason

    J "Ca sera l'occasion de revoir Bryan. Ça fait plusieurs semaines que je ne l’ai pas revu. Je crois que Kim a décidé d’inviter Anna aussi. J’espère que tout va bien se passer malgré leurs différents."
    J "Bon, je dois finir de me préparer avant d’arriver en retard. Je ne suis pas très convaincu de ma tenue mais tant pis, plus de temps à perdre."
    
    
    play sound "audio/Sounds/Phone Ringing.mp3" 
    
    # son de vibration, clic sur le portable mis en évidence en arrière plan

    # ouverture interface portable OU fondu au noir avec scène scindé, chaque perso sur son téléphone

    show nancy_normal:
        xalign 1.5 yalign -0.5
        linear 0.8 xalign 0.9

    N "Hey hey hey, comment tu vas ?"
    J "Salut Nancy, ça va et toi ?"
    N "Ouais ça va, je voulais juste t'appeler parce que je sors de chez le psy, j'avais rendez-vous cet après-midi..."
    J "Déjà ? Ton dernier rendez-vous était il y a à peine deux semaines, pourquoi voulait-il te revoir si vite ?"
    N "Honnêtement je n'ai pas compris pourquoi mais mes parents ont insisté pour que je le voie alors que..."
    N "..."
    N "Ca fait je ne sais combien de mois maintenant, il faut qu'ils passent à autre chose."

    menu:
        "Lui conseiller de continuer son traitement ou de l'arrêter ?"
        "Continuer":
            jump continuer
        "Arrêter":
            jump arreter

    label continuer:
        J "Hé, s'ils sentent que tu as besoin de continuer ton traitement, il faut que tu leur fasse confiance Nancy..."
        J "Ça ne va pas durer, tu vas y arriver. Dans le pire des cas, vas-y et raconte n'importe quoi, ils seront contents."
        N "Tu crois ?"
        J "Fais moi confiance Nan'..."
        N "..."

        jump suite
        
    label arreter:
        J "Après tu sais, j'ai vraiment l'impression que tu vas mieux."
        N "Tu trouves aussi ? J'avais peur de me tromper mais je me sens bien en ce moment."
        J "Bah, tu es plus souriante, tu as l'air de revivre."
        N "Merci ! Je suis contente que tu le remarques ! Tu es le premier à me le dire, ça fait du bien !"
        J "Tu vas continuer de suivre le traitement ?"
        N "Pourquoi, tu crois que je devrais arrêter ?"
        J "Je ne sais pas, mais je te vois guérir, tu pourrais peut-être en parler à tes parents."

    label suite:
        N "... Hé dis-moi, ça te dit de sortir ce soir ? J'ai envie de prolonger l'euphorie pour la soirée avant que ça retombe..."
        J "Oh, euh, je ne vais pas pouvoir ce soir. Je dois aller chez Kim, on va enfin se voir avec les autres, depuis le temps."
        N "Les autres ?"
        J "Ouais, Bryan et Anna, même si je ne comprends pas pourquoi on insiste à les faire venir ensemble vu l'ambiance que ça donne."
        N "Ouais, non... si c'est pour être avec eux, je vais éviter de venir ce soir..."

        menu :
            "En parler":
                jump en_parler

            "Être désolé":
                jump desole

            "Lui dire que ça va passer":
                jump passer

    label en_parler:
        J "Attends, Kim et Anna continuent de te faire chier ? J'avais fait jurer à Kim de te laisser tranquille. Merde."
        N "Ouais, bah, comme quoi, on ne peut pas lui faire confiance..."
        J "Bon, je vais essayer de lui en parler ce soir, je ne comprends pas ce qu'il se passe entre vous, mais il faut que vous arriviez à vous parler un jour toutes les trois."
        N "Je ne suis pas sûre que ça change grand chose, c'est trop tard maintenant."
        J "Je vais gérer ça avec eux. Fais-moi confiance, et ne pense plus à ça. Profite de ta soirée, tu le mérites."

        jump suite2

    label desole:
        J "Je suis désolé que tu aies à vivre ça, Kim m'avait promis d'arrêter pourtant…"
        N "Mouais, bah si elle était du genre à respecter ses promesses, on le saurait…"
        J "Arrête Nancy..."

        jump suite2

    label passer:
        J "Arrête, tu sais que Kim disait ça pour rigoler..."
        N "Pardon ? Tu ne l'a jamais vue quand elle est avec Anna, ce n'est pas 'juste pour rigoler' Jason."
        J "Non mais ce n'est pas ce que je voulais dire... Juste, ne prends pas à cœur tout ce qu'elle te dit, elle veut juste s'amuser avec toi, c'est toi qui empires la situation..."
        N "Tu sais quoi, va te faire foutre Jay ! Il faut que tu ouvres les yeux sur elle, ou elle va finir par t'avoir toi aussi."
        J "Ouais, ouais... Je sais..."

        $ relationJtoN -= 10



    label suite2:
        J "Je vais devoir te laisser Nancy, sinon je vais être en retard. Ça m'a fait plaisir de t'entendre ce soir."
        N "Ouais... Moi aussi..."
        J "Bisous !"

        play sound "audio/Sounds/Phone off.mp3"

        hide nancy_normal with dissolve


        J_think "Bon, il ne me reste plus beaucoup de temps. Kim m’a donné sa liste, si j’oublie le moindre objet, c’est un coup à ce que la soirée parte en vrille. J’espère juste que Bryan et Anna arriveront à se tenir."


        # objet = 0
        # Séquence point and clic chambre Jason

        # De quoi j'ai besoin déjà ?
        # Affichage liste d'objet

        # Possibilité de partir à tout moment de la séquence, 3 répliques selon le nb d'objet pris
        
        #if objet == 0 :
            # J_think "Hé merde, j'espère que Kim ne m'en voudras pas de enir les mains vides..."
        #elif objet < 6 :
            # J_think "Bon, au moins je n'arriverai pas les mains vides !"
        
        #elif objet == 6 :
            # J_think "Ok, je pense que je suis bon pour ce soir !"

        J_think "Oulah, il est déjà l'heure! Si je me dépêche assez, j'ai moyen d'arriver à temps'."

        scene fenetre_kim
        with dissolve

        E "Depuis l'extérieur, les fenêtres de la maison de Kim semblent éclairées. au loin, quelques ombres dansent sur les murs du salon. La soirée a déjà commencé."
        J_think "Merde, je suis le dernier. J'espère que je n'ai pas raté grand chose."

        play sound "audio/Sounds/Carillon.mp3"
        E "Ding dong"
        play music "audio/Music/Soiree1.mp3" loop fadeout 1

        scene entree_kim
        show kim_content:
            yalign -0.5


        K "Ah bah enfin te voilà ! T'es le dernier à arriver, on a cru que tu allais oublier la soirée !"
        J "Désolé, j'ai pris trop de temps sur le chemin, le bus a fait un détour."
        K "Ne t'en fais pas va ! Alors, tu as pensé à ce que tu devais ramener ?"

        #if objet == 0 :
            #jump mainsvides
        #elif objet < 6 :
            #jump moitie
        #elif objet == 6 :
            #jump tout

        #label mainsvides : 
            #J "Merde, je suis déoslé j'ai complètement oublié ce que tu voulais que je prenne..."
            #K "Tu te moques de moi là j'espère ? Non mais, tu espères vraiment me faire croire que tu as complètement oublié et tu ne m'as même pas envoyé un message pour me prévenir ?"
            #K "Jay... Je... Tu m'énerves ! Viens, sinon je vais finir par t'étriper avant même que tu rentres..."

            #jump suite3
        
        #label moitie :
            #J "Euh non, je crois qu'il fallait que je prenne un truc en plus, mais je ne me souviens plus quoi."
            #K "Oh t'es lourd ! Je n'aais pas prévu que tu allais oublier de ramener les affaires de ce soir. Il va nous manquer de quoi passer la soirée !"
            #K "Bon viens, sinon en plus d'etre con tu vas vraiment être en retard."

            #jump suite3

        #label tout :
            #J "Ouais, j'ai pensé à ce que tu m'avais dit, normalement je n'ai rien oublié."
            #K "Incroyable ! Je ne pensais pas que tu te souviendrais de tout. T'es vraiment parfait mon coeur."
            #K "Bon, allons dans le salon, on était en train de jouer et... Ne t'inquiètes pas, j'ai une petite surprise pour toi après la soirée, une petite récompense..."
            #E "Un clien d'oeil plus tard, Kim invite Jason à le suivre dans l'appartement où ils retrouvent Bryan et Anna autour d'une table de jeu dans le salon."

        scene canape_kim


        label suite3 :
            E "Dans le salon, Bryan et Anna sont tous les deux assis autour d'une  table où s'étaient déjà écoulées quelques bouteilles d'alcool."
            B "Hééééé ! Mais c'est l'autre qui se décide enfin à arriver ! Viens dépêches-toi, je te sers un verre, il faut que tu me rattrapes !"
            A "Tu vas vraiment continuer de boire toute la soirée ? T'es déjà explosé..."
            K "Ouais, s'il te plait, calme toi un peu... Je n'ai pas envie de te récupérer en train de dormir sur le sol parce que tu t'es enquillé trop de verres d'alcool..."
            B "Mais fermez là... Il va falloir qu'on apprenne à vous décoincer un peu, un jour... Pas vrai Jason ?"
            B "Bon d'ailleurs, on était dans un débat, est-ce que tu penses que tu peux compter sur moi en cas de problèmes ou pas ?"
            J "C'est quoi cette question ?"
            A "On s'ennuyait en t'attendant du coup, Kim a décidé de nous lancer une série de questions pour savoir qui on préférait dans le groupe."
            A "On en était à 'Sur qui tu peux compter ?' là."

            menu:
                "Sur qui compter ?"
                "Bryan":
                    jump choix_Bryan
                "Anna":
                    jump choix_Anna
                "Kim":
                    jump choix_Kim
        
        label choix_Bryan:
            J "Elle est nulle la question… Pour moi ça restera toujours Bryan. Il a beau être un peu con, il me colle au train depuis trop longtemps pour que je le laisse de côté."
            B "Ah ! Vous voyez je vous l’avais dit ! Il fait passer la famille avant le coeur !"
            K "Ouais, je vois ça… Je vois surtout qu’il va finir par dormir tout seul ce soir..."
            jump suite4

        label choix_Anna:
            J "En vrai, si je dois choisir entre vous trois… je pense que je prendrai Anna."
            B "Hé ! C’est quoi ce choix de merde là !"
            J "Non mais juste réfléchis un peu : elle est la plus calme, elle est la plus réfléchie d’entre nous, si il y a bien une personne qui peut me sauver le cul sans trembler c’est bien elle !"
            A "Et faut arrêter d’être jaloux Bryan. Elle baisse ta cote, assume-le, il préfère passer par d’autres gens que par toi."
            jump suite4

        label choix_Kim:
            
            J "Non mais ne me posez pas la question, je suis le seul en couple de nous trois. Si je dois appeler quelqu’un entre nous trois, c’est forcément Kim, je sais que je peux lui faire confiance."
            A "Ah ! Tu vois Bryan, c’était évident. Son couple passera toujours devant toi, ne viens pas chialer."
        
        label suite4:
            J "Forcément, elle était trop simple cette question... Vous en avez une autre ?"
            K "On a eu plein tout à l’heure mais on est à court d'idées. Genre par exemple, si jamais on devait vivre pendant une apocalypse, tu penses que lequel d’entre nous finirai par mourir en premier ?"

            menu:
                "Qui mourrait en premier ?"

                "Bryan":
                    jump choix_Bryan2
                "Anna":
                    jump choix_Anna2
                "Kim":
                    jump choix_Kim2

        label choix_Bryan2:
            B "Arrête de me regarder en rigolant, tu sais très bien que je survivrai longtemps !"
            J "Je suis désolé mais celui d’entre nous qui durera le moins longtemps, c’est toi."
            B "Mais n’importe quoi ! Je suis le seul qui fait du sport entre nous, vous allez être tellement lent que vous allez crever en moins de deux."
            B "Regarde Anna, même réfléchir ça lui prend du temps alors je te dis pas si il faut qu’elle court !"
            A "Hé ! Va te faire ! Assume-le, t’es juste trop con tu tomberai dans tous les pièges"
            B "Humpf… Je savais que ça allait être un jeu de merde de toute manière..."

            jump suite5

        label choix_Anna2:
            J "Bah, écoute..."
            A "Hé, arrête de me fixer comme ça, si il y en a bien une qui peut survivre c’est bien moi !"
            J "Alors oui, mais tu n’es pas assez sportive. Si on se fait attaquer, je pense que celle qui a le moins de chance..."
            A "Sans moi vous ne durerez pas plus de quelques jours."
            B_murmure "Tu parles, sans toi putain on serait tranquille..."
            A "Tu viens de dire quoi là ?"
            K "Bryan laisse-la tranquille un peu, tu veux ?"

            jump suite5
        
        label choix_Kim2:
            J "Si il faut réfléchir en terme de défense, le premier qui se ferait viser en cas d’attaque, c’est Kim. T’as trop l’air sans défense..."
            K "Pardon ? J’ai l’air faible ?"
            J "Non, je dis pas ça. Mais comparé à Bryan, s’il y a bien quelqu’un qui peut paraître moins dangereux, c’est bien toi quoi..."
            B_murmure "Ah c’est marrant, j’aurai plutôt dis Anna avec sa gueule de première de classe..."
            A "Hé mais vas te faire foutre !"
            K "Tu veux que je t’en colle une, voir si je suis si faible que ça ?"
            J "Non mais le prends pas comme ça mon coeur, hé !"

        label suite5:
            J "Vas-y, je change de question avant que ça parte encore plus en couilles. Si l’un d’entre nous était un dangereux psychopathe, vous pensez que ça serait qui ?"
            K "Elle est dure ta question..."

            menu:
                "Qui serait un psychopathe ?"
                "Bryan":
                    jump choix_Bryan3
                "Anna":
                    jump choix_Anna3
                "Kim":
                    jump choix_Kim3

        label choix_Bryan3:
            J "Tu trouves ? Moi je pense que ça pourrait être Bryan, regarde-le c’est le seul qui pourrait avoir assez de force pour..."
            jump suite6

        label choix_Anna3:
            J "Tu trouves ? Moi je pense que ça pourrait être Anna. Regarde-la c’est la seule qui pourrait être assez intelligente pour..."
            jump suite6

        label choix_Kim3:
            J "Tu trouves ? Moi je pense que je te dirai, toi. Entre nous tous, je suis sûr que t’es la plus fourbe, tu pourrais..."


        label suite6:
            play sound "audio/Sounds/Bruit Sourd.mp3"
            B "Vous avez entendu ?"
            A "Quoi ?"
            B "Je ne sais pas, ça vient de l’étage… Kim, tu n’as pas de chat ?"
            K "Non, non… Arrête tu commences à me faire flipper..."
            A "Non mais laisse tomber, regarde tout ce qu’il a bu, il est encore en train d’avoir des hallucinations."
            B "Anna, arrête. Je suis sûr de ce que j’ai entendu..."
            K "Mais c’était quoi, une voix, un bruit de pas..."
            B "Je n’en sais rien..."
    
            menu:
                "Croire Bryan":
                    jump suite6




    return # Quitte la partie, partie terminée