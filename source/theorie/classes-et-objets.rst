..  footer::

    OCI 3 -- Programmation orientée objets -- page ###Page###

*************
Classes et objets
*************

..  only:: html

    ..  admonition:: Documents

        Voici une version PDF de cette section pour vous permettre d'étudier et
        annoter le code sur papier.

        *   Version PDF de cette section : :download:`classes-et-objets.pdf`

Récapitulation des notions de base de la POO
============================================

Observez attentivement le code ci-dessous et répondre aux questions. Toutes
les questions posées sont vraiment essentielles et donc des questions types
qui peuvent être posées lors d'un oral de BAC.

..  code-block:: python
    :linenos:

    from gamegrid import *

    # ---------------- classe Animal ----------------
    class Animal():

        def __init__(self, imgPath):
            self.imagePath = imgPath


        def showMe(self, x, y):
             bg.drawImage(self.imagePath, x, y)


    def pressCallback(e):
        myAnimal = Animal("sprites/animal.gif")
        myAnimal.showMe(e.getX(), e.getY())

    makeGameGrid(600, 600, 1, False, mousePressed = pressCallback)
    setBgColor(Color.green)
    show()
    doRun()
    bg = getBg()

Analyse de code
---------------

1)  Décrire le rôle de la fonction ``__init__`` aux lignes 6 et 7

    ..  raw:: pdf

        Spacer 0 90

    ..  only:: corrige

        ..  admonition:: Corrigé

            La fonction ``__init__`` est le constructeur de la classe ``Animal``.
            Cette fonction est appelée automatiquement à fois que l'on crée un animal avec

            ::

                mon_animal = Animal("sprites/example.png")

2)  Décrire précisément ce qui se passe à la ligne 7

    ..  raw:: pdf

        Spacer 0 90

    ..  only:: corrige

        ..  admonition:: Corrigé

            Cette ligne crée la variable d'instance ``self.imagePath`` et
            l'initialise avec le contenu de la variable locale ``igmPath``.

3)  Que représente le premier paramètre ``self`` dans la définition des méthodes d'instance ?

    ..  raw:: pdf

        Spacer 0 90

    ..  only:: corrige

        ..  admonition:: Corrigé

            Le paramètre ``self`` est propre à toutes les méthodes d'instance
            et doit toujours se trouver en première position. Il s'agit d'une
            référence vers l'instance concrète sur laquelle la méthode a été
            invoquée.

            Lors de l'invocation de la méthode avec

            ::

                mon_animal.showMe(10, 20)

            on ne renseigne pas ce paramètre ``self`` car Python s'en charge
            pour nous en transformant notre appel dans le code suivant avant
            de l'exécuter :

            ::

                Animal.showMe(mon_animal, 10, 20)

4)  À quoi sert la fonction ``pressCallback(e)`` définie aux lignes 14 à 16 ?

    ..  raw:: pdf

        Spacer 0 120

    ..  only:: corrige

        ..  admonition:: Corrigé

            Cette fonction est un **gestionnaire d'événement** (*Event
            handler* en anglais). Elle sera appelée à par le système du jeu à
            chaque fois qu'un événement de type ``MousePressed`` est généré
            par le système.

            C'est uniquement à la ligne 18

            ::

                makeGameGrid(600, 600, 1, False, mousePressed = pressCallback)

            que notre fonction ``pressCallback`` est "connectée" à l'événemnt
            ``mousePressed``. Ce qui se passe à la ligne 18 est très nouveau
            : on passe à la fonction ``makeGameGrid`` la fonction
            ``pressCallback`` en guise de paramètre. Notez bien que l'on n'a pas
            écrit ``mousePressed = pressCallback()`` mais bien ``mousePressed
            = pressCallback`` sans appeler la fonction ``pressCallback`` avec
            des parenthèses ``()``.

5)  Que représente le paramètre ``e`` de la fonctoin ``pressCallback(e)`` ?

    ..  raw:: pdf

        Spacer 0 90

    ..  only:: corrige

        ..  admonition:: Corrigé

            Il s'agit d'un objet représentant l'événement qui a déclenché
            l'appel de ``pressCallback``. Cet objet ``e`` contient des
            informations sur l'événement généré par le clic de souris, en
            particulier les coordonnées du clic récupérables avec ``e.getX()``
            et ``e.getY()``.

