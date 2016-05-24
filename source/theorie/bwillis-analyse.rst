********
Apprentissage par l'exemple
********

Définition d'une classe
=======================

Un bon exemple vaut mieux qu'un long discours pour cerner immédiatement les
différentes notions de base de la programmation orientée  objets. Enfilez vos
meilleures lunettes (ou lentilles) et observez attentivement le code suivant
qui montre comment définir une nouvelle classe ``Recipient`` qui dérive de la
classe de base ``object`` :

..  code-block:: python
    :linenos:

    class Recipient(object):

        def __init__(self, contenance, no):
           self.no = no
           self.contenance = contenance
           self.volume = 0

        def vider(self):
           self.volume = 0

        def transferer(self, autre):
            quantite_transferee = min(autre.contenance - autre.volume, self.volume)
            autre.volume += quantite_transferee
            self.volume -= quantite_transferee

        def remplir(self):
           self.volume = self.contenance

        def __str__(self):
            return "Récipient no {}, Contenance : {}, Volume : {}".format(self.no,
                                                                          self.contenance,
                                                                          self.volume)

        def __repr__(self):
            return str(self)

Analyse du code
---------------

Étudiez attentivement le code ci-dessus à l'aide des annotations.

..  tip::

    Si vous ne comprenez pas tout, c'est normal ... la programmation orientée
    objets est difficile d'accès au début, mais dès qu'on commence à la
    maîtriser, c'est un petit paradis de la programmation.

..  figure:: figures/analyse-recipient.png
    :align: center
    :width: 98%




Cette classe va nous permettre d'aider Bruce Willis à désamorcer une bombe ...

Utilisation de la classe
========================

Pour pouvoir utiliser une classe, il faut créer un ou plusieurs objets de
cette classe. En termes techniques, on dit qu'on crée une **instance** de la
classe ou qu'on **instancie** la classe. Ainsi, après avoir défini la classe à
l'aide du mot-clé ``class``, on peut créer des récipients différents.

::

    >>> r1 = Recipient(no = 1, contenance = 5)
    >>> r2 = Recipient(no = 2, contenance = 3)

À l'aide de ces deux lignes, ont vient de créer deux objets concrets
(instances) de la classe ``Recipient`` (on pourrait dire du *type*
``Recipient``). En effet, notre classe ``Recipient`` constitue un nouveau type
de données utilisable dans notre programme.

    >>> r2.remplir() # remplir le recipient r2
    >>> r1.transferer(r2) # transfère le contenu de r2 dans r1
    >>> r2.vider() # vider le récipient r2
    >>> r2.volume
    0
    >>> r1.volume
    3
    ...
    >>> r2.volume == 2 # ce que l’on devrait obtenir à la fin ...
    True

..
    ..  activecode:: oop_exemple1
        :nocanvas:
        :language: python
        :caption: Premier exemple de test

        from math import pi

        def add(a,b):
            return a+b

        ## grading
        import unittestgui

        class myTests(unittestgui.unittest):

           def testOne(self):
               self.assertEqual(add(2,2),4,"A feedback string when the test fails")
               self.assertEqual(add(2, 0), 2, "balba")
               #self.assertAlmostEqual(add(2.0,3.0),5.0,"Your function failed on inputs of 2.0 and 3.0")

        myTests().main()


Récréation
----------

Dans *Die Hard 3*, Bruce Willis a besoin de 4 "gallons" d'eau pour
désamorcer une bombe, mais il ne dispose que d'un récipient de contenant 3
gallons et un autre de contenance 5 gallons. Comment doit-il s'y prendre?


..  tip::

    Regarder la séquence du film https://www.youtube.com/watch?v=BVtQNK_ZUJg

    ..  only:: html

        ..  youtube:: BVtQNK_ZUJg


Utilisez la classe ``Recipient`` définie ci-dessus pour écrire un programme qui permet d'avoir 4 gallons dans le grand récipient.

..  admonition:: Contraintes


    Les récipients ne sont pas gradués. On peut donc uniquement faire les opérations suivantes avec les récipients :

    *   Remplir le récipient ``r1`` avec

        ::

            r1.remplir()

    *   Transférer le contenu du récipient ``r1`` dans le récipient ``r2``. Uniquement le volume encore disponible dans le récipient ``r2`` sera transféré, le reste demeure dans le récipient de départ ``r1``.

        ::

            r1.transferer(r2)

    *   Vider le récipient avec

        ::

            r1.vider()



..  tip::

    Si vous ne parvenez pas à la solution, faites une recherche sur Google avec la requête

    ::

        Die Hard 3 jug riddle


Code de base
------------

..  code-block:: python

    # On commence par créer les instances de la classe Recipient en
    # spécifiant la capacité
    r1 = Recipient(no = 1, contenance = 5)
    r2 = Recipient(no = 2, contenance = 3)

    # Procédure à compléter  ...



    # La bombe ne peut être désamorcée que si le volume de r1 vaut 4
    # gallons
    assert(r1.volume == 4)
