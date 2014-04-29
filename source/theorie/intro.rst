************
Introduction
************

La programmation orientée objet est un *paradigme de programmation*
informatique qui consiste en la définition et l'assemblage de "briques
informatiques", appelées objets. Un objet est une entité que l’on construit
par instanciation à partir d’une classe. Une classe est en quelque sorte une «
catégorie » ou un « type » d’objets représentant un concept, une idée ou toute
entité du monde physique comme une voiture, une personne ou encore un livre.
En fait, vous avez déjà rencontré et manipulé des objets en Python puisque
toutes les variables existant en Python sont des objets, ainsi que les listes,
tuples et dictionnaires. En Python, même les fonctions sont des objets.

L'objectif de ce chapitre est d'apprendre à définir de nouvelles classes
d’objets. Il s’agit là d’un sujet relativement ardu, mais vous l’aborderez de
manière très progressive, en commençant par définir des classes d’objets très
simples, que vous perfectionnerez ensuite. En effet, comme les objets de la
vie courante, les objets informatiques peuvent être très simples ou très
compliqués. Ils peuvent être composés de différentes parties, qui soient
elles-mêmes des objets, ceux-ci étant faits à leur tour d’autres objets plus
simples, etc.

..  tip::

    L'utilisation de classes dans vos programmes vous permettra, entre autres
    avantages, d'éviter au maximum l'emploi de variables globales. Vous devez
    savoir en effet que l'utilisation de variables globales comporte des risques,
    d'autant plus importants que les programmes sont volumineux, parce qu'il est
    toujours possible que de telles variables soient modifiées, ou même
    redéfinies, n'importe où dans le corps du programme. Ce risque s'aggrave
    particulièrement si plusieurs programmeurs différents travaillent sur un même
    logiciel.
