# C'est quoi docker ?

*Docker est un outil qui peut empaqueter une application et ses dépendances dans un conteneur virtuel, qui pourra être exécuté sur n'importe quel serveur Linux*

## C'est quoi un conteneur ?

Le concept de conteneur n'a pas été inventé avec Docker. Linux, par exemple utilise des conteneur grâce à LXC.

Pour ce représenter un conteneur, nous pouvons nous imaginer une sorte de boite, un peu comme une machine virtuelle qui va être complètement isolé du système d'exploitation. Dans cette boite, nous allons pouvoir installer toute sorte de librairie dont notre application a besoin pour fonctionner, ainsi que l'application.
Une foi que le conteneur est créer, nous pouvons le distribuer et l'application fonctionnera sur toute installation de Docker. Cela est possible grâce au fait, que le conteneur contient toute les dépendance don l'application a besoin.

# Premiers pas

## Différences entre Docker et VM

Une machine virtuelle se repose sur un hyperviseur. Cet hyperviseur fait tourner son propre OS et chaque VM fait tourner également son propre OS.

Docker est plus léger. Il a besoin d'un serveur avec son OS ainsi qu'un *Container Engine* qui est Docker. Ensuite, c'est le Container Engine qui gère les conteneurs. L'avantage de cette architecture est de ne faire tourner qu'un seul système exploitation qui va partager ces ressources avec les conteneurs. Un conteneur faire rarement plus de 1Go alors qu'une VM dépasse très facilement les 10Go.

Cette organisation permet de concevoir des applications sout forme de micro-services. Chaque aspect de l'application tourne dans un conteneur, bases de données, frontend, backend, tout peu être segmenté.

## Installer Docker

Docker est très facile à installer car il est populaire et se retrouve donc dans beaucoup de repository. Nous pouvons donc, dans la majorité des cas utiliser simplement notre gestionnaire de paquet favoris pour l'installer sans rien n'avoir a faire d'autre.

<u>Exemple :</u>

```bash
sudo apt-get update && sudo apt-get install -y docker 
```

## Première utilisation de Docker

Docker se pilote via un outil en ligne de commande qui est réputé très ergonomique. Pour connaitre toute les possibilités de Docker, il vous suffit de taper la commande **docker**. Cette commande, sans argument, renvoie la liste de toutes les commandes qui lui sont associé. 

```bash
> docker
Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/home/luca/.docker")
  -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and
                           default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/home/luca/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/home/luca/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/home/luca/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  engine      Manage the docker engine
  image       Manage images
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.
```

Pour lister lister les conteneurs, il faut utiliser la commande **docker ps**.

```bash
> docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
Actuellement, la liste est vide car je n'ai pas de conteneur en fonctionnement. Il est possible d'ajouter l'argument **-a** (--all) à ps afin d'afficher tous les conteneurs qui ont étés lancé.

```bash
docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                   PORTS               NAMES
8d64fc83438e        ubuntu              "/bin/bash"         5 weeks ago         Exited (0) 5 weeks ago                       relaxed_kalam
255aba2bf36a        ubuntu              "/bin/bash"         5 weeks ago         Exited (0) 5 weeks ago                       friendly_mayer
1b1133de6982        django              "python3"           5 weeks ago         Exited (0) 5 weeks ago                       eloquent_almeida
7f3b317d3562        django              "python3"           5 weeks ago         Exited (0) 5 weeks ago                       stoic_saha
cfe8fc9b48f2        django              "-ti"               5 weeks ago         Created                                      funny_meitner
c5ba7dbb65f0        python              "test.py"           5 weeks ago         Created                                      silly_meninsky
372adea9929e        python              "python3"           5 weeks ago         Exited (0) 5 weeks ago                       busy_pascal
3134cad20fdf        python              "python3"           5 weeks ago         Exited (0) 5 weeks ago                       funny_mirzakhani
```

Si vous venez tout juste d'installer Docker et que vous n'avez pas encore lancé de conteneur, cette liste sera vide. Revenez quand nous aurons lancé notre premier conteneur !

## Lancer notre premier conteneur !

Nous allons maintenant faire tourner notre premier conteneur. Nous allons utiliser le conteneur alpine, qui est un système d'exploitation basé sur Linux qui est très léger !

Pour trouver ce conteneur, nous allons utiliser une registerie. Une registerie est une sorte de dépôt ou nous pouvons stocker des conteneurs. Il en existe beaucoup, certaine public, certaine privée. Nous, nous allons utiliser la registerie de référence, [Docker Hub](https://hub.docker.com).

Par défaut, Docker est configuré pour utiliser le Docker Hub, nous n'avons donc rien à faire pour le faire pointer sur la bonne registrie. Nous pouvons donc utiliser directement la commande **docker run** afin de lancer notre conteneur. Docker se charge tout seul de regarder si il a déjà le conteneur ou si il doit aller le chercher sur le Hub et le télécharger.

```bash
> docker run alpine:latest
Unable to find image 'alpine:latest' locally
latest: Pulling from library/alpine
aad63a933944: Pull complete
Digest: sha256:5efa52630498a3d15f969519a5ed6f3ed43bbc720e6d6b6a86a6b80b1009a108
Status: Downloaded newer image for alpine:latest

