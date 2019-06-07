***************
Solitaire, jeux de plateau
***************

..  admonition:: lecture
    :class: important

    TigerJython : http://www.tigerjython.ch/franz/index.php?inhalt_links=navigation.inc.php&inhalt_mitte=gamegrid/gridgames.inc.php


Objectifs
=========

Cette partie apporte un complément au cours TigerJython par le biais d'une
analyse de code, compétence essentielle pour bien appréhender l'oral de BAC.

Code à analyser
===============

..  code-block:: python
    :linenos:

    from gamegrid import *

    def checkGameOver():
        global isGameOver
        marbles = getActors() # get remaining marbles
        if len(marbles) == 1:
            setStatusText("Game over. You won.")
            isGameOver = True
        else:
            # check if there are any valid moves left
            if not isMovePossible():
               setStatusText("Game over. You lost. (No valid moves available)")
               isGameOver = True

    def isMovePossible():
       for a in getActors():  # run over all remaining marbles
            for x in range(7): # run over all holes
                for y in range(7):
                    loc = Location(x, y)
                    if getOneActorAt(loc) == None and \
                      getRemoveMarble(a.getLocation(), Location(x, y)) != None:
                        return True
       return False

    def getRemoveMarble(start, dest):
        if getOneActorAt(start) == None:
            return None
        if getOneActorAt(dest) != None:
            return None
        if not isMarbleLocation(dest):
            return None
        if dest.x - start.x == 2 and dest.y == start.y:
            return getOneActorAt(Location(start.x + 1, start.y))
        if start.x - dest.x == 2 and dest.y == start.y:
            return getOneActorAt(Location(start.x - 1, start.y))
        if dest.y - start.y == 2 and dest.x == start.x:
            return getOneActorAt(Location(start.x, start.y + 1))
        if start.y - dest.y == 2 and dest.x == start.x:
            return getOneActorAt(Location(start.x, start.y - 1))
        return None

    def isMarbleLocation(loc):
        if loc.x < 0 or loc.x > 6 or loc.y < 0 or loc.y > 6:
            return False
        if loc.x in [0, 1, 5, 6] and loc.y in [0, 1, 5, 6]:
            return False
        return True

    def initBoard():
        for x in range(7):
            for y in range(7):
                loc = Location(x, y)
                if isMarbleLocation(loc):
                    marble = Actor("sprites/marble.png")
                    addActor(marble, loc)
        removeActorsAt(Location(3, 3)) # Remove marble in center

    def pressEvent(e):
        global startLoc, movingMarble
        if isGameOver:
            return
        startLoc = toLocationInGrid(e.getX(), e.getY())
        movingMarble = getOneActorAt(startLoc)
        if movingMarble == None:
           setStatusText("Pressed at " + str(startLoc) + ".No marble found")
        else:
           setStatusText("Pressed at " + str(startLoc) + ".Marble found")

    def dragEvent(e):
        if isGameOver:
            return
        if movingMarble == None:
            return
        startPoint = toPoint(startLoc)
        movingMarble.setLocationOffset(e.getX() - startPoint.x,
                                       e.getY() - startPoint.y)

    def releaseEvent(e):
        if isGameOver:
            return
        if movingMarble == None:
            return
        destLoc = toLocationInGrid(e.getX(), e.getY())
        movingMarble.setLocationOffset(0, 0)
        removeMarble = getRemoveMarble(startLoc, destLoc)
        if removeMarble == None:
            setStatusText("Released at " + str(destLoc)
                           + ". Not a valid move.")
        else:
            removeActor(removeMarble)
            movingMarble.setLocation(destLoc)
            setStatusText("Released at " + str(destLoc)+
                          ". Valid move - Marble removed.")
            checkGameOver()


    startLoc = None
    movingMarble = None
    isGameOver = False

    makeGameGrid(7, 7, 70, None, "sprites/solitaire_board.png", False,
       mousePressed = pressEvent, mouseDragged = dragEvent,
       mouseReleased = releaseEvent)
    setBgColor(Color(255, 166, 0))
    setSimulationPeriod(20)
    addStatusBar(30)
    setStatusText("Press-drag-release to make a move.")
    initBoard()
    show()
    doRun()



