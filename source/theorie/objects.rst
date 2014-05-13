**************************************
Encore des objets, rien que des objets
**************************************

Introduction
============

Dans la vie de tous les jours, vous êtes entouré par une quantité d'objets.
Parce que le logiciel est un modèle qui reflète souvent une certaine réalité,
il est naturel d'introduire des objets dans l'informatique. C'est ce qu'on
appelle la programmation orientée objet (POO). Ce **paradigme de
programmation** s'est imposé depuis deux décennies dans le génie logiciel, à
tel point qu'il est impensable aujourd'hui de développer un projet
informatique sans passer en n'utilisant pas la programmation orientée objets.
Dans ce chapitre, vous allez apprendre à maitriser les concepts principaux de
cette manière de penser et de programmer en développant quelques jeux célèbres.

Sans le savoir, vous avez déjà rencontré plusieurs objets dans votre vie de
programmeur/se : les chaines de caractères, listes, dictionnaires et tuples en
sont de bons exemples.

..
    Vous avez déjà rencontré comme un objet de la tortue . Une tortue a des
    propriétés ( il a une certaine couleur , est situé à une certaine position et
    a un point de vue particulier ) et des capacités ( il peut aller de l'avant ,
    tourner , etc.) Dans la POO objets sont regroupés avec des caractéristiques et
    des capacités similaires dans les classes . Les objets appartiennent à la
    Tortue Tortue de classe , on dit aussi , sont des instances de la tortue de
    classe . Pour créer un objet , vous devez définir une classe ou utiliser une
    classe pré- définie comme tortues premier .

    Lorsque la programmation est appelé les propriétés des attributs aussi ou
    variables d'instance , les compétences et les opérations ou méthodes . Il
    existe des variables et des fonctions , à l'exception qu'ils appartiennent à
    une classe particulière et donc « encapsulés » dans la classe . Pour
    l'utiliser en dehors de la classe , vous devez préfixer une instance de la
    classe et de l'opérateur point .


``JGameGrid`` : notre espace jeux
=================================

Sans POO, il n'est pas possible de créer un jeu d'ordinateur sans se prendre
la tête, car le concepteur de jeux va forcément traiter les personnages du jeu
et les autres objets du plateau de jeu comme des objets. Le plateau de jeu est
une fenêtre d'écran rectangulaire modélisée par la classe ``GameGrid`` de la
Bibliothèque de jeux ``JGameGrid``. Avec un appel à la fonction ``makeGameGrid()``, on construit une *instance* (un exemplaire) de la classe ``GameGrid`` et la méthode ``show()`` permet d'afficher la fenêtre à l'écran. Il est possible de personnaliser  l'apparence de la fenêtre de jeu avec des paramètres appropriés


Code à tester
-------------

Avec ``makeGameGrid(10, 10, 60, Color.red, "sprites/town.jpg", False)``, on
peut afficher une fenêtre dans laquelle on pourra développer nos jeux.

*   Les trois premiers paramètres indiquent que la fenêtre va contenir une
    grille de :math:`10 \times 10` cellules carrées qui font 60 pixels de côté.

*   Le paramètre ``Color.red`` crée le grillage rouge qui montre la grille pendant la phase de
    développement mais il est possible de le supprimer par la suite.

*   Le fichier image ``sprites/town.jpg`` correspond au fond d'écran sur lequel va se dérouler le jeu

*   Le dernier paramètre gère l'affichage de la barre de navigation qui n'est pas nécessaire dans cet exemple
        

..  admonition:: Exécuter le code

    Pour exécuter les codes Python présentés dans ce chapitre, il faut les
    coller dans l'environnement *TigerJython* qui est un Python légèrement
    modifié suivant la version 2.7 du langage.

    Pour vous assurer que tout fonctionne correctement, essayez d'exécuter le code suivant dans *TigerJython* :

    ..  code-block:: python

        from gamegrid import *

        makeGameGrid(10, 10, 60, Color.red, "sprites/town.jpg", False)
        show()

