
######################
Les exceptions
######################


..  admonition:: Source
    :class: important

    Cette section est une traduction quasi mot à mot de la version anglaise sur
    https://runestone.academy/runestone/static/csud-oci1719-thinkcspy/Exceptions/01_intro_exceptions.html


Qu'est-ce qu'une exception?
===========================

Une exception est le signal témoignant qu'il est survenu  une condition ne
pouvant pas être facilement gérée à l’aide du flux de contrôle normal d’un
programme Python. Les exceptions sont souvent définies comme des «erreurs», mais
ce n'est pas toujours le cas. Toutes les erreurs en Python sont traitées à
l'aide d'exceptions, mais toutes les exceptions ne sont pas nécessairement des
erreurs.

Gestion des exceptions
======================

Pour comprendre le rôle d’une exception, il faut se rappeler le fonctionnement
du **flux de contrôle** normal dans un programme Python. Normalement, Python
exécute les instructions les unes après les autres. Il y a cependant trois
constructions de programmation qui vont interrompre cette exécution séquentielle
: les branchements conditionnels, les boucles et les invocations de fonctions.

*   Pour les instructions ``if``, un seul des blocs d’instructions est exécuté, puis
    le flux de contrôle passe à la première instruction suivant la structure ``if``.

*   Pour les boucles, lorsque la fin de la boucle est atteinte, le flux de contrôle
    revient au début de la boucle et un test est utilisé pour déterminer si la
    boucle doit être exécutée à nouveau. Si la boucle est terminée, le contrôle de
    flux passe à la première instruction après la boucle.

*   Pour les appels de fonction, le flux de contrôle saute à la première
    instruction de la fonction appelée, la fonction est exécutée et le flux de
    contrôle revient à l'instruction suivante après l'appel de la fonction.

Voyez-vous le motif? Si le flux de contrôle n'est pas purement séquentiel, il
exécute toujours la première instruction immédiatement après le flux de contrôle
modifié. C'est pourquoi nous pouvons dire que le flux de contrôle Python est
séquentiel. Mais il existe des cas où ce flux de contrôle séquentiel ne
fonctionne pas bien. Voyons pourquoi à l'aide d'un exemple :

Supposons qu’un programme contienne une logique complexe correctement subdivisée
en fonctions. Le programme est en cours d'exécution et exécute actuellement la
fonction ``D``, appelée par la fonction ``C``, appelée par la fonction ``B``,
appelée par la fonction ``A``, appelée elle-même à partir de la fonction
principale. Ceci est illustré par l'exemple de code simpliste suivant:

..  code-block:: python

    def main()
        A()

    def A():
        B()

    def B():
        C()

    def C():
        D()

    def D()
        # processing


La fonction ``D`` détermine que le traitement en cours ne fonctionnera pas pour
une raison quelconque et doit envoyer un message à la fonction principale pour
que celle-ci puisse essayer quelque chose de différent. Cependant, tout ce que
la fonction ``D`` peut faire en utilisant un contrôle de flux normal est de
renvoyer une valeur à la fonction ``C``. La fonction ``D`` renvoie donc une
valeur spéciale à la fonction ``C`` qui signifie «essayer autre chose». La
fonction ``C`` doit reconnaître cette valeur, quitter son traitement et renvoyer
la valeur spéciale à la fonction ``B``. Et ainsi de suite. Il serait très utile
que la fonction ``D`` puisse communiquer directement avec la fonction principale
(ou les fonctions ``A`` et ``B``) sans devoir envoyer cette valeur spéciale via
les fonctions d’appel intermédiaires. C'est exactement le rôle des exceptions.
Une exception est un message à n’importe quelle fonction actuellement dans la
**pile d'appel** du programme en cours d’exécution. (La **pile d'appels** permet
garder la trace des appels de fonctions actifs pendant l'exécution d'un
programme.)

En Python, vous créez un message d'exception à l'aide de la commande ``raise``.
La syntaxe lae plus simple pour une déclencher une exception (on dit **lever**
une exception) est le mot clé ``raise``, suivi du nom d'une exception. Par exemple:

..  code-block::

    raise ExceptionName