>
```

Ici, docker nous prévient qu'il n'arrive pas à trouver l'image en local et qu'il va la chercher en ligne sur le Hub. Une foi qu'il l'a trouver, il l'a télécharge et là lance. Il n'est pas facile de voir que docker a lancé l'image car une foi le run exécuté, nous avons de nouveau un prompt. Il c'est bien exécuté mais vu que l'image n'a pas rencontré d'événement elle c'est terminée.

Pour voir que l'image c'est bien lancée et qu'elle n'est actuellement pas en cours de fonctionnement, nous pouvons utiliser la commande **docker ps** et **docker ps -a**.

```bash
> docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

> docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
35ffb822dfd7        alpine:latest       "/bin/sh"           6 minutes ago       Exited (0) 6 minutes ago                       hardcore_williams

```

Ici, **docker ps -a** nous retourne qu'un conteneur a été lancé il y a 6 minutes et qu'il c'est terminé sans erreur.

Si nous voulons que le conteneur ne se ferme pas immédiatement, il faut le lancer en utilisant des paramètre. La commande **docker run -di** (d = détaché et i = interactive) nous permet de lancer le conteneur et d'avoir la main dessus. Nous pouvons aussi spécifier l'argument **--name** afin de donner un nom au conteneur et donc de le rendre plus identifiable (par défaut, Docker attribue un nom aléatoire à chaque conteneur).

```bash
> docker run -di --name exemple alpine:latest
1eac8050d042e929e3460c5d06aa5509c30ab4eb078227b41318abf751771807

>
```

Quand nous exécutons cette commande, le seul résultat qui nous est retourner avant de retomber sur notre prompte est une longue suite de caractère. Cette suite de caractère est en fait l'id du conteneur.



Mais maintenant, comment faire pour utiliser notre conteneur ? Nous pouvons déjà nous assurer qu'il tourne grâce à **docker ps**.

```bash
> docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
1eac8050d042        alpine:latest       "/bin/sh"           2 minutes ago       Up 2 minutes                            exemple
```

Nous pouvons constater que le conteneur est bien entrain de fonctionner. Nous pouvons voir, son id, l'image sur là quelle le conteneur est basé, la commande qui a été exécuté au lancement du conteneur, le temps depuis que le conteneur a été créé, le temps depuis le moment ou le conteneur a été lancé, le port qui est utilisé par le conteneur pour communiquer ainsi que son nom.

Maintenant que nous savons comment créer un conteneur depuis une image et que nous savons comment rendre le fonctionnement du conteneur persistant, il nous faut apprendre à nous y connecter. Pour ce faire, nous utilisons la commande **docker exec**. Cette commande demande des paramètre, nous allons lui spécifier **-ti** (t = tty et i = interactive). Ensuite, nous allons passer le nom ou l'id du conteneur ainsi que la commande à passer (ici sh pour avoir un shell).

```bash
> docker exec -ti exemple sh
/ #
```

Nous voila enfin dans le shell de notre conteneur alpine !  Si vraiment vous voulez être sur que vous êtes bien sur le shell du conteneur et non votre shell local, vous pouvez entrer la commande Linux **ps**.

```bash
> ps
PID   USER     TIME  COMMAND
    1 root      0:00 /bin/sh
   17 root      0:00 sh
   23 root      0:00 ps