..  admonition:: Memo

    Les méthodes de la classe ``GameGrid`` sont mises à ta disposition par la
    fonction ``makeGameGrid()``. Il est cependant également possible de créer
    une instance de ``GameGrid`` et d'appeler ses méthodes en utilisant
    l'opérateur point.

    ::

        from gamegrid import *

        gg = GameGrid(10, 10, 60, Color.red, "sprites/town.jpg", False)
        gg.show()


    *   La fenêtre de jeu est faite de cellules carrées de 60 pixels de côté.
    *   Il y a 10 cellules horizontales et 20 cellules verticales
    *   Puisque les lignes de la grilles sont affichées également tout en bas et tout à droite, la fenêtre a une taille de 601 x 601 pixels.
        Cela correspondant à la taille minimale de l'image d'arrière-plan
    *   Le dernier paramètre booléen détermine si une barre de navigation apparaît.
        
Définir une classe par dérivation
=================================

Lors de la définition d'une classe, tu peux décider si ta nouvelle classe doit
être indépendante des classes existantes ou s'il faut la dériver d'une classe
existante . Dans une classe dérivée, toutes les méthodes et attributs de la
classe de base (on parle également de *Super classe* ) sont disponibles.

Dans la bibliothèque de jeux ``JGameGrid``, les personnages de jeu et objets
animés sont appelés des *acteurs* et sont des instances de la classe
prédéfinie ``Acteur`` prédéfini. Donc, si tu veux définir un nouveau
personnage de jeu, il faut créer une nouvelle classe qui dérive de la classe
``Actor``.

La définition d'une nouvelle classe débute par le mot-clé ``class``, suivi du
nom de la classe arbitrairement sélectionnable et une paire tour de
parenthèses . Là, vous écrivez le nom de la classe à partir de laquelle vous
ableitest votre classe . Puisque vous voulez tirer le caractère de Acteur ,
vous donnez sur ce nom de classe .

La définition de la classe contenant la définition des méthodes qui sont définies comme des fonctions normales , à la différence près qu'elles ont besoin d'être rempli a le paramètre de soi que le premier paramètre. Avec ce paramètre , vous pouvez accéder à d'autres méthodes et variables d'instance de sa propre classe et sa classe de base .

La liste des définitions de méthode commence généralement par la définition d'une méthode spéciale nommée __ init__ ( deux avant et arrière Sous Lignes ) . C'est ce qu'on appelle un constructeur et il sera appelé automatiquement quand un objet de la classe est créée . Dans notre cas , vous appelez le constructeur de Alien au constructeur de la classe de base Acteur , que vous abandonnez le chemin de l'image du sprite .

Ensuite, vous définissez la méthode acte ( ) . Celui-ci joue pour l'animation de jeu un rôle central , car il est automatiquement appelée par le gestionnaire de jeu dans chaque cycle de simulation . C'est un truc particulièrement intelligent , vous n'avez donc pas à vous soucier d'un motif répétitif lui-même pour l'animation.

Dans l'acte ( ) vous mettez l'action qui devrait rendre le personnage de jeu dans chaque cycle de simulation . Comme une démonstration vous déplacez ici que move () à la cellule suivante . Depuis move () est une méthode de l'acteur de classe de base , vous devez les appeler auto lettre préfixe .

Avez-vous déjà défini votre classe Alien , de sorte que vous générer un objet étranger en composant le nom de la classe et l'affecte à une variable . Typique de la POO , c'est que vous pouvez bien sûr créer autant étrangers . Comme dans la vie de tous les jours , ceux-ci ont leur propre individualité , «savoir» , c'est la façon dont ils doivent se déplacer .

Pour insérer les étrangers créent le plateau de jeu , vous utilisez addActor ( ) , où vous devez indiquer les coordonnées de la cellule avec l'emplacement ( ) ( la cellule avec les coordonnées (0,0) est en haut à gauche , prend x à gauche, y vers ) . Pour démarrer le cycle de simulation , vous appelez enfin sur doRun ( ) .