# Variables et types

C comporte beaucoup de types de variables, mais il y a quelque types basique:

- Entiers - Nombre positif ou négatif. Ce définit en utilisant `char`, `int`, `short`, `long` ou `long long`.
- Entiers non signé - Nombre qui peut uniquement être prositif. Ce définit en utilisant `unsigned char`, `unsigned int`, `unsigned short`, `unsigned long` ou `unsigned long long`.
- Nombre à virgule flotante - Nombre réel (nombre avec fractions). Ce définit en utilisant `float` ou `double`.
- Structure - Nous allons en parler plus tard.

Voici un tableau récapitulatif de la taille de chaque type d'entier ainsi que le range de valeur qu'il peut contenire:

|Type          |Taille      |Range de valeur                           |
|--------------|------------|------------------------------------------|
|char          |1 byte      |-128 à 127                                |
|unsigned char |1 byte      |0 à 255                                   |
|int           |2 ou 4 bytes|-2147483648 à 2147483647                  |
|unsigned int  |2 ou 4 bytes|0 à 4294967295                            |
|short         |2 bytes     |-32768 à 32767                            |
|unsigned short|2 bytes     |0 à 65535                                 |
|long          |4 ou 8 bytes|-9223372036854775808 à 9223372036854775807|
|unsigned long |4 ou 8 bytes|0 à 18446744073709551615                  |

> Ces chiffres peuvent varier en fonction de l'architecture du proceesseur.

Voici le même tableau, mais cette fois ci, pour les nombres à virgules flotantes :

|Type   |Taille |Range de valeur            |Précision     |
|-------|-------|---------------------------|--------------|
|float  |4 bytes|1.17549e-38 à 3.40282e+38  |6 décimales   |
|double |8 bytes|2.22507e-308 à 1.79769e+308|15 décimales  |

> Ces chiffres peuvent varier en fonction de l'architecture du proceesseur.

Vous avez peu être remarqué que nous n'avons pas parlé des bolléans. C'est parsque C n'utilse pas ce type. Nous pouvons simuler ce fonctionnement en ajoutant ces instruction pour le préprocesseur :

```c
#define BOOL char
#define FALSE 0
#define TRUE 1
```

Pour les strings, C utilise des tableaux de char.

## Déclarer une variable

Maintenant que nous en avons vu plus sur les type, nous allons voir comment déclarer une variable. Pour ce faire, nous avons besoin de lui donner un type et un nom, nous pouvons aussi lui donner une valeur lors de la déclaration.

```c
int maVariable = 42;
```

Nous voyons donc, que pour déclarer une variable, nous commencont par lui donner un type, puis un nom, nous pouvons aussi utiliser le `=` pour lui affecter une valeur. Ceci est tout a fait valable :

```c
int maVariable;
```

## Afficher la valeur d'une variable

Nous avons vu que nous pouvions utiliser `printf()` pour afficher un texte. Nous pouvons aussi l'utiliser pour afficher des informations sur des variables. Pour se faire `printf()` utilise un système de paterne bien pratique. Il est un peu difficile a appréander mais il est très puissant.