lève une exception de type ``ExceptionName``. Alors, qu'advient-il d'un message
d'exception après sa création? Le flux de contrôle normal d'un programme Python
est interrompu et Python commence à rechercher tout code dans sa pile
d'exécution qui est intéressé par le traitement du message. Il recherche
toujours à partir de son emplacement actuel au bas de la pile d'exécution, en
haut de la pile, dans l'ordre dans lequel les fonctions ont été appelées à
l'origine. Un bloc ``try: ... except:``  est utilisé pour dire «hé, je peux
gérer ce message». Le premier bloc ``try: except:`` que Python trouve en
remontant la pile d'appel sera exécuté. S'il aucune bloc ``try: except:`` n'est
trouvé., le programme “se plante” et affiche sa pile d'exécution sur la console.

Jetons un coup d’œil à plusieurs exemples de code pour illustrer ce processus.
Si la fonction ``D`` avait un bloc ``try: except:`` entourant le code qui a
occasionné une exception, ``MyException``, le flux d'exécution aurait été passé
à ce bloc ``try: except:`` et la fonction ``D`` traiterait ses propres
problèmes.

..  code-block:: python

    def main()
        A()

    def A():
        B()

    def B():
        C()

    def C():
        D()

    def D()
        try:
            # processing code
            if something_special_happened:
                raise MyException
        except MyException:
            # execute if the MyException message happened

Mais peut-être que la fonction ``C`` est mieux placés pour gérer le problème, et
on pourrait alors mettre le bloc ``try: except:`` dans la fonction ``C``:

..  code-block:: python

    def main()
        A()

    def A():
        B()

    def B():
        C()

    def C():
        try:
            D()
        except MyException:
            # execute if the MyException message happened

    def D()
        # processing code
        if something_special_happened:
            raise MyException


Mais peut-être que, finalement, c'est la fonction principale qui est la mieux
placés pour gérer le problème, et on pourrait alors mettre le bloc ``try:
except:`` dans la fonction ``main``:

..  code-block:: python
    def main()
        try:
            A()
        except MyException:
            # execute if the MyException message happened

    def A():
        B()

    def B():
        C()

    def C():
        D()

    def D()
        # processing code
        if something_special_happened:
            raise MyException

..  admonition:: Résumé
    :class: info

    En résumé, une exception est un message qui indique que quelque chose de
    spécial s'est produit et que le flux de contrôle normal doit être abandonné.
    Lorsqu'une exception est déclenchée, Python recherche dans sa pile
    d'exécution un bloc ``try: except:`` qui peut traiter la condition de
    manière appropriée. Le premier bloc ``try: except:`` qui prétend savoir
    comment traiter le problème est exécuté, puis le flux de contrôle revient à
    son exécution séquentielle normale. Si aucun bloc ``try: except:`` approprié
    n’est trouvé, le programme “se plante” et affiche sa pile d’exécution sur la
    console.

    Comme dernier exemple, voici un programme qui se plante car aucun bloc
    ``try: except:`` valide  n’a été trouvé pour traiter le message
    ``MyException``. Notez que le bloc ``try: except:`` dans la fonction
    principale sait seulement comment traiter les exceptions ``ZeroDivisonError``
    mais pas les exceptions ``MyException``.


Exceptions standard
====================

La plupart des * exceptions * standard intégrées à Python sont répertoriées ci-dessous.
Ils sont organisés en groupes liés en fonction du type de problèmes qu’ils traitent.



=====================  ================================================
Language Exceptions    Description
=====================  ================================================
``StandardError``      Classe de base pour toutes les exceptions intégrées (built-in) excepté 
                       ``StopIteration`` et ``SystemExit``.
``ImportError``	       Levée lorsqu'une instruction ``import`` ne échoue.
``SyntaxError``        Levée lorsqu'il y a une erreur de syntaxe Python.
``IndentationError``   Levée lorsqu'il y a des erreurs d'indentation.
``NameError``          Levée lorsqu'un identifiant n'est pas trouvé dans l'espace de noms local ou global.
``UnboundLocalError``  Levée lorsqu'un instruction tente d'accéder à une variable locale dans une fonction ou méthode et qu'aucune valeur ne lui a encore été assignée.
``TypeError``          Levée lorsque le programme tente d'effectuer une opération ou d'appeler une fonction invalie pour le type de données en question.
``LookupError``        Classe de base pour toutes les erreurs de type *lookup*.
``IndexError``         Levée lorsqu'un indice n'est pas trouvé dans une séquence.
``KeyError``           Levée lorsque la clé en question n'est pas trouvée dans le dictionnaire.
``ValueError``         Levée lorsque le paramètre passé à une fonction est d'un type correct mais que la valeur est invalide.
                       
