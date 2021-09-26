# Description des méthodes pour grid.py
*Pour plus de clareté dans le code nous allons déporter les indications dans ce fichier*

## SudokuGrid
Cette classe représente une grille de Sudoku.
Toutes ces méthodes sont à compléter en vous basant sur la documentation fournie en docstring.

### __init__ 
Ce constructeur initialise une nouvelle instance de la classe SudokuGrid.
Il doit effectuer la conversation de chaque caractère de la chaîne en nombre entier,
et lever une exception (ValueError) si elle ne peut pas être interprétée comme une grille de Sudoku.
:param initial_values_str: Une chaîne de caractères contenant **exactement 81 chiffres allant de 0 à 9**,où ``0`` indique une case vide
:type initial_values_str: str

### from_file
Cette méthode de classe (ou méthode statique) crée une nouvelle instance de grille de Sudoku
à partir d'une ligne contenue dans un fichier.
:param filename: Chemin d'accès vers le fichier à lire
:param line: Numéro de la ligne à lire
:type filename: str
:type line: int
:return: La grille de Sudoku correspondant à la ligne donnée dans le fichier donné
:rtype: SudokuGrid

### from_stdin
Cette méthode de classe crée une nouvelle instance de grille de Sudoku
à partir d'une ligne lu depuis l'entrée standard (saisie utilisateur).
*Variante avancée: Permettez aussi de «piper» une ligne décrivant un Sudoku.*
:return: La grille de Sudoku correspondant à la ligne donnée par l'utilisateur
:rtype: SudokuGrid

### __str__
Cette méthode convertit une grille de Sudoku vers un format texte pour être affichée.
:return: Une chaîne de caractère (sur plusieurs lignes...) représentant la grille
:rtype: str

### get_row
Cette méthode extrait une ligne donnée de la grille de Sudoku.
*Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
:param i: Numéro de la ligne à extraire, entre 0 et 8
:type i: int
:return: La liste des valeurs présentes à la ligne donnée
:rtype: list of int

### get_col
Cette méthode extrait une colonne donnée de la grille de Sudoku.
*Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
:param j: Numéro de la colonne à extraire, entre 0 et 8
:type j: int
:return: La liste des valeurs présentes à la colonne donnée
:rtype: list of int

### get_region
Cette méthode extrait les valeurs présentes dans une région donnée de la grille de Sudoku.
*Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
:param reg_row: Position verticale de la région à extraire, **entre 0 et 2**
:param reg_col: Position horizontale de la région à extraire, **entre 0 et 2**
:type reg_row: int
:type reg_col: int
:return: La liste des valeurs présentes à la colonne donnée
:rtype: list of int

### get_empty_positions
Cette méthode renvoit les positions des cases vides dans la grille de Sudoku,
sous la forme de tuples ``(i,j)`` où ``i`` est le numéro de ligne et ``j`` le numéro de colonne.
*Variante avancée: Renvoyez un générateur sur les tuples de positions ``(i,j)`` au lieu d'une liste*
:return: La liste des positions des cases vides dans la grille
:rtype: list of tuple of int

### write
Cette méthode écrit la valeur ``v`` dans la case ``(i,j)`` de la grille de Sudoku.
*Variante avancée: Levez une exception si ``i``, ``j`` ou ``v`` ne sont pas dans les bonnes plages de valeurs*
*Variante avancée: Ajoutez un argument booléen optionnel ``force`` qui empêche d'écrire sur une case non vide*
:param i: Numéro de ligne de la case à mettre à jour, entre 0 et 8
:param j: Numéro de colonne de la case à mettre à jour, entre 0 et 8
:param v: Valeur à écrire dans la case ``(i,j)``, entre 1 et 9


### copy
Cette méthode renvoie une nouvelle instance de la classe SudokuGrid,
qui doit être une copie **indépendante** de la grille de Sudoku.
*Variante avancée: vous pouvez utiliser ``self.__new__(self.__class__)`` pour court-circuiter l'appel à ``__init__`` et manuellement initialiser les attributs de la copie.*
:return: Une copie de la grille courrante
:rtype: SudokuGrid