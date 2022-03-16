# Installer Django

Pour pouvoir utiliser Django, il faut que Python soit installé. Dès que c'est fait, il suffit de faire `pip install django`. Afin de garder une machine propre, il est recommander d'utiliser un environnement virtuelle. Personnellement, pour cette formation, je vais utiliser pipenv.

# Gestion d'un projet

## Création d'un projet

Django est fournit avec un outil en ligne de commande qui est très pratique et qui met à disposition plusieurs fonctions, comme par exemple:
- Création d'un projet ou d'une application
- Création des tables dans la base de données en ce basant sur le modèle
- Lancement d'un serveur web de développement
- etc

Cette outils s'appel **django-admin**. Pour pouvoir l'utiliser l'utiliser, il faut ouvrir un terminal et l'appeler par son nom.
> Il faut bien passer par un terminal et pas par l'interpréteur Python.

Afin d'avoir plus d'information sur son fonctionnement, il suffit de taper `django-admin --help`. Voila ce que cette commande me retourne:
```bash
Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).
```

Pour mettre en pratique ce que je vais apprendre durant cette formation, je vais créer un blog. Cela me servira de fil rouge. Je me rend donc dans le dossier dans le quel je veux créer mon projet `~/dev/python/django/tuto`. Et j'utilise la commande suivant pour créer le créer `django-admin startproject blog`. Un nouveau dossier nommé *blog* a été créé avec la structure suivante:
```bash
blog
├── blog
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
``` 
Ce dossier est le dossier de notre projet. ä l'intérieur, nous trouvons deux choses, un fichier *manage.py* ainsi qu'un sous dossier *blog*. Dans le sous dossier *blog*, nous pouvons trouver 5 fichier.

- `__init.py__` : Il ne faut pas toucher à ce fichier. Il permet de dire à Python que nous travaillons sur un module.
- `asgi.py` : Il ne faut pas toucher à ce fichier. Il permet d'interfacer notre application django avec un serveur web compatible avec Asynchronous Server Gateway Interface. Il a été introduit avec Django 3.
- `settings.py` : C'est dans ce fichier que nous pouvoir configurer notre projet.
- `urls.py` : Ce fichier nous permet de configurer les URLS de notre application.
- `wsgi.py` : Il ne faut pas modifier ce fichier. Il permet d'interfacer notre application django avec un serveur web compatible avec Web Server Gateway Interface.

Le fichier *manage.py* qui se trouve à la racine de notre projet est une sorte de raccourci vers *django-admin*. La différence est qu'il prend en compte le contexte de notre projet. Maintenant que notre projet est créer, nous n'avons plus besoin d'utiliser *django-admin*.
> Il ne faut surtout pas modifier ce fichier !

Afin de nous assurer que notre projet a bien été créer nous allons lancer un serveur de développement.
```bash
python manage.py runserver
```
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

June 28, 2020 - 16:33:05
Django version 3.0.7, using settings 'blog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
>Vu que nous venons de démarrer le projet, nous avons un avertissement en rouge. Celui-ci n'empêche pas de lancer le serveur web. Nous verrons plus loins ce que signifie cet avertissement et comment le corriger.

Comme vous pouvez le voir, notre serveur à démarré. Nous pouvons y accéder via le localhost sur le port 8000. Si vous vous rendez à cette adresse avec un navigateur web, vous pourrez voir la page par défaut de django.

Nous avons vu comment lancer un serveur de dev avec *manage.py*, il faut savoir que cet outil est très puissant et qu'il permet de faire plein de chose afin de manager notre projet. Pour avoir plus d'information sur *manage.py*, vous pouvez utiliser la commande `python manage.py --help`. Nous utiliserons encore beaucoup *manage.py* au cours de ce tutoriel et nous verrons d'autre fonctionnalité de l'outil.

## Configuration du projet
Avant de commencer à créer des applications pour notre projet, nous allons le configurer. Pour ce faire, il faut ouvrir le fichier `settings.py`. Ce fichier est un simple fichier python qui contient des variables que nous pouvons modifié afin de modifier le comportement de notre projet.

```python
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```
La première variable qui est définie dans ce fichier est la variable `BASE_DIR`. Cette variable contient le chemin vers la racine de notre projet. Cette variable est très utile pour créer les chemins vers nos ressources.

Nous n'allons pas nous arrêter sur chaque variable, il y en a beaucoup. Nous allons passer en revue les variables les plus importantes. Pour avoir des informations sur les variables que nous n'allons pas voir, vous avez la documentation à votre disposition.

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
```
La variable `DEBUG`, permet d'indiquer si votre projet est en cours de développement. Quand vote projet est en mode debug, des informations sur les erreurs sont affiché lorsqu'elle survienne. Il ne faut absolument pas laisser ce mod activé lorsque vous passez votre projet en production car les erreurs peuvent contenir des informations sensible.

La configuration de la base de données se fait dans le dictionnaire `DATABASE`, par défaut, il est configurer pour utiliser une BDD SQLite. Il est conseillé de garder cette configuration pour le développement car l'avantage de SQLite est que toute la base est contenue dans un seul fichier. Ce système n'est pas le plus performant, mais il permet de rapidement commencer à développer sans ce prendre la tête avec un gestionnaire de base de données.

Voici un exemple pour un base de données MySQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Backends disponibles : 'postgresql', 'mysql', 'sqlite3' et 'oracle'.
        'NAME': 'crepes_bretonnes',             # Nom de la base de données
        'USER': '<nom d\'utilisateur>',
        'PASSWORD': '<mot de passe MySQL>',        
        'HOST': '127.0.0.1',                    # Utile si votre base de données est sur une autre machine
        'PORT': '3306',                         # ... et si elle utilise un autre port que celui par défaut
    }
}
```

