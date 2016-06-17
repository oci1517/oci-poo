***************
Solitaire, jeux de plateau
***************

..  admonition:: lecture
    :class: warning

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

#.  Dans la fonction ``initBoard()``, pourquoi supprime-t-on un acteur à la position ``(3,3)`` de la grille de jeu ?

#.  Expliquer en détails le fonctionnement de la ligne ``toLocationInGrid(e.getX(), e.getY())`` dans la fonction ``pressEvent(e)``

#.  Que se passerait-il si on oubliait le mot ``global`` à la ligne 58 dans la fonction ``pressEvent``

#.  Dans la fonction ``dragEvent(e)``, à quoi sert la fonction ``setLocationOffset()``

#.  À quoi sert la fonction ``isMovePossible()`` et en quoi n'est-elle pas implémentée de manière très efficace ?

#.  Étudier le fonctionnement de la fonction ``getRemoveMarble(start, dest)`` et expliquer son fonctionnement en bref. Préciser à quoi servent toutes les instructions ``return`` présentes dans cette fonction.




..  comment::

Concepts
========

#.  Citer les différentes phases de développement d'un logiciel

#.  Expliquer ce qu'est la programmation défensive ???





Exercice supplémentaire
=======================

Éliminer toutes les variables globales en créant une classe ``GameManager``