6)  Décrire précisément ce qui se passe à la ligne 16 ?

    ..  raw:: pdf

        Spacer 0 90

    ..  only:: corrige

        ..  admonition:: Corrigé

            En gros, on crée une instance de la classe ``Animal`` à la ligne
            15 que l'on affiche à la ligne 16 à l'emplacement du clic de la
            souris.

7)  Expliquer ce que fait globalement ce code Python?

    ..  raw:: pdf

        Spacer 0 130

    ..  only:: corrige

        ..  admonition:: Corrigé

            Globalement, le programme affiche des petits animaux lorsqu'on
            clique dans l'espace de jeu. Le coin supérieur gauche du rectangle
            contenant le sprite de l'animal correspondra aux coordonnées du
            clic de la souris.


Héritage
========

L'héritage est une des propriétés les plus utiles et fondamentales dans la
POO. Ce mécanisme permet de réutiliser du code défini dans d'autres classes
par dérivation. Observer ce code et répondre aux questions posées :

..  only:: not pdf

    ..  sidebar:: Appel du construteur de la classe de base

        Dans la version 2.7 de Python utilisée par TigerJython, on peut écrire

        ::

            super(Pet, self).__init__(self, imgPath)

        pour appeler le constructeur de la classe de base de ``Pet`` pour éviter
        d'y faire référence explicitement comme le fait notre code avec

        ::

            Animal.__init__(self, imgPath)

        Dans Python 3, il est possible de se contenter de

        ::

            super().__init__(self, imgPath)

        ce qui est nettement plus élégant


..  code-block:: python
    :linenos:

    from gamegrid import *
    # Une des forces de TigerJython est qu'il permet d'utiliser
    # les bibliothèques Java
    from java.awt import Point

    # ---------------- classe Animal ----------------
    class Animal():

        def __init__(self, imgPath):
            self.imagePath = imgPath


        def showMe(self, x, y):
             bg.drawImage(self.imagePath, x, y)

    # ---------------- classe Pet ----------------
    class Pet(Animal):   # Derived from Animal

        def __init__(self, imgPath, name):
            Animal.__init__(self, imgPath)
            self.name = name

        def tell(self, x, y): # Additional method
            bg.drawText(self.name, Point(x, y))

    makeGameGrid(600, 600, 1, False)
    setBgColor(Color.green)
    show()
    doRun()
    bg = getBg()
    bg.setPaintColor(Color.black)

    for i in range(5):
        myPet = Pet("sprites/pet.gif", "Trixi")
        myPet.showMe(50 + 100 * i, 100)
        myPet.tell(72 + 100 * i, 145)


Questions
---------

1)  Pourquoi met-on ``Animal`` entre parenthèses après ``class Pet`` dans la définition de la casse ``Pet`` ?

    ..  raw:: pdf

        Spacer 0 90

    ..  only:: corrige

        ..  admonition:: Corrigé

            Pour indiquer que la classe ``Pet`` est basée sur la classe
            ``Animal``. Autrement dit, la classe ``Pet`` hérite de toutes les
            propriétés (variables d'instances) et méthodes de la classe
            ``Animal``.

2)  Décrire précisément ce que fait la ligne 20

    ..  raw:: pdf

        Spacer 0 90


    ..  only:: corrige

        ..  admonition:: Corrigé

            La ligne 20

            ::

                Animal.__init__(self, imgPath)

            appelle explicitement le constructeur de la classe parent pour lui
            déléguer l'initialisation des attributs d'instances définis dans
            la classe ``Animal``.

        ..  tip::

            Il faut toujours déléguer l'initialisation des variables
            d'instances définies dans la classe de base au construteur de la
            classe de base.

3)  Décrire ce que fait le programme globalement

    ..  raw:: pdf

        Spacer 0 120

    ..  only:: corrige

        ..  admonition:: Corrigé

            En général, un bon programmeur peut prendre le code de quelqu'un
            d'autre et savoir ce qu'il va faire sans l'exécuter. Le commun des
            mortels  exécutent le programme et s'étonnent lorsque ça ne
            fonctionne pas comme ils pensaient ...

4)  Dessiner le diagramme de classes de ``Animals`` et ``Pet``

    ..  raw:: pdf

        Spacer 0 400

    ..  only:: corrige

        ..  admonition:: Corrigé

            ..  figure:: figures/diagramme-classe-Animal-Pet.png
                :width: 95%
                :align: center

                Diagramme de classes montrant la classe ``Pet`` dérivée de la classe ``Animal``