Plus bas dans le fichier, il y a la variable `LANGUAGE_CODE`. Cette variable permet d'annoncer quel est la langue de notre projet. Ici, je vais changer `en-us` pour `fr-FR`.

Nous venons de voir les options les plus importantes. Comme je l'ai dis plus haut, il ne faut pas hésiter à aller voir la doc pour approfondir le sujet.

## Création d'application
Nous avons vu comment créer un projet et comment le configurer. La prochaine étape est de créer une application. En effet django s'organise en projet composer d'application. Une application est un ensemble de fonctionnalité qui rassemblée on un but, par exemple : un blog, un forum, une galerie photo, ...

Pour créer une application, nous allons utiliser `manage.py`. La commande ressemble beaucoup à la création d'un projet.
```bash
python manage.py startapp blog
```

Comme `startproject`, `startapp` créer un ensemble de fichiers et de dossier qui serviront de base à la création de notre application. Toute notre nouvelle application ce trouve dans le dossier `blog`. Ce dossier s'appel blog car c'est le nom que j'ai donner lors de l'exécution de `startapp`.

Voici la structure de notre projet maintenant maintenant que nous avons ajouter notre application blog:
```bash
.
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── blogtuto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```
Je vais maintenant décrire les fichiers qui ont été créer.
- `__init__.py` : Il ne faut pas modifier ce fichier, il permet de dire à Python que ce dossier est un module.
- `admin.py` : va permettre de définir ce que nous voulons afficher dans l'administration.
- `apps.py` : permet de configurer certain aspect de l'application.
- `models.py` : ce fichier contient tous les modèles de l'app.
- `tests.py` : C'est dans ce fichier que nous pouvons mettre les tests unitaires.
- `views.py` : Contient toutes les vues de notre application.

En plus de ces fichiers, il y a un dossier qui ce nomme `migrations`. Ce dossier permet de retracer l'histoire des modèles. Il contient toutes les requêtes SQL qui ont été passé à la base.

Maintenant que nous avons créer l'application, il faut configurer le projet pour qu'il là prenne en compte. Il faut déclarer l'application dans le fichier `settings.py` du projet.
Dans ce fichier, il faut chercher il faut chercher la liste `INSTALLED_APP` et y ajouter le nom de la nouvelle application.
```python
INSTALLED_APPS = [
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
Il faut laisser les entrées de la liste qui sont déjà présente !

Notre projet et notre application sont désormais configuré. Nous allons pouvoir commencer à développer notre application.

# Les bases de données
Il est très souvent utile d'utiliser une base de données en parallèle d'une application Django afin de stocker des données. Pour cela, Django utilise un **ORM** *object-relationnal mapping*. L'ORM permet de ne pas avoir besoin d'utiliser le langage SQL pour interagir avec la base de données. En effet, lorsque nous créons un modèle, Django va automatiquement créer une table qui lui est associé. Cette table va permet de stocké toutes les informations relative au modèle.

Voici l'exemple d'un modèle:
```python
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=40)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
```
A partir de ce modèle, Django va créer une table `blog_article` (*blog* est le nom de l'application et *article* et le nom du modèle). Dans cette table, il va créer plusieurs champs: `titre`, `auteur`, `contenu` et `date`. Chaque champ à son propre type en fonction de ce que nous avons définit dans le modèle ainsi que ces propres paramètre.

Nous venons de créer une table avec plusieurs champs sans jamais taper de SQL ! Ne pas avoir besoin d'utiliser le SQL n'est pas le seul avantage d'un ORM. En effet, il permet de migrer de système de gestion de base de données sans avoir besoin de ré-écrire les requêtes ! Nous allons donc pouvoir développer notre application en local en utilisant SQLite et par la suite, passer sur un système de gestion des bases de données plus robuste lors de la mise en production.

## Les clés étrangères
Django va dans tous les cas, pour chaque table, créer un champ `ID`. Ce champ permet de rendre unique chaque entrée das la base de données. En effet, le champ est configurer pour incrémenter automatiquement de 1 à chaque nouvelle entrée. Ceci permet d'aller chercher une enregistrement précis dans une table.

Cela permet aussi de lier plusieurs table. Django connait trois relations, *plusieurs-à-plusieurs*, *plusieurs-à-une* et *un-à-un*. 

# Les vues
Nous allons dans ce chapitre, voir comment créer des vues et donc afficher pour la première fois du texte sur un page web ! Lorsque nous créons une vue, nous devons lui associé un url afin de pouvoir la joindre.

## Hello World !
Nous allons, pour commencer, créer un petit *Hello World !*. Comme je l'ai dis plus haut, quand nous créons une vue avec Django, nous devons au moins lui attribuer un URL. La vue en elle même est une fonction dans le fichier `views.py` de l'application. Cette fonction va recevoir les données du modèle et appeler un template pour générer le rendu HTML.

Nous n'allons pas commencer par quelque chose de compliquer, nous allons afficher sur une page "Bienvenu sur mon blog!".

### La gestion des vues
Dans le dossier `blog`, nous allons travailler sur le fichier `views.py`. Ce fichier a été généré lors de la création de l'application par Django. Pour le moment, il est presque vide.
```python
from django.shortcuts import render