Analyse de code
===============

Répondre aux questions d'analyse ci-dessous.

#.  À quoi sert la fonction ``isMarbleLocation(loc)`` ?

    ..  only:: corrige

        ..  admonition:: Corrigé
            :class: important

            **Réponses correctes** : 

            *   Elle permet de voir si le point que l'on entre appartient à la grille de jeu (retourne False si le point n'en fait pas partie et True s'il en fait partie.
            *   ça permet de dire si la case est une case du plateau où on peut poser une pièce.
            *   La fonction "isMarbleLocation(loc)" définit la position des acteurs, plus précisément les coordonnées où vont venir se placer les pions (marbre).

#.  Dans la fonction ``initBoard()``, pourquoi supprime-t-on un acteur à la position ``(3,3)`` de la grille de jeu ?

    ..  only:: corrige

        ..  admonition:: Corrigé
            :class: important

            **Exemples de réponses correctes** : 

            *   Car c'est l'acteur qui est au milieu de la grille. Si on ne le supprimait pas, on ne pourrait bouger aucun acteur car on a besoin d'une case vide.
            *   Quand on initialise le plateau, on place les pions partout. il faut donc enlever celui du milieu.
            *   C'est le pion ou l'acteur qui se trouve au centre de la grille de jeu. Si on ne le supprime pas, on peut tout simplement pas jouer.



#.  Expliquer en détails le fonctionnement de la ligne ``toLocationInGrid(e.getX(), e.getY())`` dans la fonction ``pressEvent(e)``

    ..  only:: corrige

        ..  admonition:: Corrigé
            :class: important

            **Exemples de réponses correctes** : 

            *   Elle retourne la position de la case dans laquelle se trouve la
                position donnée entre parenthèses par ``e.getX()`` et ``e.getY()`` 
            
            *   Au clic de souris, ``tolocationInGrid(e.getX(), e.getY())`` va
                renvoyer les coordonnées sur la grille de l'endroit où le clic a eu
                lieu. Cette ligne permet alors de connaître l'endroit où a eu lieu
                le clic.

            *   Le paramètre ``e`` correspond à l'objet événement qui survient
                lors du clic de la souris. La fonction ``toLocationInGrid(x, y)``
                permet de passer du **système de coordonnées "écran"** (pixels) au **système de
                coordonnées "grille"** (cases utilisées par JGameGrid pour placer les acteurs).