```

Nous voyons bien que nous sommes dans un conteneur car il n'y a pas de système qui tourne. Il n'y a que sh qui tourne (nous l'avons lancer lors de la connexion au conteneur) ainsi que ps que nous sommes entrain d'analyser. Vous ne trouverez pas ici de systemd ou init.

# Lancer un conteneur de serveur web (nginx)

Nous allons ici voir un cas concret. Le but va être de lancer un conteneur qui contient un serveur web(nginx). Cela va permet d'introduire la notion d'exposition de ports. Lors du lancement d'un conteneur avec la commande **docker run**, il est possible d'utiliser l'argument **-p<portConteneur>:<portLocal>** afin de définir le port par le quel le conteneur sera joignable.

Pour cette exemple, nous allons créer un conteneur qui se nom web, qui est basé sur la dernière version de l'image de ngix et qui est exposé sur le port 8080.

```bash
> docker run -tid -p 8080:80 --name web nginx:latest
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
68ced04f60ab: Pull complete
28252775b295: Pull complete
a616aa3b0bf2: Pull complete
Digest: sha256:2539d4344dd18e1df02be842ffc435f8e1f699cfc55516e2cf2cb16b7a9aea0b
Status: Downloaded newer image for nginx:latest
8476798c9e4ddde4f86226b99bbd981154343cae627bd7b3a0c783de6e2a73b5
```

Nous pouvons faire un coup de **docker ps** afin de nous assurer que notre conteneur est bien en fonctionnement.

```bash
> docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                  NAMES
c05c04e5057f        nginx:latest        "nginx -g 'daemon of…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp   web
1eac8050d042        alpine:latest       "/bin/sh"                41 hours ago         Up 47 minutes                              exemple
```

Ici, nous pouvons constater que notre conteneur est bien actif. Nous pouvons aussi voir que notre exposition de port c'est bien passé, car la règle est présente dans la colonne PORTS.

## Docker Inspect pour avoir des informations

Maintenant que notre conteneur nginx est en fonctionnement est qu'il répond sur le port 8080, il peu être intéressant d'avoir plus d'informations sur le conteneur. Pour avoir ces informations, il nous faut utiliser **docker inspect <conteneur>**.

```bash
> docker inspect web
...
```

Cette commande nous permet par exemple de trouver l'adresse IP d'un conteneur. Pour ce faire, nous piper le résulta de **docker inspect** dans un grep de IPAddress.

```bash
> docker inspect web | grep IPAddress
            "SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.3",
                    "IPAddress": "172.17.0.3",
```

# Monter un volume persistant et stockez vos données

## Lancer un conteneur stopper

SI vous avez redémarrez votre machine depuis que nous avons lancer le conteneur nginx, vous vous êtes peu être rendu compte qu'il ne tourne plus.

```bash
> docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

Pour redémarrer un conteneur, nous utilisons la commande **docker start <conteneur>**. Si vous ne vous souvenez plus du nom que vous avez donner au conteneur ou son id, vous pouvez utiliser la commande **docker ps -a** afin de le retrouver.

```bash
> docker start web
> docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
c05c04e5057f        nginx:latest        "nginx -g 'daemon of…"   32 minutes ago      Up 4 seconds        0.0.0.0:8080->80/tcp   web
```

Il faut que ce conteneur fonctionne car nous allons l'utiliser comme exemple plus loin.

## Volume persistant

Docker, par défaut, ne stock pas les nouvelles données dans le conteneur. Afin de rendre les données persistantes, nous allons devoir créer un volume qui va faire le lien entre le conteneur et un répertoire de la machine qui héberge Docker.  

Je vais commencer par créer un répertoire sur mon système local qui va contenir toute les données qui devront être persistante de notre conteneur. 

```bash
> mkdir /srv/data/nginx
```

Maintenant que nous avons créer notre répertoire, nous allons supprimer notre conteneur web avec la commande **docker rm -f web** 

```bash
> docker rm -f web
```

Maintenant que notre conteneur n'existe plus, nous allons pouvoir le re-créer avec un nouveau paramètre pour pointer vers notre stockage local. Ce paramètre est **docker run -v <path_local>:<path_conteneur>**.

```bash
> docker run -tid -p 8080:80 -v /srv/data/nginx/:/usr/share/nginx/html/ --name web nginx:latest
```