# Create your views here.
```
Nous n'avons pas encore vu comment créer des modèles et des templates, mais nous pouvons quand même créer une vue simple. Nous allons écrire du code HTML directement dans la vue et le renvoyer au client. Pour le moment, nous n'allons pas utiliser la méthode `render` qui est importée par défaut et utiliser `HttpResponse` qui permet de renvoyer une réponse HTTP.
```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Bienvenu sur mon blog!</h1>
    """)
```
Ce code se découpe en 3 partie:
- Nous importons la classe `HttpResponse` du module `django.http`. Cette classe permet de renvoyer une réponse (soit du texte brute, soit du HTML) depuis une chaine de caractère. `HttpResponse` est spécifique à Django et permet d'encapsuler la réponse dans un objet générique qui peu être traiter par Django.
- Une fonction `home`, avec comment argument une instance de `HttpRequest`. Nous avons nommé cette argument `request`. Cette argument contient des informations sur la méthode de la requête (GET, POST), les données des formulaire, la session du client, etc.
- Pour finir, la fonction renvoie une instance de `HttpResponse` à partir d'une chaine de caractère.

Il faut absolument que toutes les fonctions prennent comme premier argument un objet de type `HttpReqest`. Il faut aussi que toutes les fonctions vue renvoie une instance de `HttpResponse`. Si ce n'est pas le cas, Django va lever une erreur.

Par la suite, nous ne renverrons jamais du code HTML directement depuis la vue. C'est le rôle des templates de le faire. Nous le faisons ici afin de pouvoir introduire le sujet des vues simplement.

## Routage d'URL
Maintenant que nous avons une vue opérationnel, nous devons lui créer un URL afin de pouvoir y accéder. Pour se faire, nous devons aller modifier le fichier `urls.py` du projet. Par défaut, ce fichier ne contient qu'un seul url. C'est l'url de l'administration.
```python
"""blogtuto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```
Quand un utilisateur appel une page, la requête est prises en compte par le contrôleur de Django qui va chercher à quel vue correspond cet URL. En fonction de l'ordre de définition dans le fichier `urls.py`, la première vue qui correspond à l'URL sera appelé et elle retourne la réponse HTML au contrôleur qui lui se charge de la retourner à l'utilisateur. Si aucun URL ne correspond, une page d'erreur 404 est retournée.

Nous allons nous occuper de la liste `urlpatterns` qui permet de définir des association entre des URLs et de vues. Une association de routage basique se définit par un sous-tuple composé des éléments suivant:
- Le schéma de l'URL: une URL peut être composée d'arguments qui permettent par la suite de retrouver des informations dans les modèles.
- Le chemin python vers la vue correspondante.

Si nous reprenons le fichier `urls.py` et que nous voulons rendre accessible la vue que nous venons de créer via la racine du site, il faut ajouter la règle suivante dans `urlpatterns`.
```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
```
Comme pour la ligne de l'administration, le premier argument représente le fragment d'URL et le seconde est la vue que nous avons créer dans le fichier `blog/views.py`. Nous avons importer le modèle `views` afin de pouvoir joindre notre vue.

Maintenant, si vous enregistrez ces modifications et que vous lancer le serveur de développement (`python manage.py runserver`), et en vous rendant à l'adresse `http://127.0.0.1:8000`, vous devriez voir la vue que nous avons créer apparaitre !

Si c'est le cas, félicitation ! Sinon, reprenez ce chapitre et vérifié que tout est correcte, une petite erreur dans le code va faire que rien ne marche !

## Organiser proprement les URL
La méthode que nous venons de mettre en place pour la gestion de nos URLs pose un gros problème de réutilisation de notre application. En effet, nous mettons tous les URLs de nos applications dans le fichier `urls.py` de notre projet. Dans le cas ou nous voulons reprendre notre application pour un autre projet, il faudra entré tous les URLs de notre application dans le fichier de l'autre projet. Une application peu vraiment avoir beaucoup d'URLs, ce qui rend ce travail fastidieux.

Pour remédier à ce problème, nous pouvons créer un fichier `urls.py` dans notre application et l'inclure dans le fichier `url.py` de notre projet.

### Comment mettre ce système en place ?
Tout d'abord, il faut créer un fichier `urls.py` à la racine de notre application. Il ne faut pas oublier d'importer les modules dont nous avons besoin.
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home)
]
```
Il faut donc inclure la classe path qui nous permet de créer nos chemin et les vues de l'application. En suite, nous créons un dictionnaire `urlpatterns` et nous le remplissons avec nos associations URLs -> vue.

Maintenant que nous avons créer le fichier et que nous y avons mis nos URLs, il nous faut nous rendre à nouveau dans le fichier `urls.py` de notre projet et le modifier pour y inclure notre nouveau fichier.
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogs.urls')),
]
```
Nous n'avons plus besoin d'importer directement notre vue. Par contre, nous devons importer la classe include du module `django.urls`. C'est cette classe qui va ce charger d'inclure le fichier `blog/urls.py`.