``RuntimeError``	   Levée lorsque le programme produit une erreur qui ne tombe dans aucune autre catégorie.
``MemoryError``        Levée lorsqu'une opération occassionne un dépassement de mémoire (plus de mémoire disponible).
``RecursionError``     Levée lorsque la profondeur maximale de la récursion est dépassée.
``SystemError``        Levée lorsque l'interpréteur se prduit une erreur interne. Lorsque cette erreur survient, l'interpréteur Python ne quitte pas.
=====================  ================================================

=====================  ================================================
Exceptions Math        Description
=====================  ================================================
``ArithmeticError``	   Classe de base pour toutes les erreurs qui surviennent lors de calculs numériques. On sait qu'une erreur s'est produit mais on ne sait pas laquelle précisément.
``OverflowError``      Levée lorsqu'un calcul produit un nombre qui excède la capacité d'un type numérique.
``FloatingPointError`` levée lorsq'un calcul en virgule flottante échoue.
``ZeroDivisonError``   levée lorsqu'une division ou une opération de modulo par zéro est effectuée.
=====================  ================================================

=====================  ================================================
Exceptions d'I/O       Description
=====================  ================================================
``FileNotFoundError``  Levée lorsque le programme tente d'ouvrir un fichier ou un dossier qui n'existe pas.
``IOError``            Levée lorsqu'une opération d'entrée/sortie échoue, telle que l'instruction ``print`` ou un appel à la fonction ``open()`` pour essayer d'ouvrir un fichier qui n'existe pas. Également levée pour des erreurs liées au système d'exploitation.
``PermissionError``    Levée lorsque le programme tente d'effectuer une opération mais ne dispose pas des droits nécessaires.
``EOFError``           Levée lorsqu'il n'y a plus de données à lire sur l'entrée standard pour la fonction ``input````raw_input()`` et que la fin du fichier est atteinte.
                       
``KeyboardInterrupt``  Levée lorsque l'utilisation interrompt l'exécution du programme avec les touches ``Ctrl+c``.
=====================  ================================================

=====================   ================================================
Autres Exceptions       Description
=====================   ================================================
``Exception``           Classe de base pour toutes les exceptions. Ceci intercepte la plupart des exceptions.
``StopIteration``       Levée lorsque la méthode ``next()`` d'un intérateur ne pointe pas vers un objet.
``AssertionError``      Levée lorsqu'une instruction ``assert`` échoue.
``SystemExit``          Levée lorsque l'interpréteur Python est quitté avec ``sys.exit()``. Si cette exception n'est pas gérée dans le code, elle cause la fermeture de l'interpréteur.
``OSError``             Levée pour les erreurs liées au système d'exploitation.
``EnvironmentError``    Classe de base pour toutes les exceptions qui surviennent en-dehors de l'environnement Python.
``AttributeError``      Levée en cas d'échec d'une référence d'attribut (variable d'instance ou de classe) ou d'une opération d'assignation.
``NotImplementedError`` Levée lorsqu'une méthode abstraite qui devrait être redéfinie dans une classe fille n'est en réalité pas redéfinie.
=====================   ================================================

Toutes les exceptions sont des objets. Les classes qui définissent les objets
sont organisées dans une hiérarchie montrée ci-dessous. Ceci est important car
la classe parente d'un ensemble d'exceptions interceptera tous les messages
correspondant à sa propre classe ou à ses classes filles. Par exemple, une
exception  ``ArithmeticError`` va gérer toutes les exceptions
``FloatingPointError``, ``OverflowError``, et  ``ZeroDivisionError``.

