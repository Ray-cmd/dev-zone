# ZSH c'est quoi ?

**ZSH** est une alternative a **Bash**. Il est Open source et est plus récent que **Bash**. Il permet d'utiliser des thème et des plugins en plus de proposer des fonctionnalités très puissantes. **ZSH** est maintenu par une communauté impressionnante de plus de 1300 contributeurs ! 

Il met par exemple a disposition la commande *z* qui permet de très facilement chercher un dossier ou un fichier sur le système. Il permet aussi la correction d'orthographe. 

# Installation
Pour installer **ZSH** sur un distribution Linux, il suffit dans la plupart  des cas d'utiliser le gestionnaire de paquets par défaut. Par exemple:
```bash
sudo apt-get install zsh -y
```
Un foi que **ZSH** est installé, nous pouvons le lancer avec la commande :
```bash
zsh
```

Lors de la première utilisation, il nous est demander si nous voulons que **ZSH** créer un fichier de configuration pour nous.
| Option | Description |
| ------ | ----------- |
| q      | Quitte **ZSH** sans rien faire. Quand vous relancerez **ZSH**, cette configuration vous sera de nouveau présentée |
| 0      | Quitte **ZSH** et crée un fichier .zshrc avec comme seul contenu un commentaire Cela a pour effet ne plus demander la configuration |
| 1      | Affiche un menu qui permet de configurer plus finement **ZSH** |
| 2 | Crée un fichier .zshrc qui contient une petite configuration de base |

# Configurer ZSH
La configuration de **ZSH** se fait dans le fichier *.zshrc*. Ce fichier doit se trouver à la racine de notre répertoire *home*. Il se peu que se fichier n'existe pas, cela dépende de option que vous avez choisi lors du premier lancement. Donc, si nous le trouvons pas à la racine de notre *home*, il faut relancer **ZSH** et choisir l'option 0 ou 2. 0 va créer .zshrc avec pour seul contenu un commentaire alors que 2 va créer .zshrc avec une configuration minimale de base.

Afin d'éditer le fichier *.zshrc*, il faut utiliser un éditeur, ici je vais utiliser **nano** . Tous les éditeurs traditionnel feront l'affaire, suivez vos préférances.
```zsh
nano ~/.zshrc
```

Ce fichier peu être très simple comme très complexe en fonction de vos besoins. Afin de connaitre toutes les configurations possible, il faut se rendre sur la [documentation](http://zsh.sourceforge.net/Doc/Release/zsh_toc.html)