### Passer des arguments à nos vues
Nous sommes maintenant comment lier des URLs à nos vues et comment les organiser. Nous n'avons pas encore vu comment nous pouvons passer des paramètres dans nos URLs. Ce que nous voulons faire, c'est que lors nous appelons l'URL `127.0.0.1:8000/1` cela nous sert une vu qui donne le détail de l'article qui porte l'id numéro 1.

Pour pouvoir passer des paramètres dans les URLs, il faut les capturés directement depuis la définition des association URLs -> vue. J'ajoute donc une route au fichier `urls.py` de l'application.
```python
urlpatterns = [
    path('', views.home),
    path('<id_article>', views.detail),
]
```
Maintenant, quand l'utilisateur appel la page `127.0.0.1:8000/42`, le contrôleur appel la fonction `detail` et passe le paramètre `42`. Nous pouvons donc créer une vue très basique qui va recevoir le paramètre:
```python
def detail(request, id_article):
    return HttpResponse(
        "Vous avez demander l'article {}".format(id_article)
    )
```
Maintenant, si vous appelez l'URL racine avec un paramètre, vous pourrez vous rendre compte qu'il est bien passer à notre vue.

Ici, nous ne faisons aucune validation sur le paramètre que nous capturons. Il est possible de capturer plusieurs paramètre dans le même URL et de forcer son type. Voici un exemple que je ne vais pas utiliser pour le blog, il permet par contre d'illustrer le propos.
```python
urlpatterns = [
    path('', views.home),
    path('<id_article>', views.detail), 
    path('<str:tag>', views.list_articles_by_tag), 
    path('<int:year>/<int:month>', views.list_articles),  
]
```
En tout, il existe 5 type de données identifiable par ce système de routage:
- `str` : C'est le format par défaut. Il permet de récupérer une chaine de caractère non vide excepter le `/`.
- `int` : une suite de chiffre, un entier sera donc retourné à notre vue.
- `slug` : c'est une chaine de caractère sans accentuation ou caractère spéciaux.
- `uuid` : format standardisé de donnée souvent utiliser pour un identifiant unique.
- `path` : comme `str`, mais permet en plus de capturer les `/`. Cela permet de récupérer n'importe quel URL, quelque soit le nombre de segment.

Maintenant que nous avons vu que nous pouvons spécifié un type de données à capturer, je vais modifié le fichier `urls.py`. Je veux que le paramètre passé soit un `int`.
```python
urlpatterns = [
    path('', views.home),
    path('<int:id_article>', views.detail),
]
```

#### Utiliser les expressions régulière dans les URL
La méthode de capture des paramètres que nous venons de voir a été introduite dans Django 2.0. La version 1.0 de Django utilisait une autre manière de la faire, elle permettait de définir les URL avec des expressions régulière. Voici un exemple:
```python
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'', views.home),
    re_path(r'(?P<id_article>.+)', views.view_article), 
    re_path(r'(?P<tag>.+)', views.list_articles_by_tag), 
    re_path(r'(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles),  
]
```
Nous pouvons voir que c'est beaucoup plus verbeux. Nous pouvons aussi remarquer qu'il est possible de faire des tests en amont de la vue. Si nous prenons la dernière ligne nous pouvons remarquer une subtilité. Si nous découpons la chaine nous arrivons à ça:
- `(?P<year>\d{4})` : un nombre à quatre chiffres qui sera affecté à la variable year.
- `(?P<month>\d{2})` : un nombre à deux chiffres qui sera affecté à la variable month.

Il y a aussi des avantages à utiliser le nouveau système. Contrairement aux expressions régulière, le nouveau système affecte directement le bon type à la variable qui est créer. Il n'y a donc pas besoin de faire de cast.

#### Un dernière mot sur les paramètres
Quand nous avons créé nos paramètres, nous avons pris soin de leur donner un nom. Cela permet de dire à Django comment la valeur de nos paramètres seront accessible dans la vue. De ce fait, l'ordre de déclaration des paramètres dans la vue n'importe peu. Le seul paramètre qui a une place spécifique est `request` qui doit toujours être le premier paramètre. La seul chose important est de s'assurer que nous utilisons les mêmes nom dans `urls.py` et dans nos vues.

Nous pouvons aussi spécifié une valeur par défaut pour un paramètre. Cela veux dire que si l'utilisateur ne spécifie pas de valeur pour un paramètre donné, il prendra la valeur que nous lui avons définit. Pour définir une valeur par défaut, cela ce passe comme pour python est les fonctions. Au moment ou nous écrivons notre fonction avec ces paramètres dans `views.py`, il suffit de mettre `=<val>` à côté du paramètre comme nous voulons définir comme optionnel.

Il est aussi toujours possible de passer des paramètres `GET`. Pour récupère ces valeurs, il faut utiliser le dictionnaire `request.GET` qui est disponible dans la vue.