.. code-block:: Python

  BaseException
   +-- SystemExit
   +-- KeyboardInterrupt
   +-- GeneratorExit
   +-- Exception
        +-- StopIteration
        +-- StopAsyncIteration
        +-- ArithmeticError
        |    +-- FloatingPointError
        |    +-- OverflowError
        |    +-- ZeroDivisionError
        +-- AssertionError
        +-- AttributeError
        +-- BufferError
        +-- EOFError
        +-- ImportError
        +-- LookupError
        |    +-- IndexError
        |    +-- KeyError
        +-- MemoryError
        +-- NameError
        |    +-- UnboundLocalError
        +-- OSError
        |    +-- BlockingIOError
        |    +-- ChildProcessError
        |    +-- ConnectionError
        |    |    +-- BrokenPipeError
        |    |    +-- ConnectionAbortedError
        |    |    +-- ConnectionRefusedError
        |    |    +-- ConnectionResetError
        |    +-- FileExistsError
        |    +-- FileNotFoundError
        |    +-- InterruptedError
        |    +-- IsADirectoryError
        |    +-- NotADirectoryError
        |    +-- PermissionError
        |    +-- ProcessLookupError
        |    +-- TimeoutError
        +-- ReferenceError
        +-- RuntimeError
        |    +-- NotImplementedError
        |    +-- RecursionError
        +-- SyntaxError
        |    +-- IndentationError
        |         +-- TabError
        +-- SystemError
        +-- TypeError
        +-- ValueError
        |    +-- UnicodeError
        |         +-- UnicodeDecodeError
        |         +-- UnicodeEncodeError
        |         +-- UnicodeTranslateError
        +-- Warning
             +-- DeprecationWarning
             +-- PendingDeprecationWarning
             +-- RuntimeWarning
             +-- SyntaxWarning
             +-- UserWarning
             +-- FutureWarning
             +-- ImportWarning
             +-- UnicodeWarning
             +-- BytesWarning
             +-- ResourceWarning


Principes d'utilisation des exceptions
======================================

Il y a beaucoup de mauvais exemples d'utilisation *d'exception* sur Internet. Le
but d'une *exception* consiste à modifier le flux de contrôle, pas à intercepter
des erreurs simples. Si votre bloc ``try: except:`` se trouve dans la fonction
qui ``raise`` l'exception, vous utilisez probablement les exceptions de travers.

..  topic :: Principe 1:

    Si une condition peut être gérée à l'aide du flux de contrôle normal,
    n'utilisez pas une exception!

Example 1:

+------------------------------------------+-------------------------------------------+
| **MAUVAIS**:                             | Lorsque vous pouvez tout aussi bien tester|
|                                          | l'absence d'éléments dans la liste avec:  |
+------------------------------------------+-------------------------------------------+
| .. code-block:: Python                   | .. code-block:: Python                    |
|                                          |                                           |
|   try:                                   |   if len(a_list) > 0:                     |
|     average = sum(a_list) / len(a_list)  |     average = sum(a_list) / len(a_list)   |
|   except ZeroDivisionError:              |   else:                                   |
|     average = 0                          |     average = 0                           |
+------------------------------------------+-------------------------------------------+

Example 2:

+------------------------------------------+-------------------------------------------+
| **DON'T DO THIS**:                       | When you can just as easily test for a    |
|                                          | valid index doing this:                   |
+------------------------------------------+-------------------------------------------+
| .. code-block:: Python                   | .. code-block:: Python                    |
|                                          |                                           |
|   try:                                   |   if 0 <= index < len(my_list):           |
|     value = my_list[index]               |     value = my_list[index]                |
|   except IndexError:                     |   else:                                   |
|     value = -1                           |     value = -1                            |
+------------------------------------------+-------------------------------------------+


Example 3:

+------------------------------------------+-------------------------------------------+
| **DON'T DO THIS**:                       | When you can just as easily test          |
|                                          | to see if the key is valid doing this:    |
+------------------------------------------+-------------------------------------------+
| .. code-block:: Python                   | .. code-block:: Python                    |
|                                          |                                           |
|   try:                                   |   if key in my_dictionary.keys():         |
|     value = my_dictionary[key]           |     value = my_dictionary[key]            |
|   except KeyError:                       |   else:                                   |
|     value = -1                           |     value = -1                            |
+------------------------------------------+-------------------------------------------+