Maintenant que notre nouveau conteneur est créé, si nous nous rendons à l'adresse *localhost:8080*. nous avons une erreur 403. Cela vient du fait, que ce nouveau conteneur va mapper le dossier de nginx sur un répertoire local qui est vide. Pour que l'erreur 403 n'apparaisse plus, il suffit de rajouter un fichier *index.html* dans */srv/data/nginx*.

Maintenant que vous avez ajouté ce fichier, rendez vous à l'adresse *localhost:8080* et votre fichier html s'affiche !

Nous pouvons noté, que si nous supprimons le conteneur, même avec **docker rm -f**, le fichier html que nous avons créer ne sera pas supprimer car il est en dehors du conteneur !

La procédure que nous venons exécuter et la manière la plus simple de mettre en place un volume. Il en existe d'autres, plus complète, nous les verrons plus loin.

# La commande DOCKER VOLUME

Nous venons de voir comment monter un répertoire distant afin de rendre les données persistante. Nous allons voir ici un moyen plus pousser de faire la même action et cela ce passe avec la commande **docker volume**.

La commande **docker volume** permet l'utilisation de 5 paramètres :

| Paramètre | Description                                        |
| --------- | -------------------------------------------------- |
| create    | Pour créer un volume                               |
| inspect   | Affiche les informations à propos d'un volume      |
| ls        | Liste tous les volumes existant                    |
| prune     | Supprime tous les volumes qui ne sont plus utilisé |
| rm        | Supprime le volumes de votre choix                 |

## Créer un volume

Nous allons commencer par créer un volume. Pour ce faire, nous l'avons vu plus haut, il nous faut utiliser la commande **docker volume create <name_volume>**.

```bash
> docker volume create newvolume
```

Maintenant que notre nouveau volume est créer, nous pouvons le voir en utilisant le paramètre **ls**.

```bash
> docker volume ls
DRIVER              VOLUME NAME
local               newvolume
```

Ici, nous voyons donc la liste de tous nos volumes. Nous n'en avons créer qu'un seul, la liste n'est donc pas très grande.

Le paramètre **ls** permet de lister les volumes mais ne donne aucune précision sur ceux-ci. Pour avoir des infos sur un volume il faut utiliser **docker volume inspect <name_volume>**.

```bash
> docker volume inspect newvolume
[
    {
        "CreatedAt": "2020-03-26T22:05:30Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/newvolume/_data",
        "Name": "newvolume",
        "Options": {},
        "Scope": "local"
    }
]
```

## Utiliser un volume

Maintenant que nous avons créer un volume, il faut l'utiliser. Pour ce faire nous devons créer un nouveau conteneur et spécifié le paramètre **--mount source=<name_volume>,target=<conteneur_path>. Ici, je commence pas supprimer le conteneur *web* que nous avons créé et je le recréer pour qu'il pointe sur le nouveau volume que nous venons de créer.

```bash
> docker stop web
> docker rm web
> docker run -tid --name web -p 8080:80 --mount source=newvolume,target=/usr/share/nginx/html nginx:latest
```

Maintenant, vous pouvez constater avec **docker ps** et en vous rendant sur localhost:8080 que nginx fonctionne bien et qu'il est utilisable.

Pour éditer le fichier index.html afin de le personnalisé, il suffit d'ouvrir et de modifié le fichier */var/lib/docker/volumes/newvolume/_data*.

### Utiliser les volumes sous WSL

Si comme moi vous utilisez WSL pour faire tourner docker, vous risquez d'avoir un problème pour accéder aux volumes. En effet, quand vous utilisez WSL, docker stock les volumes sur la mini machine virtuel qui contient le noyau linux. Il n'est vraiment pas facile d'accéder à cet endroit pour éditer vos fichiers. Je vous conseil donc de bindez un répertoire de la machine hôte comme volume. Pour ce faire, il y a deux méthodes, soit, comme plus haut, vous utiliser le paramètre **-v <path_source>:<path_conteneur>**. Vous pouvez aussi utiliser le paramètre **--mount** comme cela :

```bash
> docker run -tid -p 8080:80 --name web --mount type=bind,source=<path_source>,target=<path_conteneur> nginx:latest
```

Ces deux méthodes font la même chose. utiliser le paramètre **--mount** permet de spécifier les arguments par leur nom et donc de passer les arguments dans l'ordre que nous voulons, alors que **-v** ne le permet pas.