### Réponses spéciales
Nous avons vu jusqu'ici comment retourner du HTML à l'utilisateur. Il y a des situations ou nous voulons renvoyer une erreur 404 ou une redirection. Nous allons voir comment nous pouvons faire.

#### Afficher une erreur 404
Il est possible que l'utilisateur demande une page qui colle à un paterne d'URL valide mais que la page ne peu quand même pas être affichée. Par exemple, si l'utilisateur demande le détail d'un article qui n'existe pas, le routage ne pourra pas ce rendre compte que que la page n'est pas valide car l'URL est formaté correctement. Il faudra donc faire une contrôle dans la vue et si l'id n'existe pas, afficher une erreur 404. Pour ce faire, il faut utiliser une exception du framework qui s'appel `Http404` et qui fait partie du module `django.http`.

```python
from django.http import HttpResponse, Http404

def detail(request, id_article):
    if id_article > 100:
        raise Http404

    return HttpResponse('<h1>Article {}</h1>'.format(id_article))
```
Cette exemple, renvoie une erreur 404 lorsque l'id de l'article est plus grand que 100. Ce n'est pas un bon moyen de faire, mais cela permet de tester l'erreur 404. Si l'id est plus petit que 100, la page sera affichée normalement.
> Si vous êtes en mod DEBUG, la page 404 ne sera pas une page 404 classique. Django va afficher l'erreur.

#### Rediriger l'utilisateur
Il peut arriver que vous vouliez rediriger l'utilisateur vers une autre page lorsque une action est faite. Par exemple, lorsque un utilisateur ce connecte, on peut vouloir le rediriger vers la page accueille où ça page d'origine.

Pour ce faire, Django met à disposition la méthode `redirect` qui renvoie un objet `HttpResponseRedirect` (classe qui hérite de `HttpResponse`), qui renvoie vers un autre URL. La méthode `redirect` peut prendre en paramètre plusieurs types d'arguments, comme par exemple un URL ou le nom d'une vue.

Par exemple, si nous voulons rediriger un utilisateur vers la page accueille de Django nous pouvons faire quelque chose comme ça:
```python
from django.shortcuts import redirect

def list(request):
    return redirect("https://www.djangoproject.com")
```

Nous pouvons aussi vouloir rediriger l'utilisateur vers une page de notre site. Dans ce cas, il vaut mieux utiliser l'autre méthode qui permet de garder indépendante la configuration des URLs et des vues. Nous devons donc passer comme argument le nom de la vue vers laquelle nous voulons rediriger utilisateur et éventuellement des paramètres qui lui sont destiné. 
```python
from django.shortcuts import redirect

def list(request):
    return redirect(redirection)

def redirection(request):
    return HttpResponse("Vous avez été redirigé !")
```
Pour cette exemple, j'ai créé une nouvelle vue qui s'appel `redirection`. Chaque foi que la vue `list` est appelée, nous sommes redirigé vers la vue `redirection` qui elle affiche un message.

Il ne faut pas oublier que chaque vue doit avoir au moins une URL qui lui est associée, il faut donc ajouter un chemin au fichier `urls.py`.
```python
urlpatterns = [
    path('', views.list),
    path('<int:id_article>', views.detail),
    path('redirection', views.redirection),
]
```
Si nous n'ajoutons pas de chemin de routage, Django affichera une erreur.

Il est aussi possible de définir si une redirection est temporaire ou définitive. Pour cela, il faut ajouter le paramètre `permanent=True`. Cela ne change rien pour l'utilisateur, ça permet d'aider les moteurs de recherche.

Si nous voulons rediriger l'utilisateur vers notre vue `detail`, nous devons passer en paramètre l'id de l'article.
```python
return redirect(view_detail, id_article=22)
```
 Pour en finir avec les redirection, il est possible de faire pointer la redirection vers le nom d'une d'une vue qui est définie dans le fichier `urls.py`. Ici, elle va donc générer l'url `/22` et rediriger l'utilisateur vers celui-ci. Cela permet de changer les URLs dans le fichier `urls.py` sans casser toutes les redirections. Cette fonctionnalité est extrêmement pratique, il ne faut donc jamais écrire des URLs en dure dans vos vue, sauf quand cette méthode est inutilisable.

 Au lieu d'écrire à chaque fois touts le chemin d'une vue ou de l'importer, il est possible de lui assigner un nom plus cours dans le fichier `urls.py`.
 ```python
 urlpatterns = [
    path('', views.view_list, name='list'),
    path('<int:id_article>', views.view_detail, name='detail'),
]
 ```
 Nous pouvons maintenant utiliser son nom pour faire la redirection.
 ```python
 return redirect('detail', id_article=22)
 ```

 Pour terminer, il faut savoir que que Django met à disposition la méthode `reverse()` (`django.urls.reverse`). Elle retourne une chaine de caractère qui contient l'URL du nom que nous avons passer en paramètre. Pour que cela marche, il faut qu'un nom soit définit dans `urls.py` pour le chemin.

 # Les templates
 Jusque ici nous avons vu comment créer des vues qui renvoie du HTML à l'utilisateur. Cela n'est pas une bonne pratique. En faisant ce que nous avons fait, notre code devient beaucoup plus difficile à éditer car le code HTML et python ce confonde. 

 C'est pour cela que le framework intègre un moteur de template. Le moteur de template permet d'écrire du code HTML séparer du code python. En plus de ça, il met à disposition un mini language de programmation qui permet d'ajouter des structures de contrôle basique (`if/else`, `for`, etc.) sous forme de balises. Quand le moteur tombe sur une balise, il la transforme automatiquement en code HTML.

 ## Lier des templates à des vues
 Dans la manière de fonctionner de Django, la vue va chercher les informations du modèle puis les transmet au template qui lui ce charge de générer le code HTML qui sera renvoyé au visiteur.

 Dans le chapitre précédent, nous avons utilisé la méthode `HttpResponse()` pour renvoyer du HTML au navigateur. Cette méthode prend en entrée une chaine de caractère et la renvoie sous forme d'une réponse HTTP. Ici, nous allons utiliser la méthode `render()` qui va ce charger d'appeler le template et le renvoyer sous forme de réponse HTTP.
 > La méthode `render` est fait partie de `django.shortcut`. Elle génère un objet `HttpResponse` après avoir traité le template.

 Voici un exemple:
 ```python
from datetime import datetime
from django.shortcuts import render

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())
 ``` 
 ```python
from django.urls import path
from . import views

urlpatterns = [
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]
 ```

 Comme nous pouvons le voir la fonction `render` prend trois paramètres:
