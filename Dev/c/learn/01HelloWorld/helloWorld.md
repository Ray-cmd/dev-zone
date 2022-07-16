# Hello World

Le but de ce dossier et de documenter mon apprentissage du language C.

Le language C est très courant, il a l'avantage d'avoir une syntaxe assez simple et qui s'assimile assez vite toute en restant proche du hardware. Il n'y a pas de garbage collector en C, il faut faire la gestion de la mémoire à la main. Cela permet d'optimisé les logiciels afin et d'atteindre une vitesse d'execution très élevée.

Chaque programme en C doit contenir une fonction main. C'est fonction représente le point d'entrée de l'application. Elle dois aussi forcement retourner un integer. Chaque programme dois donc comporter les lignes suivantes:

```c
int main() {
    // Mettre le code ici
    return 0;
}
```

`int` est la pour détérmier le type de la valeur retournée. Nous avons dit plus haut que la fonction main devait retourner un integer.

`main` est le nom de la fonction, ici, nous voulons créer le point d'entrée dans l'applicaton, nous devons donc impérativement appeler la fonction que cela.

`()` permet de stipuler les paramètres de la fonction, ici, nous n'en prennont aucun.

`{}` définisse le scope de la fonction. Touts le code qui est dedant sera executé lorsque la fonction est appelées.

`return 0` est la valeur que retourne la fonction. Il faut mettre cette instruction à la fin de la fonction car dès quel sera executée, la fonction sera quittée. Nous retournont la valeur 1, c'est une convention afin de  dire que le programe c'est bien executé.

Maintenant que nous avons la structure de base de notre programme, nous allons pouvoir ajouter des instruction afin qu'il puisse faire des choses. Ici, nous allons afficher **Hello World !**. Pour se faire, nous allons devoir faire appel à la fonction `printf()`. Cette fonction permet d'afficher du texte dans la console. Afin de pouvoir faire un executable le plus légé possible, C n'intégre pas beaucoup de fonctionalité de base. Ceci permet de faire des programme pour des environnemet qui ont très peu de mêmoire, comme par exemple, des micro controller. Pour parrer a ce problème, C est doté d'une librairie de base qui permet d'ajouter des fonctionnalité au language. Pour pouvoir utiliser la fonction `printf()`, nous devons importer le module de la bibliothèque standard qui s'ocuppe des entrée, sortie. Ce module s'appel **stdio** et nous allons devoir demandé au préprocesseur de l'include. Je ne vais pas rentrer dans les détail, mais en bref, le préprocesseur permet d'automatiser des actions en amont de la compilation. Ici, il va s'occuper d'inclure la bibliothèque. Une instruction pour le préprocesseur se met en haut du fichier. Elle doit être précédée d'un **#** et ne pas se finir par un ;.

```c
#include <stdio.h>
```

Ici, nous avons demander au préprocesseur d'importer **stdio.h**. l'extention **.h** correspond à un ficher header. C'est un fichier qui donne les instructions sur comment importer le module. Nous verrons aussi plus loins comment créer un module et rédiger un fichier header.

Maintenant que nous avons importer la bibliothèque, nous pouvons utiliser la fonction `printf()`.

```c
#include <stdio.h>

int main() {
    printf("Hello World");
    return 0;
}
```

Nous avons maintenant un programme prêt à être compilé ! En plus de la structure de base que doit comporter chaque programme, nous avons utiliser la fonction `printf()` afin d'afficher du texte. Nous devont entourer le texte de guiellmet. Cela permet de faire comprendre au compialteur que nous voulons afficher le texte et non pas le contenu d'une variable par exemple.