Il faut quand même noté que ces techniques ne permette pas de gérer les volumes avec la commande **docker volume**. Si vous passez la commande **docker volume ls** alors que vous avez monté un volume avec **-v** ou **--mount type=bind**, il apparaitra pas. Dans la majorité des cas, il est recommandé d'utiliser la commande **docker volume** et laisser docker gérer tous seul les volumes. Le fait que nous utilisons un environnement WSL nous pousse à transgresser cette règles afin de pouvoir accéder facilement aux fichiers.

Si vous voulez quand même utiliser **docker volume** sous windows, vous pouvez accéder au répertoire ou est stocker le volume via ce chemin à passer dans votre explorateur *\\\wsl$\docker-desktop-data\mnt\wsl\docker-desktop-data\data\docker\volumes*.

## Supprimer un volume

Pour supprimer un volume, il faut utiliser la commande **docker volume rm <name_volume>**. Attention, nous ne pouvons pas supprimer un volume qui est utilisé par un conteneur. Pour se faire, il faut d'abord supprimer le conteneur.

```bash
> docker rm web
> docker volume rm newvolume
```

# Les variables d'environnement 

Nous allons maintenant, voir comment passer des variables d'environnement à un conteneur via la ligne de commande. Nous devons passer ces variables lors de la création d'un conteneur. Ici, je créer un nouveau conteneur qui se base sur la dernière image d'*Ubuntu*, il portera le nom de *testenv* et recevra une variable d'environnement qui se nom *MYVARIABLE* et qui vaut *123456*.

```bash
> docker run -tid --name testenv --env MYVARIABLE="123456" ubuntu:latest
```

SI vous ne l'avez pas encore, Docker va télécharger la dernière image d'Ubuntu et créer un conteneur avec les paramètre que nous lui avons passer.

Nous pouvons maintenant nous connecter à ce nouveau conteneur afin de nous assurer que la variable d'environnement est bien passée. Pour ce faire, il faut utiliser **docker exec**.

```bash
> docker exec -ti testenv sh
```

Maintenant que nous avons un prompte dans le conteneur, il suffit d'utiliser la commande Linux **env** pour afficher toutes les variables d'environnement.

```bash
> env
HOSTNAME=f77ceeb36753
HOME=/root
TERM=xterm
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MYVARIABLE=123456
PWD=/
```

Nous voyons bien que *MARAIABLE* est présent et qu'elle vaut bien *123456*.

## Passer des informations sensibles

Si vous devez passer des informations sensible (un mot de passe par exemple) à une variable d'environnement, il est possible de passer par un fichier. Cela évite de taper l'information en claire dans le terminal.

La première chose à faire et de créer un fichier avec le nom que vous voulez sur votre machine hôte. Dans ce fichier, nous pouvons ajouter autant de variables d'environnement que nous voulons. Voici un exemple.

```bash
MYLOGIN=admin
MYPASSWORD=password+1234
```

Maintenant que le fichier est prêt, nous pouvons supprimer le conteneur que nous vennons de créer afin de pouvoir le recréer en utilisant notre nouveau fichier.

```bash
> docker rm -f testenv
```

Nous pouvons maintenant recréer le conteneur avec le paramètre **--env-file <path_file>** au lieu d'utiliser **--env**.

```bash
> docker run -tid --name testenv --env-file env.lst ubuntu:latest
```

Il ne faut pas oublier de changer l'argument du paramètre **--env-file** pour qu'il match avec le nom du fichier que vous avez créer.

Si nous reproduisons la procédure que nous avons fait plus haut afin de nous assurer que nos variables sont bien là, nous pouvons constater que tous c'est bien passé.

```bash
> env
HOSTNAME=cf35c04ff9bd
HOME=/root
TERM=xterm
MYLOGIN=admin
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PWD=/
MYPASSWORD=password+1234
```

Nous pouvons le constater, les deux variables d'environnement que nous avons configurer dans le fichier sont bien présente.

## Changer la variable HOSTNAME

Vous l'avez peu être vu, par défaut, Docker affect à la variable d'environnement *HOSTNAME* avec l'id du conteneur. Nous allons voir comment changer ça.

Nous pouvons de nouveau supprimer notre conteneur, car nous allons le recréer.

```bash
> docker rm -f testenv
```

Quand nous recréons notre conteneur, nous pouvons utiliser le paramètre **--hostname** qui prend en paramètre la valeur que va avoir la variable d'environnement *HOSTNAME*.

