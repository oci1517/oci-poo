..  footer::

    OCI 3 -- Programmation orientée objets -- page ###Page###

*************
Classes et objets
*************

Récapitulation des notions de base de la POO
============================================

Observez attentivement le code ci-dessous et répondre aux questions. Toutes
les questions posées sont vraiment essentielles et dont des questions types
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

2)  Décrire précisément ce qui se passe à la ligne 7

    ..  raw:: pdf

        Spacer 0 90

3)  Que représente le premier paramètre ``self`` dans la définition des méthodes d'instance ?

    ..  raw:: pdf

        Spacer 0 90

4)  À quoi sert la fonction ``pressCallback(e)`` définie aux lignes 14 à 16 ?

    ..  raw:: pdf

        Spacer 0 90

5)  Que représente le paramètre ``e`` de la fonctoin ``pressCallback(e)`` ?

    ..  raw:: pdf

        Spacer 0 90

6)  Décrire précisément ce qui se passe à la ligne 16 ?

    ..  raw:: pdf

        Spacer 0 90

7)  Expliquer ce que fait globalement ce code Python?

    ..  raw:: pdf

        Spacer 0 90


Héritage
========

L'héritage est une des propriétés les plus utiles et fondamentales dans la
POO. Ce mécanisme permet de réutiliser du code défini dans d'autres classes
par dérivation. Observer ce code en répondre aux questions posées :

..  code-block:: python
    :linenos:

    from gamegrid import *
    # Une des forces de TigerJython est qu'il permet d'utiliser
    # les bibliothèques Java
    from java.awt import Point

    # ---------------- class Animal ----------------
    class Animal():
        
        def __init__(self, imgPath): 
            self.imagePath = imgPath 

        
        def showMe(self, x, y): 
             bg.drawImage(self.imagePath, x, y)

    # ---------------- class Pet ----------------
    class Pet(Animal):   # Derived from Animal
        
        def __init__(self, imgPath, name):  
            super().__init__(self, imgPath)
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

1)  Pourquoi met-on ``Animal entre parenthèses`` après ``class Pet`` dans la définition de la casse ``Pet`` ?

    ..  raw:: pdf

        Spacer 0 90

2)  Décrire précisément ce que fait la ligne 20

    ..  raw:: pdf

        Spacer 0 90

3)  Décrire ce que fait le programme globalement

    ..  raw:: pdf

        Spacer 0 120

4)  Dessiner le diagramme de classes de ``Animals`` et ``Pet``

    ..  raw:: pdf

        Spacer 0 160


Hiérarchie de classes
---------------------

..  code-block:: python
    :linenos:

    from gamegrid import *
    from java.awt import Point

    # ---------------- class Animal ----------------
    class Animal():
        
        def __init__(self, imgPath): 
            self.imagePath = imgPath 

        
        def showMe(self, x, y):  
             bg.drawImage(self.imagePath, x, y) 
             
    # ---------------- class Pet ----------------
    class Pet(Animal): 
        
        def __init__(self, imgPath, name): 
            self.imagePath = imgPath 
            self.name = name
        
        def tell(self, x, y):
            bg.drawText(self.name, Point(x, y))

    # ---------------- class Dog ----------------
    class Dog(Pet):
        
        def __init__(self, imgPath, name): 
            self.imagePath = imgPath 
            self.name = name
        
        def tell(self, x, y): # Overriding
            bg.setPaintColor(Color.blue)
            bg.drawText(self.name + " tells 'Waoh'", Point(x, y))

    # ---------------- class Cat ----------------
    class Cat(Pet):
        
        def __init__(self, imgPath, name):
            self.imagePath = imgPath
            self.name = name
        
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
    alex.tell(200, 130)  # Overriden method is called

    rex = Dog("sprites/dog.gif", "Rex")
    rex.showMe(100, 300) 
    rex.tell(200, 330)  # Overriden method is called

    xara = Cat("sprites/cat.gif", "Xara")
    xara.showMe(100, 500) 
    xara.tell(200, 530)  # Overriden method is called


Polymorphisme
=============

..  code-block:: python
    :linenos:

    from gamegrid import *
    from soundsystem import *

    # ---------------- class Animal ----------------
    class Animal():
        
        def __init__(self, imgPath): 
            self.imagePath = imgPath 

        
        def showMe(self, x, y):  
             bg.drawImage(self.imagePath, x, y) 
             
    # ---------------- class Pet ----------------
    class Pet(Animal): 
        
        def __init__(self, imgPath, name): 
            self.imagePath = imgPath 
            self.name = name
        
        def tell(self, x, y):
            bg.drawText(self.name, Point(x, y))

    # ---------------- class Dog ----------------
    class Dog(Pet):
        
        def __init__(self, imgPath, name): 
             self.imagePath = imgPath 
             self.name = name
        
        def tell(self, x, y): # Overridden
             Pet.tell(self, x, y)
             openSoundPlayer("wav/dog.wav")
             play()

    # ---------------- class Cat ----------------
    class Cat(Pet):
        
        def __init__(self, imgPath, name):
            self.imagePath = imgPath
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

    animals = 
        [Dog("sprites/dog.gif", "Alex"), 
         Dog("sprites/dog.gif", "Rex"), 
         Cat("sprites/cat.gif", "Xara")]

    y = 100
    for animal in animals:
        animal.showMe(100, y)     
        animal.tell(200, y + 30)    # Which tell()???? 
        pet.show())
        y = y + 200
        delay(1000)