..  admonition:: À retenir

    On peut appeler sans problème la méthode ``myPet.showMe()`` alors même que
    ``showMe()`` n'est pas définie dans la classe ``Pet``, car un animal de
    compagnie est bien un animal et dispose donc des mêmes comportements. On
    appelle cette relation des classes ``Pet`` et ``Animal`` une relation
    **Est-Un(e)** (*IS-A* en anglais), car un ``Pet`` *est un* ``Animal``.

    Pour que ``DerivedClass`` dérive de la classe ``BaseClass``, il suffit
    d'indiquer ``(BaseClass)`` entre parenthèses dans la définition de
    ``DerivedClass`` :

    ::

        class BaseClass:

            # définition de la classe de base
            pass

        class DerivedClass(BaseClass):

            # définition de la classe dérivée
            pass

    En Python 3, par convention, les classes qui n'ont pas de classe de base
    dérivent de la classe ``object`` et il est considéré comme une bonne
    pratique de l'indiquer explicitement :

    ::

        # classe qui ne dérive d'aucune autre classe
        class MaClasse(object):

            # définition de la classe
            pass


    Le langage Python permet l'**héritage multiple** (*Mutliple inheritance* en anglais), ce qui permet de dériver une classe à partir de plusieurs classes de base :

    ::

        # classe qui ne dérive d'aucune autre classe
        class MaClasse(BaseClass1, BaseClass2):

            # définition de la classe
            pass


Hiérarchie de classes
---------------------

Étudier attentivement le code suivant et répondre aux questions :

..  code-block:: python
    :linenos:

    from gamegrid import *
    from java.awt import Point

    # ---------------- classe Animal ----------------
    class Animal():

        def __init__(self, imgPath):
            self.imagePath = imgPath


        def showMe(self, x, y):
             bg.drawImage(self.imagePath, x, y)

    # ---------------- classe Pet ----------------
    class Pet(Animal):

        def __init__(self, imgPath, name):
            Animal.__init__(self, imgPath)
            self.name = name

        def tell(self, x, y):
            bg.drawText(self.name, Point(x, y))

    # ---------------- classe Dog ----------------
    class Dog(Pet):

        def __init__(self, imgPath, name):
            Pet.__init__(self, imgPath, name)

        def tell(self, x, y): # Overriding
            bg.setPaintColor(Color.blue)
            bg.drawText(self.name + " tells 'Waoh'", Point(x, y))

    # ---------------- classe Cat ----------------
    class Cat(Pet):

        def __init__(self, imgPath, name):
            Pet.__init__(self, imgPath, name)

        def tell(self, x, y): # Overriding
            bg.setPaintColor(Color.gray)
            bg.drawText(self.name + "  tells 'Meow'", Point(x, y))

    makeGameGrid(600, 600, 1, False)
    setBgColor(Color.green)
    show()
    doRun()
    bg = getBg()

    alex = Dog("sprites/dog.gif", "Alex")
    alex.showMe(100, 100)
    alex.tell(200, 130)

    rex = Dog("sprites/dog.gif", "Rex")
    rex.showMe(100, 300)
    rex.tell(200, 330)

    xara = Cat("sprites/cat.gif", "Xara")
    xara.showMe(100, 500)
    xara.tell(200, 530)

Questions
---------

1)  Dessiner le diagramme de classes de ``Animal``, ``Pet``, ``Cat``, ``Dog``

    ..  raw:: pdf

        Spacer 0 300

    ..  only:: corrige

        ..  admonition:: Corrigé

            ..  figure:: figures/diag-classe-Animal-Pet-Cat-Dog.png
                :width: 95%
                :align: center

                Diagramme de classes montrant la classe ``Pet`` dérivée de la classe ``Animal``


2)  Modifier les classes ``Dog`` et ``Cat`` pour qu'elles chargent automatiquement le bon sprite (la bonne image représentative)
    sans devoir le spécifier dans le construteur

    ..  raw:: pdf

        Spacer 0 130


    ..  only:: corrige

        ..  admonition:: Corrigé

            Il suffit de modifier le construteur des classes ``Dog`` et
            ``Cat``. Par exemple, pour la classe ``Dog``, en supposant que le
            sprite voulu soit ``sprites/dog.png``, il apporter les modifications suivantes :

            ..  code-block:: python

                class Dog(Pet):

                    def __init__(self, name):
                        Pet.__init__(self, imgPath="dog.png")
                        self.name = name