```bash
> docker run -tid --name testenv --hostname test.lab --env VAR=test --env-file env.lst ubuntu:latest
```

Si vous refaite la procédure de vérification, vous pourrez vous rendre compte que la variable *HOSTNAME* a bien prise la valeur que nous lui avons définit, que la variable VAR que nous avons passé avec **--env** et aussi présente et que les deux variable que nous avons définit dans un fichier sont aussi présente.

# Créer une image à partir d'un conteneur

Nous allons voir ici comment créer une image à partir d'un conteneur. Une image est un genre de template que vous pouvez utiliser pour créer autant de conteneur que vous le souhaitez. Tous les conteneurs que nous avons créer jusque là dérivé d'une image. Quand nous avons créer le conteneur web avec le serveur nginx, nous avons spécifié à la fin du **docker run** nginx:latest. Docker va d'abord chercher dans son registre d'image local si l'image nginx:latest est présente. Si elle ne l'est pas en local, il va la chercher sur la registry qui est configurer (ici DockerHub).

La méthode que nous allons utilisé ici, n'est pas la seul et n'est probablement pas la meilleur. Nous verrons plus tard une alternative. Cette alternative est plus difficile à mettre en place mais elle est beaucoup plus puissante. 

Pour afficher les images que vous avez en local, nous pouvons utiliser la commande **docker image ls**.

```bash
> docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              latest              4e5021d210f6        7 days ago          64.2MB
nginx               latest              6678c7c2e56c        3 weeks ago         127MB
```

Nous voyons ici, toutes les images que nous avons en local. Ici j'ai deux images, Ubuntu:latest et nginx:latest. Nous pouvons aussi voir l'id de l'image, depuis combien de temps elle a été créée et la taille qu'elle prend sur le disque.

Afin d'avoir un exemple concret, nous allons créer un conteneur à partir de l'image d'ubuntu. Puis nous le modifieront en rajoutant des logiciels, et nous en ferons une image. Ici, je vais utiliser le conteneur *testenv* que nous avons créer plus tôt.

La première chose à faire et de ce connecter au conteneur.

```bash
> docker exec -ti testenv bash
```

Maintenant que nous avons la main sur notre conteneur, nous allons installer git et vim.

````bash
> apt-get update && apt-get install -y git vim
````

Maintenant que nous avons personnalisé notre conteneur Ubuntu, nous allons voir comment créer une image à partir de celui ci. Pour ce faire nous allons utiliser la commande **docker commit -m <text> <id> <name>**. Cette commande marche un peu comme la commande commit de git. Nous pouvons lui ajouter un argument **-m <text>** afin de mettre un message sur le commit.

```bash
> docker commit -m "Création de la nouvelle image" d61 ubuntu_custom:v1.0
```

Ici, nous avons créé une nouvelle image qui s'appel *ubuntu_custom:v1.0* à partir du conteneur qui a l'id *d61* et nous avons mis un message sur le commit.

Afin de constater que sa a bien marché, nous pouvons lister les images locale avec **docker image ls**.

```bash
> docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
ubuntu_custom       v1.0                3a623f6e87fd        About a minute ago   240MB
ubuntu              latest              4e5021d210f6        7 days ago           64.2MB
nginx               latest              6678c7c2e56c        3 weeks ago          127MB
```

Nous pouvons maintenant créer un nouveau conteneur à partir de cette image.

```bash
> docker run -tid --name imgtest ubuntu_custom:v1.0
```

Maintenant que le nouveau conteneur est créer, nous pouvons nous y connecter et constater que git et vim sont bien présent.

```bash
> docker exec -ti ubuntu_custom:v1.0 bash
> git
...
> vim
...
```

Afin d'avoir plus d'informations sur la création de l'image, nous pouvons utiliser **docker history** avec en argument l'id de l'image.

```bash
> docker history 3a6
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
3a623f6e87fd        8 minutes ago       /bin/bash                                       176MB               Création de la n
ouvelle image
4e5021d210f6        7 days ago          /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
<missing>           7 days ago          /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B
<missing>           7 days ago          /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   745B
<missing>           7 days ago          /bin/sh -c [ -z "$(apt-get indextargets)" ]     987kB
<missing>           7 days ago          /bin/sh -c #(nop) ADD file:594fa35cf803361e6…   63.2MB
```

## Supprimer notre image

