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
    $ relationJ = 0
    $ relationK = 0
    $ relationB = 0
    $ relationA = 0
    $ relationN = 0
    $ relationJtoK = 0
    $ relationJtoB = 0
    $ relationJtoA = 0
    $ relationJtoN = 0
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

    

    J_think "Aujourd'hui, c'est le grand jour. Debout dans la salle de bain, je continue de me préparer. Il ne faut pas que je gâche la soirée, sinon Kim ne me le pardonnera jamais."
    J_think "Depuis le temps qu'il s'embête à tout bien organiser, la moindre petite faute de goût va me coûter très cher. Kim et moi, on se connait depuis quelques années maintenant, je sais comment il réagira. Surtout depuis notre dispute de la veille."

    scene chambre_jason
    show jason_normal:
        #size (1200,1300)
        xalign 0.5
        yalign 0.25
    with dissolve
    J "Ce soir, je vais enfin revoir Bryan, mon meilleur ami. Ça fait plusieurs semaines que je ne l’ai pas vu. Je crois que Kim a décidé d’inviter Anna aussi. J’espère que tout va bien se passer entre eux."

    J "Bon, je dois finir de me préparer avant d’arriver en retard. Je ne suis pas très convaincue de ma tenue mais tant pis, pas de temps à perdre."
    
    E "Bzzzz Bzzzz"
    
    
    """show lieuIntro
    with dissolve
    show J
    with dissolve"""

    menu:
            J "Que faire ?"
            "Manger":
                jump manger
            "Dormir":
                jump dormir







# Partie test 
    label manger:
        J "Miam miam !"
        $ testVar = True
        
        jump done
    
    label dormir:
        J "Zzzzz"
        jump done

    label done:
        J "Partons maintenant"

        if testVar == True:
            J "OK j'ai bien mangé, maintenant on avance"
        


    return # Quitte la partie, partie terminée