..  topic :: Principe 2:

    Si vous appelez une fonction qui génère potentiellement des exceptions et que vous pouvez faire
    quelque chose d'approprié pour traiter l'exception,  entourez le code
    qui contient l'appel de fonction avec un bloc ``try: except:``.

Exemple: supposons que vous ayez une fonction qui lit un fichier pour
initialiser l’état d'une application quand il démarre. Vous devriez attraper les
erreurs liées à la lecture du fichier et définir l'état de l'application aux valeurs
par défaut si elles ne peuvent pas être lues à partir du fichier.

..  code-block:: Python

    try:
        load_state('previous_state.txt')
    except OSError:
        set_state_to_defaults()


..  topic:: Principle 3:

    Si vous appelez une fonction qui génère potentiellement des exceptions et
    que vous ne pouvez rien de d'intelligent avec l'exception levée, alors il
    vaut mieux ne rien faire et la laisser remonter plus loin pour qu'elle
    puisse éventuellement être gérée en amont par une autre fonction.


Syntaxe des exceptions
======================

Il existe de nombreuses variantes pour intercepter les exceptions. Voici un bref
résumé, mais il faut savoir qu'il existe encore d'autres possibilités de le
faire tout-à-fait valides.

Attraper toutes les exceptions
------------------------------

Attrape toutes les exceptions, quel que soit leur type. Cela empêchera votre
programme de planter, mais ce type de gestion des exceptions est rarement utile
car vous ne pouvez rien faire de significatif pour récupérer l'erreur produite
de manière intelligente.

..  code-block:: Python

    try:
        # Your normal code goes here.
        # Your code should include function calls which might raise exceptions.
    except:
        # If any exception was raised, then execute this code block.


Attraper une exception spécifique
---------------------------------

C'est peut-être la syntaxe la plus souvent utilisée. Il attrape une condition
spécifique et tente de gérer l'erreur de manière intelligente et pertinente.


.. code-block:: Python

    try:
        # Your normal code goes here.
        # Your code should include function calls which might raise exceptions.
    except ExceptionName:
        # If ExceptionName was raised, then execute this block.

Attraper plusieurs exceptions spécifiques
-----------------------------------------

.. code-block:: Python

    try:
        # Your normal code goes here.
        # Your code should include function calls which might raise exceptions.
    except Exception_one:
        # If Exception_one was raised, then execute this block.
    except Exception_two:
        # If Exception_two was raised, then execute this block.
    else:
        # If there was no exception then execute this block.


Nettoyage après les exceptions
------------------------------

Si vous avez du code que vous voulez exécuter même si des exceptions se
produisent, vous peut inclure un bloc de code ``finally``:

.. code-block:: Python

    try:
        # Your normal code goes here.
        # Your code might include function calls which might raise exceptions.
        # If an exception is raised, some of these statements might not be executed.
    finally:
        # This block of code will always execute, even if there are exceptions raised


Un exemple d'entrée / sortie de fichier
---------------------------------------

Une situation nécessitant une gestion d'exception systématique est la lecure ou
l'écriture dans un fichier. Voici un exemple typique de traitement de fichier.
Notez que le bloc externe ``try: except:`` s’occupe d’un fichier manquant ou
le fait que le fichier existant ne puisse pas être ouvert en écriture. Le bloc
``try: except:`` intérieur protège contre les erreurs de sortie, telles que
l'écriture sur un périphérique plein. Le code ``finally`` garantit que le
fichier sera fermé correctement même en cas d'erreur lors de l'écriture.


.. code-block:: Python

    try:
        f = open("my_file.txt", "w")
        try:
        f.write("Writing some data to the file")
        finally:
        f.close()
    except IOError:
        print "Error: my_file.txt does not exist or it can't be opened for output."

.. index:: exceptions syntax

Glossaire
=========

*   exception : Une erreur qui se produit au moment de l'exécution.

*   gérer une exception : Pour empêcher une exception de terminer un programme en encapsulant le bloc de code dans une construction ``try`` / ``except```.

*   lever : Pour provoquer une exception en utilisant l'instruction ``raise``.