Il faut bien se l'avouer, notre image n'est pas très utile, nous allons donc la supprimer. Pour se faire, nous sommes obligé de d'abord supprimer le conteneur. Il est logique de ne pas pouvoir supprimer un image qui est encore utiliser par un conteneur, car sans l'image, le conteneur de peu pas fonctionner.

```bash
> docker rm -f imgtest
> docker image rm 3a6
```

Maintenant, si nous faisons un **docker image ls**, notre image a disparu.

```bash
> docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              latest              4e5021d210f6        7 days ago          64.2MB
nginx               latest              6678c7c2e56c        3 weeks ago         127MB
```

# Créer une image avec le DOCKERFILE

Nous venons de voir comment créer une image à partir d'un conteneur. Cette méthode pose pas mal de problème. Par exemple, si vous voulez rapidement recréer l'image en y ajoutant des éléments ou en n'en modifiant d'autres, il vous faudra surement repartir de l'image ubuntu:latest d'origine.

L'autre méthode pour créer une image est de créer un fichier qui contiendra toute les instructions pour recréer l'image. Cette méthode est très puissante, car pour modifié l'image, il suffit de modifier le fichier et de lancer un **docker build**. Cette méthode permet aussi de facilement transmettre une image à quelqu'un, car ce n'est qu'un fichier qui peu être déposer sur un dépot git ou sur un ftp par exemple.

Le fichier **DOCKERFILE** contient des séquences d'instruction, voici les possibilités.

| Instruction | Description                                       |
| ----------- | ------------------------------------------------- |
| FROM        | L'image à partir de la quel nous voulons démarrer |
| RUN         | Lancement de commande (apt, git, ...)             |
| ENV         | Variables d'environnement                         |
| EXPOSE      | L'exposition de ports                             |
| VOLUME      | définition de volumes                             |
| COPY        | Copie de fichiers entre l'host et le conteneur    |
| ENTRYPOINT  | Processus maitre                                  |
| MAINTAINER  | La personne qui maintient l'image                 |

## A quoi ressemble un DOCKERFILE ?

Afin de faire un exemple pratique, nous allons recréer l'image que nous avons créer plus haut avec la commande **docker commit** avec un **DOCKERFILE**.

La première chose à faire est de créer un fichier qui se nomme **Dockerfile**. Et d'y ajouter ce que nous avons besoin. Ici je vais vous montrer et vous détailliez une fichier **Dockerfile** qui fait exactement la même chose que le point d'en dessus.

```bash
FROM ubuntu:latest
MAINTAINER Luca
RUN apt-get update \
&& apt-get install -y vim git \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
```

- La ligne *FROM* définit que nous voulons partir de l'image *ubuntu:latest*
- La ligne *MAINTAINER* définit que je suis la personne qui gère l'image
- la ligne RUN commence par mettre à jour la listes des paquets, puis installe *vim* et *git* et pour finir, elle passe un apt-get clean et elle supprime les fichier temporaire afin de rendre l'image la plus propre et la plus petite possible.

Maintenant que nous avons notre **Dockerfile** qui définit la création de notre image, il nous reste à demander a docker de l'utiliser pour créer effectivement notre image. Pour ce faire, nous utilisons la commande **docker build -t <name_img> <path_Dockerfile>**.

```bash
> docker build -t testimg:v1.0 .
```

Ici, nous créons une image qui se nomme testimg:v1.0 à partir du fichier Dockerfile qui se trouve dans le même répertoire que moi.

Au moment ou vous tapez cette commande, vous allez vous rendre compte que votre terminal fait les étapes que vous avez demandez dans le Dockerfile. En fait, docker va effectivement installer vim et git, mettre à jour la liste des paquets et nettoyer les traces, comme nous l'avons définit dans le fichier.

```bash
> docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
testimg             v1.0                bc5a9a463e17        About a minute ago   212MB
ubuntu              latest              4e5021d210f6        8 days ago           64.2MB
nginx               latest              6678c7c2e56c        3 weeks ago          127MB
```

Nous pouvons constater que notre image est bien présente. Il ne nous reste plus qu'a créer le conteneur et voir si git et vim sont bien installé.

```bash
> docker run -tid --name test testimg:v1.0
> docker exec -ti test bash
> git 
...
> vim
...
```

Si tous c'est bien passé, les commandes git et vim doivent retourner un résulta.