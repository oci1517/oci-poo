*************
Classes et objets
*************

Variables d'instances
=====================

::

    from gamegrid import *

    # ---------------- class Animal ----------------
    class Animal():
        def __init__(self, imgPath):
            self.imagePath = imgPath  # Instance variable

        def showMe(self, x, y):  # Method definition
             bg.drawImage(self.imagePath, x, y) 

    def pressCallback(e):
        myAnimal = Animal("sprites/animal.gif") # Object creation
        myAnimal.showMe(e.getX(), e.getY())  # Method call

    makeGameGrid(600, 600, 1, False, mousePressed = pressCallback)
    setBgColor(Color.green)
    show()
    doRun()
    bg = getBg()


Héritage
========

::

    from gamegrid import *
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
            self.imagePath = imgPath 
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

Hiérarchie de classes
---------------------

::

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

