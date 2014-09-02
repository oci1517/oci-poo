Surcharge d'opérateurs
######################

Théorie
=======

La **surcharge d'opérateurs** permet de définir des opérateurs dont
l'utilisation sera différente selon le type des paramètres qui leur sont
passés. Il est donc possible par exemple de surcharger l'opérateur ``+`` et de
lui faire réaliser des actions différentes selon qu'il s'agit d'une opération
entre deux entiers (addition : ``3+4 = 7``) ou entre deux chaînes de caractères
(concaténation : ``"parle" + "ment" = "parlement"``). Ainsi, l'opérateur reste le
même mais sont action est différente . En anglais, on parle alors d'\
**overloading.** La surcharge d'opérateur en Python se fait de la même manière
que la définition d'une méthode à l'exception que le nom de la méthode à
définir est spécifié par le langage. Ainsi, pour surcharger l'opérateur ``+`` de
telle sorte qu'il puisse également additionner deux objets de type
``Point()``, il suffit de définir une méthode ``__add__`` dans la classe
``Point()`` :

..  code-block:: python
    :linenos:

    class Point(object):
        "Encore une nouvelle classe de points"

        def __init__(self, coord_x, coord_y):
            self.x = coord_x
            self.y = coord_y

        def __repr__(self):
            return "({}; {})".format(self.x, self.y)

        def __add__(self, other):
            x_res = self.x + other.x
            y_res = self.y + other.y
            res = Point(x_res, y_res)
            return res

L'exécution de ce script provoque l'affichage suivant :

..  code-block:: python

    >>> A = Point(4, 7)
    >>> B = Point(-2, 5)
    >>> C = A + B
    >>> C
    (2; 12)

Notons que l'addition ``A + B`` est automatiquement convertie par Python
sous la forme d'un appel à la méthode ``__add__``, c'est-à-dire sous
la forme ``A.__add__(B)``. La surcharge d'opérateurs facilite la
lisibilité du code tout en étendant les fonctionnalité de certains
opérateurs. La plupart des opérateurs Python peuvent être surchargés de
cette manière en définissant la méthode correspondante. Parmi les plus
importants, nous retiendrons surtout les opérateurs suivants :

..  list-table:: Surcharge des opérateurs arithmétiques
    :header-rows: 1

    *   - Opérateur
        - Méthode à surcharger

    *   - ``+``
        - ``__add__``

    *   - ``-``
        - ``__sub__``

    *   - ``*``
        - ``__mul__``

    *   - ``/``
        - ``__div__``

    *   - ``<``
        - ``__lt__``

    *   - ``<=``
        - ``__le__``

    *   - ``>``
        - ``__gt__``

    *   - ``>=``
        - ``__ge__``

    *   - ``==``
        - ``__eq__``
          
Exercice 1 (opérations sur les fractions)
=========================================

On donne la classe ``Vector`` suivante qui représente des vecteurs.

..  code-block:: python

    class Vector(object):

        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def __repr__(self):
            return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)

Consigne
--------

Surcharger les opérateurs ``+`` et ``*`` pour que les opérations suivantes soient possibles :

..  code-block:: python

    >>> v1 = Vector(1, 1, 1)
    >>> v2 = Vector(2, 2, 2)
    >>> v1 + v2 # somme vectorielle
    Vector(3, 3, 3)
    >>> v1 * v2  # produit scalaire
    6


Exercice 2 (Opérations sur les vecteurs)
========================================

Implémenter une classe Fraction qui doit pouvoir s’utiliser de la manière suivante :
 
..  code-block:: python

    # Manières d'appeler le constructeur #de fractions.
    >>> Fraction(4, -6)
    Fraction(-2, 3)
    >>> Fraction('-5/6')
    Fraction(-5, 6)
    >>> Fraction('4')
    Fraction(4,1)
    >>> Fraction('4.2')
    Fraction(21, 5)
    # donne le plus petit dénominateur com-mun 
    >>> f1, f2 = Fraction(6, 3), Frac-tion(2, 5)
    # opérations arithmétiques sur les ob-jets Fraction
    >>> f1 + f2
    Fraction(12, 5)
    >>> f1 - f2
    Fraction(8, 5)

    >>> f1 * f2
    Fraction(4, 5)
    >>> f1 / f2
    Fraction(5, 1)
    # opérations de comparaison sur les fractions
    >>> f1 < f2
    False
    >>> f2 < f1
    True
    >>> f1 == f2
    False
    >>> f1 <= f2
    False
    >>> f1 >= f2
    True
    >>> gcd(15, 21)
    3
    >>> gcd(15, 5)
    5

Indications
-----------

*   Compléter le fichier ``my_fractions.py`` qui se trouve sur GoogleDocs et qui dispose déjà
    d’une fonction ``pgcd`` qui calcule le pgcd de deux nombres entiers à l’aide de l’algorithme d’Euclide

*   Le module intégré ``fractions`` contient une classe ``Fraction`` qui présente ces caractéristiques.
    Il est donc possible d’importer la classe ``Fraction`` avec ``from fractions import Fraction``.
*   Une fraction négative est représentée par un numérateur négatif et un dénominateur positif.
*   Veiller à définir une méthode ``reduire()`` qui divise le numérateur et le dénominateur par leur PGCD.
*   Surcharger les fonctions spéciales ``__add__``, ``__mul__``, ``__div__`` etc … pour implémenter les opérations mathématiques sur les fractions
*   Surcharger les opérations de comparaison pour pouvoir comparer des fractions (cf. la documentation pour savoir comment s’appellent ces méthodes spéciales, comme par exemple ``__le__`` pour ``<``.
*   Tester le type de la valeur donnée au constructeur et lever des erreurs de manière appropriée, par exemple si le dénominateur vaut 0, si la chaine de caractère ne représente pas un nombre, etc …