1. La requête HTTP initiale, que nous appelons `request` par convention.
2. Le chemin vers le bon template dans un dossier données dans `settings.py`.
3. Un dictionnaire reprenant les variables qui seront disponible dans notre template.

Maintenant que nous avons nos vues prête, nous devons nous demander où nous allons stocker nos template.
1. Dans la liste des dossier du paramètre `DIR` de la variable `TEMPLATE`.
2. S'il ne l'a pas trouver, dans un dossier `templates` de l'application.

Lorsque nous avons configuré notre projet parlé de `TEMPLATE`. Elle a en quelque sorte la même structure que `DATABASE`. On peu choisir moteur de template spécifique et le configurer. Nous allons utiliser le moteur par défaut de Django, mais nous allons ajouter un dossier à la configuration.
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Cette ligne ajoute le dossier templates à la racin du projet
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
Maintenant que nous avons passé cette configuration, il faut ajouter un dossier `templates` à la racine du projet. Ce dossier va permettre de mettre les templates qui seront commun à toutes les applications de notre projet (erreur 404, squelette du design, page static, etc...). Django va aller chercher en premier lieu dans ce répertoire.

Pour ce qui est des applications, nous allons utiliser un dossier `templates` propre à cette dernière. Il est préférable de conserver les templates qui sont propre à l'application dans son propre dossier. Cela permet de facilement réutiliser une application.

Pour éviter les conflits, il est d'usage de créer un dossier au nom de l'application dans le dossier `templates`. La structure ressemble donc à ceci:
```bash
.
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── blog
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blogtuto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── templates
```

Maintenant que nous avons notre structure, nous allons pouvoir créer notre premier template. Nous devons créer le fichier `blog/templates/blog/date.html`. Dans ce dossier, j'ajoute:
```html
<h1>Bienvenu sur mon blog</h1>
<p>La date est : {{ date }}</p>
```

Nous retrouvons bien `date` que nous avons passer à la méthode `render`. C'est la seul variable qui est accessible via le template car c'est la seul variable que nous avons passé.

Il est possible de passer toutes les variables de la vue avec `locals()`. Voici un exemple:
```python
def view_test(request):
    name = "Luca"
    last_name = "Ray"
    address = "Sous la loge 5"
    return render(request, 'blog/test.html', locals())
```
```html
<h1>Prénom</h1>
<p>{{ name }}</p>
<br>
<h1>Nom de famille</h1>
<p>{{ last_name }}</p>
<br>
<h1>Adresse</h1>
<p>{{ address }}</p>
```
Toutes les variables locales que nous avons créer dans la vue sont passées au template et sont accessible grâce à leur nom.
Dans ce cas de figure, nous avons aussi à la valeur de `request` car c'est également une variable locale de notre vue.

## Afficher une variable
Comme nous venons de le voir, pour afficher une variable dans un template, nous devons utiliser l'expression `{{  }}`. Si la variable n'est pas un string, la fonction `__str__` sera utiliser. Par exemple, si nous affichons une liste, nous aurons le résultat `['el1', 'el2', 'el3']`. Si la variable à afficher est un objet, il est possible d'accéder à ces attributs avec le `"."`.

### Les filtres
Les filtres permette d'influencer l'affichage d'une variable directement dans le template sans passer par la vue. Par exemple, il y a le filtre `truncatewords`. Il permet d'afficher qu'un certain nombre de mot d'une variable à l'utilisateur. Voici comment l'utiliser:
```django
{{ text|truncatwords:10 }}
```
Imaginer que la variable `text` contient un texte assez long. Dans le cas présent, que les 10 premier mot seront affiché.

Comme vous pouvez le voir, pour appliquer un filtre sur une variable, il faut d'abord appeler la variable et la faire suivre d'un `|` et le nom du filtre. Si le filtre prend un paramètre, il faut faire suivre le tout de `:` puis le paramètre voulus.