..  only:: not pdf

    Polymorphisme
    =============

    Le polymorphisme consiste à **surcharger** (*override* en anglais) les
    méthodes de la classe de base dans les classes dérivées. Ici, en
    l'occurrence, on utilise ce mécanisme pour surcharger la méthode ``tell``
    dans les classes ``Dog`` et ``Cat`` :

    ..  code-block:: python
        :linenos:

        from gamegrid import *
        from soundsystem import *

        # ---------------- classe Animal ----------------
        class Animal():

            def __init__(self, imgPath):
                self.imagePath = imgPath


            def showMe(self, x, y):
                 bg.drawImage(self.imagePath, x, y)

        # ---------------- classe Pet ----------------
        class Pet(Animal):

            def __init__(self, imgPath, name):
                Animal.__init__(self, imgPath)
                self.name = name

            def tell(self, x, y):
                bg.drawText(self.name, Point(x, y))

        # ---------------- classe Dog ----------------
        class Dog(Pet):

            def __init__(self, imgPath, name):
                Pet.__init__(self, imgPath, name)
                self.name = name

            def tell(self, x, y): # Overridden
                Pet.tell(self, x, y)
                openSoundPlayer("wav/dog.wav")
                play()

        # ---------------- classe Cat ----------------
        class Cat(Pet):

            def __init__(self, imgPath, name):
                Pet.__init__(self, imgPath, name)
                self.name = name

            def tell(self, x, y): # Overridden
                Pet.tell(self, x, y)
                openSoundPlayer("wav/cat.wav")
                play()


        makeGameGrid(600, 600, 1, False)
        setBgColor(Color.green)
        show()
        doRun()
        bg = getBg()

        pets = [Dog("sprites/dog.gif", "Alex"),
                   Dog("sprites/dog.gif", "Rex"),
                   Cat("sprites/cat.gif", "Xara")]

        y = 100
        for pet in pets:
            pet.showMe(100, y)
            pet.tell(200, y + 30)    # Which tell()????
            y = y + 200
            delay(1000)


..  admonition:: À retenir

    a)  Lorsqu'un méthode est redéfinie à plusieurs endroits dans une
        hiérachie de classes, le polymorphisme permet d'appeler la bonne version
        de la méthode. En Python, le polymorphisme est logique puisque le type des
        données est déterminé de manière dynamique lors de l'exécution. Toutefois,
        dans les langages à typage statique tels que Java ou C++, le mécanisme de
        polymorphisme est bien moins trivial.

    b)  Le polymorphisme pratiqué par Python est parfois appelé *Duck-Typing*
        selon la citation de James Whitcomb Riley (1849 - 1916) :

            Si je vois un oiseau qui marche comme un canard, nage comme un
            canard et qui cancane comme un canard, alors il s'agit d'un canard

    c)  Il arrive qu'une méthode soit définie dans la classe de base mais
        qu'elle ne doive rien faire du tout à part être redéfinie dans les classes
        dérivées. On parle alors de **méthode virtuelle** définie dans une
        **classe abstraite**.

        En Python, on spécifie qu'une méthode est virtuelle et ne doit donc
        pas être appelée en levant l'exception ``NotImplementedError``

        ::

            class AbstractClass(object):

                def __init__(self):
                    pass

                def VirtualMethod(self):
                    raise NotImplementedError

Es gibt Fälle, wo eine überschriebene Methode in der Basisklasse zwar definiert ist, aber nichts bewirken soll.  Dies erreicht man entweder mit einem sofortigen return oder mit der leeren Anweisung pass.



Toute la puissance du polymorphisme
===================================

Il est possible d'obtenir exactement le même résultat avec moins de code. En
effet, la seule différence entre les méthodes ``Dog.tell`` et ``Cat.tell`` est
le nom du fichier WAV joué. Dès lors, on peut éviter de surcharger cette
méthode dans les classes filles et faire référence, dans la classe de base
``Pet``, à une variable d'instance qui est définie dans la classe de base
``Pet`` mais qui sera spécifiée de manière différente uniquement dans le
construteur des classes dérivées ``Cat`` et ``Dog``.

Observez bien le code ci-dessous pour comprendre comment cela fonctionne :

..  literalinclude:: scripts/catsndogs_3.py
    :language: python
    :linenos:


Modifications effectuées
------------------------

Lorsqu'on a deux versions différentes d'un même fichier, on peut toujours
observer rapidement les ajouts ou suppression du deuxième fichier par rapport
au fichier original avec la commande

..  code-block:: bash

    diff fichier1.py fichier2.py

qui donne le résultat suivant

..  literalinclude:: scripts/catsndogs.diff
    :language: diff