#.  Que se passerait-il si on oubliait le mot ``global`` à la ligne 58 dans la fonction ``pressEvent``

    ..  only:: corrige

        ..  admonition:: Corrigé
            :class: important

            **Exemples de réponses correctes** : 




            *   Les fonction dragEvent(e) et releaseEvent(e) ne pourraient pas fonctionner
            correctement.

            *   Les deux variables suivant l'indicateur 'global' ne serait utilisable que
                dans cette fonction. Le jeu ne fonctionnerait donc pas, on ne pourrait par
                exemple pas déplacer les acteurs.

            *   On ne met pas à jour les variables globales et on crée des variables
                locales.

            *   Le programme va considérer "startLoc" et "movingMarble" comme des variables
                locales, et ainsi s'y référer avant qu'une valeur leur soit attribuée. Il faut
                donc les considérer comme des variables globales car elles sont propres à la
                fonction et on ne peut s'y référer sans les rendre globales.

                ..  admonition::  Remarque
                    :class: warning

                    *   Bonne réponse. Mais cela ne dit pas ce qui va se produire
                        comme type d'erreur. Le programme va-t-il se planter? Va-t-il
                        être dysfonctionnel? Ne va-t-il tout simplement pas démarrer
                        (erreur de syntaxe) ?

                    *   Il faut préciser qu'il s'agit d'une erreur de
                        sémantique. Le programme va bien démarrer car la ligne 59

                        ..  code-block:: python

                            startLoc, movingMarble
                        
                        est valide sans le ``global`` (sauf dans TigerJython qui
                        signale que l'instruction ne fait rien). Mais cela n'est
                        pas une erreur Python standard. On peut désactiver cette
                        option dans les paramètres de TigerJython (Fichier =>
                        Options ... => Python => détection d'erreurs tricte).

                        Ce n'est pas une erreur d'exécution et le programme ne
                        va pas se planter car il va simplement créer des
                        variables locales ``startLoc`` et ``movingMarble`` au
                        lieu de modifier les variables globales. Les
                        gestionnaires d'événements ne pourront de ce fait pas
                        communiquer et la fonctionnalité de **glisser-déposer**
                        des pions ne fonctionnera pas correctement.

            *   Les autres fonctions de gestion d’événement n’auraient pas accès aux
                variables définies dans d’autres fonctions. Il serait donc bon de transformer ce
                code en un code orienté objet pour éviter ces problèmes.

                ..  admonition::  Remarque
                    :class: warning

                    *   En gros, cette réponse identifie bien le problème mais
                        manque de précision. Les différents gestionnaires
                        d'événements ``{press, drag, release}Eveent`` ont besoin
                        de communiquer et ils le font au travers de variables
                        globales. Il faut donc que ces variables soient
                        déclarées comme globales puisque les variables sont
                        locales par défaut en Python (fort heureusement).

                    *   Il est vrai qu'une programmation orientée objet très
                        propre aurait permis d'éviter le recours à des variables
                        globales et serait plus élégante. 


            **Exemples de réponses vraiment trop imprécises ou erronées**  :

            *   Les fonctions dragEvent et releaseEvent n'auraient pas accès aux valeurs de
                startLoc et movingMarble.

                ..  admonition::  Remarque
                    :class: warning
                
                    *   Que veut dire "avoir accès" ?? Accès en lecture mais pas en écriture !

            *   Serait variable propre à la fonction 

                ..  admonition::  Remarque
                    :class: warning
            
                    Pas précis, trop vague, n'entre pas assez dans les détails,
                    n'utilise pas la terminologie dédiée (variable locale.


#.  Dans la fonction ``dragEvent(e)``, à quoi sert la fonction ``setLocationOffset()``

    ..  only:: corrige

        ..  admonition:: Corrigé
            :class: important

            **Exemples de réponses correctes** : 

            *   La méthode ``Actor.setLocationOffset(dx, dy)`` permet d'afficher
                le sprite de l'acteur aux coordonnées relatives ``(dy, dy)`` par
                rapport à sa position réelle au sein de la grille de jeu. Cela
                permet, en l'occurrence, de déplacer l'image de l'acteur avec la
                souris sans pour autant déplacer l'acteur dans la grille.

#.  À quoi sert la fonction ``isMovePossible()`` et en quoi n'est-elle pas
    implémentée de manière très efficace ?

    ..  only:: corrige

        ..  admonition:: Corrigé
            :class: important

            **Exemples de réponses correctes** : 

            *   De concours avec la fonction ``getRemoveMarble```, la fonction
                ``isMovePossible`` permet de déterminer s'il est encore possible
                de bouger une bille. Elle est un peu inefficace car, pour chaque
                acteur testé, elle parcourt l'ensemble de la grile de jeu au
                lieu de ne tester que les cases potentielles.

        ..  admonition:: Remarque
            :class: attention

            Ce n'est cependant pas un problème à cause de la taille très
            réduite de la grille de jeu. Un code optimisé aurait sans doute
            été bien plus compliqué à implémenter. De manière générale, on
            n'optimise le code que lorsque cela est rendu nécessaire par
            l'utilisabilité du programme. En l'occurrence, ce petit manque
            de performance ne diminue pas l'expérience utilisateur (UX =
            User eXperience).

#.  Étudier le fonctionnement de la fonction ``getRemoveMarble(start, dest)`` et
    expliquer son fonctionnement en bref. Préciser à quoi servent toutes les
    instructions ``return`` présentes dans cette fonction.


    ..  admonition:: Corrigé
        :class: important

        **Élements de réponse corrects mais incomplets de manière isolée** : 

        *   Sert à indiquer tous les mouvement possibles pour qu’ils
            respectent les règles du jeux
        
        *   Elle retourne l'acteur qui doit être supprimé si le mouvement
            effectué est valable, et retourne 'None' si le mouvement n'est pas
            valable. Les paramètres représentent les endroits de départ et d'arrivée
            du mouvement effectué.
        
        *   Elle donne la position de la pièce à enlever.

        *   Conditions testées
        
            *   1.Si pos dép rien -> rien
            
            *   2.Si pos dest qqch -> rien
            
            *   3.Si pos déplacement de 2 entre dép_dest et pos dest y = pos dep y
                -> pièce entre 
            
            *   4.Si pos déplacement de 2 entre dest_dép et pos dest y = pos dep y
                -> pièce entre
            
            *   5.Si pos déplacement de 2 entre dép_dest et pos dest x = pos dep x
                -> pièce entre
            
            *   6.Si pos déplacement de 2 entre dest_dép et pos dest x = pos dep x
                -> pièce entre
            
            *   7.sinon -> rien
        u
        *   La fonction "getRemoveMarble(start, dest)" permet de retirer un pion
            du jeu lorsque celui-ci est "mangé". Toutes les instructions servent
            alors à connaître les cas qui permettent cela. Les conditions pour que
            l'on puisse "manger" le pion. Lorsque l'on passe par dessus un pion, la
            fonction va étudier le cas au travers de ses instructions et juger le
            geste valable ou non. 
        
        *   Elle vérifie les règles du jeu. Autrement dit, que le mouvement
            désiré avec un acteur lambda du jeu soit bel et bien possible. Les
            instructions ``return`` servent à prendre l'acteur, dans le cas où le
            mouvement est juste, se trouvant au milieu du mouvement et pouvoir
            l'enlever plus tard.
        





..  comment::

Concepts
========

#.  Citer les différentes phases de développement d'un logiciel

    ..  admonition:: Corrigé
        :class: important

        **Exemple de réponse correcte** : 

        Voici la méthodologie généralement utilisée pour un petit projet
        d'étudiant. Les remarques ci-dessous indiquent que l'industrie change
        parfois sciemment cet ordre pour la gestion de projets complexes.

        1. Définition des objectifs
        2. Analyse des besoins et faisabilité
        3. Conception générale
        4. Conception détaillée => cahier des charges
        5. Codage
        6. Tests unitaires
        7. Tests d'acceptance (on vérifie que les spécifications = User stories sont bien satisfaites)
        8. Documentation


    ..  admonition:: Remarques
        :class: warning

        Les phases mentionnées ne sont parfois pas réalisées dans cet ordre et,
        selon la complexité du logiciel, il est possible que certaines phases
        soient négligées ou que l'on recommence plusieurs fois certaines phases
        (itérations successives). 

        Par exemple, certains préconisent d'écrire la documentation avant de se
        mettre à coder, ce qui a tendance à forcer à bien réfléchir aux choses
        avant même de coder.

        Il y a aussi un courant important qui préconise d'écrire les tests avant
        d'écrire le code (TDD = Test Driven Development), très à la mode
        actuellement dans l'industrie.


#.  Expliquer ce qu'est la programmation défensive ?

    ..  admonition:: Corrigé
        :class: important

        **Élements de réponse corrects mais incomplets de manière isolée** : 
        
        *   C'est un état d'esprit qui consiste à s'attendre au pire lorsque
            l'on programme. Par exemple, le programmeur peut ajouter du code
            vérifiant qu'il n'y a pas d'erreurs (avant avoir exécuté le programme,
            donc sans savoir s'il y en a réellement)
        
        *   Programmer en prenant en compte toutes les possibilités pour éviter
            les problèmes. On ne fait pas confiance à l'utilisateur.
        
        *   C'est l'anticipation de ce qui pourrait arriver. Le programmeur doit
            alors penser à tout ce qui pourrait arriver et se préparer contre cela.
            Ainsi son programme ne sera alors pas perturbé et il ne rencontrera pas
            de problèmes.
        
        *   C'est écrire le code en s'attendant au pire. Elle permet d’assurer
            la fonction continue d'un logiciel dans des circonstances et
            utilisations imprévues.
        
        *   C'est de la programmation préventive qui s'occupe de prendre en
            compte tous les cas qui peuvent entraîner une erreur.


Exercice supplémentaire
=======================

Éliminer toutes les variables globales en créant une classe ``GameManager``