Il existe plein d'autre filtres, pour mettre les mots au plurielle si besoin, pour afficher une valeur par défaut si la variable n'existe pas, ... Nous pouvons trouver tous les filtres [ici](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#built-in-filter-reference).

## Manipuler des données
Nous allons, ici, voir les tags. Il permet de faire des manipulation sur les données, comme par exemple, des boucles et des conditions.

### Les conditions
Tout comme en python, nous pouvons faire des conditions directement dans nos vues. Pour ce faire, nous devons utiliser les tags `{% if <condition> %}`, `{% elif <condition> %}`, `{% else %}`, `{% endif %}`.
```django
Bonjour
{% if sexe == "Femme" %}
    Madame
{% else %}
    Monsieur
{% endif %} !
``` 
Ici, en fonction de la variable `sexe`, il sera afficher Monsieur ou Madame.

Nous pouvons aussi utiliser `{% elif %}` afin de chainer les conditions dans la même structure conditionnel.
```django
{% if age > 25 %}
    Bienvenu Monsieur !
{% elif age > 16 %}
    Va-y, tu peu passer..
{% else %}
    Tu ne peu pas rentrer petit !
{% endif %}
```

### Les boucles
Le moteur de template de Django permet de faire un boucle qui est similaire à la boucle `for` de python. Nous pouvons donc l'utiliser pour parcourir des éléments. Par exemple, si nous avons une liste qui contient des couleurs.
```python
couleurs = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
```
Nous pouvons le parcourir grâce au tag `{% for %}`, `{% endfor %}`:
```django
Les couleur de l'arc-en-ciel sont:
<ul>
{% for couleur in couleurs %}
    <li>{{ couleur }}</li>
{% endfor %}
</ul>
```
Cela donnera le code HTML suivant:
```html
Les couleurs de l'arc-en-ciel sont :
<ul>
    <li>rouge</li>
    <li>orange</li>
    <li>jaune</li>
    <li>vert</li>
    <li>bleu</li>
    <li>indigo</li>
    <li>violet</li>
</ul>
```

Il est aussi possible de parcourir un dictionnaire et de décomposer chaque itération en clé/valeur:
```python
couleurs = {
    'FF0000':'rouge', 
    'ED7F10':'orange', 
    'FFFF00':'jaune', 
    '00FF00':'vert', 
    '0000FF':'bleu', 
    '4B0082':'indigo', 
    '660099':'violet',
}
```
```django
Les couleurs de l'arc-en-ciel sont:

<ul>
{% for code, nom in couleurs.items %}
    <li style="color: #{{code}}">{{nom}}</li>>
{% endfor %}
</ul>
```
Ce qui génère le code HTML suivant:
```html
<ul>
    <li style="color:#ED7F10">orange</li>
    <li style="color:#4B0082">indigo</li>
    <li style="color:#0000FF">bleu</li>
    <li style="color:#FFFF00">jaune</li>
    <li style="color:#660099">violet</li>
    <li style="color:#FF0000">rouge</li>
    <li style="color:#00FF00">vert</li>
</ul>
```
> Il est important de répéter que le traitement dans sur les données doivent être fait au maximum dans la vue. Le template n'est la que pour afficher des données.

Il existe un autre tag qui peu être utiliser avec le tag `{% for %}`, c'est `{% empty %}`. Il permet d'afficher quelque chose si l'itérable que nous voulons parcourir est vide:
```django
{% for commentaire in commentaires %}
    <p>{{ commentaire }}</p>
{% empty %}
    <p class="empty">Pas de commentaire pour le moment </p>
{% endfor %}
```

### Les blocs
Dans la majorité des cas, un site web a toujours la même structure: un titre en haut de page, un menu, un footer, ... Si vous devez copier ce code dans chaque template et que vous voulez changer un élément, il faudra faire la modification partout. Cela peu s'avérer très vite rébarbatif. Pour palier à ce problème, le moteur de template de Django met à disposition la balise `{% block %}`.

Ce tag permet de déclarer des blocks dans un template qui peuvent être réutiliser dans d'autres templates. De ce fait, nous pouvons créer un template général que nous nommerons `base.html` qui va définir la structure globale de nos pages. Par exemple:
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>{% block title %}Exemple{% endblock %}</title>
</head>
<body>
    <nav>
        {% block nav %}
        <ul>
            <li><a href="#">Menu 1</a></li>
            <li><a href="#">Menu 2</a></li>
            <li><a href="#">Menu 3</a></li>
        </ul>
        {% endblock %}
    </nav>
    <section id="content">
        {% block content %}{% endblock %}
    </section>
    <footer>&copy; Exemple</footer>
</body>
</html>
```
Ce template est composé de plusieurs blocs:
- `{% block title %}`
- `{% block nav %}`
- `{% block content %}`
> Tous ces blocs pourront être redéfini ou inclus tels quels dans un autre template

J'enregistre ce template dans le dossier `templates` du projet et non de l'application. Je fais ce choix car ce template va s'appliquer pour tous le projet et pas que pour une seul application. Maintenant que nous avons notre template général, nous allons pouvoir créer des templates spécifique pour chaque une de nos vue dans le dossier `templates` de notre application.

Pour pouvoir utiliser notre template `base.htmt`, nous allons utiliser le tag `{% extend %}`. Cela nous permet d'inclure un template et de si besoin le surcharger.

Voici le template `test.html` que nous avons créer plus tôt:
```html
{% extends 'base.html' %}    
{% block title %}Page de test{% endblock %}
{% block content %}
    <h1>Prénom</h1>
    <p>{{ name }}</p>
    <br>
    <h1>Nom de famille</h1>
    <p>{{ last_name }}</p>
    <br>
    <h1>Adresse</h1>
    <p>{{ address }}</p>
    <br>
    {{text|truncatewords:10}}
{% endblock %}
```
Dans cette exemple, nous surchargeons deux blocs `title` et `content`. Le tag `extends` va chercher le template `base.html` 

### Les URL
Comme pour les vues, il existe un équivalent de la méthode `reverse()` pour les templates. Pour l'utiliser, il faut utiliser le tag `{% url %}`. Ce tag permet de créer des URL en passent en paramètre le nom d'une vue. En plus du nom de la vue, il est possible de passer des arguments qui servent de paramètre à la vue.
```html
<a href="{% url 'detail' 42 %}">Article 42</a>
```
Génère le code suivant:
```html
<a href="/42">Article 42</a>
```
Comme vous pouvez, nous passons en paramètre le nom de la vue, il est donc important de donner un nom à nos vues dans le fichier `urls.py`. Dans cet exemple, je passe l'argument 42 à la main, il est bien sur possible de passer une variable comme argument.

### Les commentaires
Il est possible de mettre des commentaires directement dans un template. La différence entre les commentaire HTML et les commentaire du moteur de template de Django et que les commentaires de Django n'apparaisse pas dans le code source de la page. 

Il peuvent être pratique pour organiser votre code ou encore pour faire des tests en enlevant temporairement des lignes.

Comme pour les commentaire HTML, il existe deux type de commentaires Django. Un commentaire pour une seul ligne et un commentaire pour plusieurs lignes.
```html
{# Voici un commentaire sur une seul ligne Django, il n'apparaitra pas dans le code source de la page. #}
{% comment %}
Voici un commentaire multi ligne Django
Lui non plus n'apparet pas dans le code source de la page.
Par contre, il permet de commenter plusieurs lignes.
{% endcomment %}
```

## Les fichiers statique
Jusque là, nous n'avons utiliser que des fichiers HTML. Une application web moderne utilise beaucoup d'autre chose, comme par exemple, du CSS, du JS, des images, ... Nous allons voir ici, comment les ajouter à nos templates.

Comme pour les templates, nous pouvons mettre nos fichiers statiques à plusieurs endroit. Afin d'organiser au mieux notre projet, nous allons faire un dossier `static` propre à l'application ainsi qu'un dossier `static` pour le projet.

Je commence par créer le dossier `static` à la racine du projet. C'est ici que nous allons mettre les fichiers qui appartiennent globalement au projet.

Nous devons, comme pour les dossiers `templates`, adapter la configuration dans le fichier `settings.py`.
```python
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
```
La première variable indique l'URL du dossier depuis lequel vos ficher serons accessible. Le deuxième indique le chemin vers ces fichiers sur le disque dur à partir de la racine du projet.

Je vais aussi créer un dossier `static` à la racine du projet afin d'accueillir les fichiers propres à l'application. Afin de respecter la convention et pour ne pas faire de conflit, je créer un dossier `blog` dans le dossier `static`.

Voici la structure de mon projet:
```bash
.
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── static
│   │   └── blog
│   │       └── linux.png
│   ├── templates
│   │   └── blog
│   │       ├── date.html
│   │       ├── list.html
│   │       └── test.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blogtuto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── static
│   ├── css
│   ├── img
│   │   └── python.png
│   └── js
└── templates
    └── base.html
```
Comme vous pouvez le voir, j'ai ajouter une image dans le dossier `static` du projet et une dans le dossier `static` de l'application.

Voici comment je peux intégrer ces images à nos vues:
```html
{% load static %}
<img src="{% static 'blog/linux.png' %}" /><br>
<img src="{% static 'img/python.png' %}" />
```

La première chose que je fait, c'est appeler `{% load static %}`. Cela permet de charger la librairie de gestion des fichiers static. Une foi que c'est fait, je peu appeler l'URL de mes images avec `{% static <chemin> %}`.

Il ne faut jamais coder le chemin en dur, imaginer que vous voulez changer l'endroit ou sont stocké les fichiers ou si vous voulez changer l'URL d'accès à ces derniers et que les chemins sont codé en dur, il faudra changer l'url de chaque ressource. Si vous utiliser `{% static %}`, il suffit de changer la configuration dans `settings.py`.

Lorsque un site Django est en production, il ne faut pas utiliser cette méthode. C'est la travail du serveur web de servir les fichiers. Par contre, lors du développement cela va s'avérer très pratique. Nous verrons plus loins comment configurer un projet pour la production.

# Les modèles
Nous avons vu comment créer des vues et des templates. Sans les modèles, ces deux composantes sont presque inutile. Autant utiliser un site statique ! 