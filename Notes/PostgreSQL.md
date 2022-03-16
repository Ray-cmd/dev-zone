PostgreSQL

- [1. Introduction](#1-introduction)
- [2. Installation](#2-installation)
- [3. Utilisation des rôles et des bases de données](#3-utilisation-des-rôles-et-des-bases-de-données)
  - [3.1. Basculer sur le compte postgres](#31-basculer-sur-le-compte-postgres)
  - [3.2. Accéder à un prompte Postgres sans changer de compte](#32-accéder-à-un-prompte-postgres-sans-changer-de-compte)
- [4. Création d'un nouveau rôle](#4-création-dun-nouveau-rôle)
- [5. Création d'une nouvelle base de données](#5-création-dune-nouvelle-base-de-données)
- [6. Ouverture d'une invite Postgres avec le nouveau rôle](#6-ouverture-dune-invite-postgres-avec-le-nouveau-rôle)
- [7. Création et suppression de tables](#7-création-et-suppression-de-tables)
- [8. Ajout, requête et suppression de données dans une table](#8-ajout-requête-et-suppression-de-données-dans-une-table)
- [9. Ajout et suppression de colonnes dans une table](#9-ajout-et-suppression-de-colonnes-dans-une-table)
- [10. Mise à jour des données dans une table](#10-mise-à-jour-des-données-dans-une-table)
- [11. Liens](#11-liens)

# 1. Introduction
Dans de nombreux cas, une application à besoin de stocké des données. Le stockage et l'affichage doit être rapide et doit pouvoir gérer beaucoup de connexions simultanées afin de ne pas la ralentir. Beaucoup de service web ont d'énorme volume de données complexe à stocké et c'est pour cela que le modèle de base de données relationnel c'est imposé. 

Dans ce papier, nous allons découvrir **PostgreSQL** aussi appelé **Postgres**. **Postgres** est un système de gestion de base de données relationnel qui implémente le langage **SQL**. Il est, avec le temps devenu très populaire autant pour les petits projet que les plus gros et cela grâce à ces fonctionnalités avancées telles que les transactions fiables et la simultanéité sans verrouillage en lecture. Il est aussi largement open source et est gratuit.

Nous allons, dans ce papier, voir comment nous pouvons l'installer et l'utiliser. Ce n'est pas un tutoriel sur le langage **SQL**, mais nous allons voir quelque exemple. J'utilise ici, une machine virtuel (WSL) Ubuntu.
> Il est bien sur possible de l'installer sur Windows et MacOS. Je fait ce tuto sur Ubuntu car Postgres est souvent installé pour du web sur des machine Linux.

# 2. Installation
Les dépôts présent par défaut avec Ubuntu mette à disposition le binaire de Postgres. Il me suffit donc d'utiliser `apt` afin de l'installer. Si il n'est pas présent de base dans votre distribution, il faut chercher sur le net pour trouver un dépôt dans le quel il est présent. Cela ne devrait pas être trop difficile vu qu'il est populaire et donc que beaucoup de gens auront voulus l'ajouter à leur distribution.

Nous allons installer deux paquets, `postgresql` et `postgresql-contrib`. Ce dernière paquet est un binaire qui ajoute quelque outils et fonctionnalités en plus.

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib -y
```
Maintenant que Postgres est installé, nous allons pouvoir voir comment il fonctionne et en quoi il diffère de ces concurrents. 

# 3. Utilisation des rôles et des bases de données
Par défaut, Postgres utilise le système de **rôle** pour gérer les authentifications et les autorisations. Un rôle peu être comparé un compte UNIX. La seul différence c'est qu'un rôle Postgres ne fait pas la différence entre un compte UNIX et un groupe UNIX. C'est pour cela qu'ils ont tous regrouper sous le terme de rôle.

A l'installation, Postgres est configuré pour utiliser l'authentification *ident*, ce qu'il fait qu'il associe les rôles Postgres à un compte Unix. Si un rôle existe dans Postgres alors un compte ou un groupe UNIX portant le même nom peu si connecter.

Lors de l'installation de Postgres, un compte ce nommant **Postgres** a été créer. Il est associé au rôle Postgres par défaut. Pour utiliser Postgres, nous pouvons nous connecter à ce compte.

Il y a plusieurs façon d'utiliser ce compte pour accéder à Postgres.

Nous pouvons maintenant lancer le serveur. Cette étape varie en fonction de la distribution que vous utiliser. Personnellement, je n'utilise pas systemd alors je dois faire:
```
sudo /etc/init.d/postgresql start
```
Si votre distribution utilise systemd, vous pouvez faire:
```bash
sudo systemctl start postgresql
```

## 3.1. Basculer sur le compte postgres
Maintenant que le service est lancé, nous allons nous connecter à Postgres. Je vous ai dis qu'il y avait plusieurs méthode, en voici une:
```bash
sudo -i -u postgres
```
Nous venons de nous connecter avec l'utilisateur qui a été créer lors de l'installation de Postgres. Cette utilisateur est associé avec le rôle de Postgres par défaut. Nous pouvons don utiliser la commande `psql` afin de nous connecter.

```bash
psql
```
```postgresql
psql (10.12 (Ubuntu 10.12-0ubuntu0.18.04.1))
Type "help" for help.

postgres=#
```
Nous sommes maintenant connecter à notre serveur de base de données. C'est depuis ce prompte que nous allons pouvoir manipuler nos bases et nos données.

Pour quitter ce prompte, il faut utiliser la commande `\q`.
```postgresql
postgres=# \q
```
Cela vous ramène au terminal de l'utilisateur postgres.

## 3.2. Accéder à un prompte Postgres sans changer de compte
Nous venons de voir comment nous pouvions nous connecter à Postgres an passant par l'utilisateur postgres. Il existe une méthode qui nous permet de nous connecter sans changer d'utilisateur et cela grâce à `sudo`. 

Dans l'exemple précédent, nous nous sommes d'abord connecté à l'utilisateur postgres et ensuite, nous avons entré la commande `psql`. Il est possible de faire ces deux étapes en une seul.
```bash
sudo -u postgres psql
```
Cette méthode fait exactement la même chose que la technique précédente, sauf qu'elle ne passe pas par un Bash intermédiaire. 

Nous nous retrouvons donc connecter à `psql` avec l'utilisateur postgres. Pour quitter et revenir au Bash, il faut aussi faire `\q`.
```postgresql
postgres=# \q
```
Cela nous renvoie directement dans le Shell de notre utilisateur courant sans passer par le Shell de l'utilisateur postgres.

Dans de nombreux cas, nous allons vouloir plus d'un rôle Postgres. Nous allons maintenant voir comment en créer de nouveaux.

# 4. Création d'un nouveau rôle
Lors de l'installation de Postgres, seul un rôle est créer, le rôle postgres. Pour en créer de nouveau, il suffit d'utiliser l'outil en ligne de commande `createrole`. L'argument `--interactive` propose d'entrer le nom du nouveau rôle et demande aussi si ce dernier possède des autorisations superutilisateur.

Si nous sommes connecté en temps que l'utilisateur postgres, nous pouvons taper la commande:
```bash
createuser --interactive
```

Nous pouvons aussi directement exécuter cette commande sans passer par le Shell de l'utilisateur postgres.
```bash
sudo -u postgres createuser --interactive
```
Ces commandes lance un script qui vous posera des questions et exécutera les bonnes commandes Postgres pour créer un utilisateur en fonction de nos spécifications.
```bash
Enter name of role to add: test
Shall the new role be a superuser? (y/n) y
```

Notre installation Postgres contient maintenant un nouveau rôle. Nous n'avons par contre pas encore ajouté de base de données. Nous verrons comment faire dans la section suivante.

# 5. Création d'une nouvelle base de données
Par défaut, le système d'authentification de Postgres par du principe que chaque rôle à une base de données qui possède le même nom et à la quel il va connecter l'utilisateur.

Cela veut dire que si dans la section précédente nous avons créer un utilisateur qui se nomme **test**, le rôle va tenter de se connecter à une base de données nommé "test". Pour créer la base de données appropriée, nous devons utiliser la commande `createdb`.

Si nous sommes connecté au compte postgres, nous pouvons taper la commande directement.
```bash
createdb test
```

Si nous ne voulons pas quitter notre compte courant, nous pouvons passer par `sudo`.
```bash
sudo -u postgres createdb test
```

# 6. Ouverture d'une invite Postgres avec le nouveau rôle
Maintenant que nous avons créer notre nouveau rôle et la base de données qui lui est attribué, nous devons créer le compte UNIX qui sera utiliser pour si connecter. Nous devons le faire car par défaut Postgres utilise la méthode **ident** pour connecter les utilisateurs.

Pour créer l'utilisateur, nous devons utiliser la commande `adduser` depuis un utilisateur non root et la précéder de `sudo`. Pour ce faire, utiliser le compte courant plutôt que le compte postgres.
```bash
sudo adduser test
```
Le système nous demande d'entrer un mot de passe. Il est conseillé de mettre un mot de passe fort. Mais nous pouvons supprimer ce mot de passe avec la commande:
```bash
sudo passwd -d test
```

Une foi que le compte est créer, nous pouvons nous connecter à Postgres grâce à la commande:
```bash
sudo -i -u test
psql
```

Ou alors:
```bash
sudo -u test psql
```
Si nous avons bien tout configuré, ces commandes nous connecterons automatiquement.

Si nous voulons que notre utilisateur ce connecte à une autre base de données, nous pouvons utiliser la commande `psql` avec le paramètre `-d` suivit du nom du rôle.
```bash
sudo -i -u test
psql -d postgres
```
Où alors:
```bash
sudo -u test psql -d postgres
```
Une foi connecté, nous pouvons afficher les informations de connexion avec la commande `\conninfo`.
```
test=# \conninfo
```
```
You are connected to database "test" as user "test" via socket in "/var/run/postgresql" at port "5432".
```
Cette commande est très utilise quand nous nous connectons à des base de données qui ne sont pas celles par défaut.

# 7. Création et suppression de tables
Maintenant que nous avons installé et configuré Postgres, nous allons voir quelque tâches de gestion basique. Je rappel que ce papier n'a pas pour but d'apprendre le langage SQL.

Nous allons créer, pour l'exemple, une table qui stocke certaine données. Ici, des équipements d'une place de jeux (playground).

La syntaxe de cette commande est:
```sql
CREATE TABLE table_name (
    column_name1 col_type (field_length) column_constraints,
    column_name2 col_type (field_length),
    column_name3 col_type (field_length)
)
```
Comme nous pouvons le voir, cette commande donne un nom à la table, et crée les colonnes ainsi que le type de colonne et la longueur maximale des champs. Nous pouvons aussi, éventuellement ajouter des contraintes pour chaque colonne.

Pour l'exemple, nous allons créer notre table comme suite.
```sql
CREATE TABLE playground (
    equip_id serial PRIMARY KEY,
    type varchar (50) NOT NULL,
    color varchar (50) NOT NULL,
    location varchar (25) check (location in ('north', 'south', 'west', 'east', 'northeast', 'southeast', 'southwest', 'northwest')),
    install_date date
)
```
Cette commande crée une table qui va stocker les équipement d'une place de jeu. la colonne `equip_id` qui est de type `serial` permet d'avoir un id unique pour chaque entrée. Le type `serial` permet de gérer automatiquement l'incrément de l'id. Nous lui avons aussi mis la contrainte `PRIMARY KEY` qui force le champ à être non null et unique.

Les deux champs `equip_id` et `install_date` n'ont pas de longueur de champ. En effet, certain type de données n'ont pas besoin d'une grandeur maximum car elle est déduire par Postgres.

Les deux champs `type` et `color` qui ne peuvent pas être vide.

La colonne `location` ne peu contenir que l'une des 8 valeurs que nous lui avons spécifié.

Voici comment afficher la table que nous venons de créer.
```
test=# \d
```
```
                  List of relations
 Schema |          Name           |   Type   | Owner
--------+-------------------------+----------+-------
 public | playground              | table    | test
 public | playground_equip_id_seq | sequence | test
(2 rows)
```
Nous voyons bien notre table *playground*. Mais nous voyons aussi un objet de type `sequence` qui se nomme `playground_quip_id_seq`. C'est une représentation du type `serial` que nous avons mis dans la table. Elle aide Postgres à incrémenter l'id à chaque nouvelle entrée.

Pour voir la table *playground* sans voir la séquence, nous devons utiliser:
```
test=# \dt
```
```
          List of relations
 Schema |    Name    | Type  | Owner
--------+------------+-------+-------
 public | playground | table | test
(1 row)
```

# 8. Ajout, requête et suppression de données dans une table
Maintenant que nous avons une table nous allons pouvoir y insérer des données.

Pour l'exemple, nous allons ajoutez un toboggan et une balançoire. Pour cela, nous allons appeler les colonnes qui nous intéresse dans la table *playground*.
```sql
INSERT INTO playground (
  type, 
  color, 
  location, 
  install_date
) VALUES (
  'slide',
  'blue',
  'south',
  '2020-06-20'
);

INSERT INTO playground (
  type,
  color,
  location,
  install_date
) VALUES (
  'swing',
  'yellow',
  'northwest',
  '2019-04-22'
);
```
Nous devons faire attention à certaine chose quand nous écrivons nos requêtes. La première chose et que nous ne devons pas donner de valeur à la colonne `equip_id`. Postgres s'en charge tout seul.

Une autre chose à noter est que les noms de colonne sont écrient telle quel alors que les valeurs sont entre guillemets.

Maintenant que nous avons ajouter des données, nous pouvons les afficher.
```sql
SELECT * FROM playground;
```
```
 equip_id | type  | color  | location  | install_date
----------+-------+--------+-----------+--------------
        1 | slide | blue   | south     | 2020-06-20
        2 | swing | yellow | northwest | 2019-04-22
(2 rows)
```
Comme nous pouvons le constater, toute nos données sont là. Le champ `equip_id` a bien été renseigné automatiquement.

Si nous voulons, par exemple, supprimer le toboggan, nous pouvons utiliser `DELETE`.
```sql
DELETE FROM playground WHERE type = 'slide';
```
Si nous affichons à nouveau notre table, nous allons nous rendre compte que notre entrée a bien disparu.
```sql
SELECT * FROM playground;
```
```
 equip_id | type  | color  | location  | install_date
----------+-------+--------+-----------+--------------
        2 | swing | yellow | northwest | 2019-04-22
(1 row)
```

# 9. Ajout et suppression de colonnes dans une table
Maintenant que nous avons vu comment ajouter une entrée est la supprimer, nous allons voir comment ajouter un champ dans la table.

Nous allons ajouter un champ qui va stocker la date de la dernière maintenance.
```sql
ALTER TABLE playground
ADD last_maint date;
```
Si nous affichons notre table, nous nous rendons compte que le nouveau champ est bien présent.
```sql
SELECT * FROM playground;
```
```
 equip_id | type  | color  | location  | install_date | last_maint
----------+-------+--------+-----------+--------------+------------
        2 | swing | yellow | northwest | 2019-04-22   |
(1 row)
```
Pour supprimer une champ, c'est tout aussi facile.
```sql
ALTER TABLE playground
DROP last_maint;
```
Cela supprime le champ `last_maint` ainsi que toutes les données qu'il comporte alors que les autres données ne sont pas altérée.

# 10. Mise à jour des données dans une table
Nous devons encore voir comment mettre à jour des données que nous avons inséré dans la table.

Pour mettre à jour notre entrée, il faut cibler l'une où les entrées que nous voulons modifier. Cela ce fait grâce au `WHERE`. Ici je veux changer la couleur de tous les toboggan (même si il n'y en a qu'un dans ma table).
```sql
UPDATE playground
SET color = 'red'
WHERE type = 'swing';
```
Maintenant, si nous affichons de nouveau notre table, nous allons nous rendre compte que la couleur de notre toboggan à bien changé.
```sql
SELECT * FROM playground;
```
```
 equip_id | type  | color | location  | install_date
----------+-------+-------+-----------+--------------
        2 | swing | red   | northwest | 2019-04-22
(1 row)
```


# 11. Liens

- [x] [Source](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04-fr)
- [ ] [Découvrir comment créer et gérer des tables avec Postgres](https://www.digitalocean.com/community/tutorials/how-to-create-remove-manage-tables-in-postgresql-on-a-cloud-server) (Data type)
- [ ] [Découvrir comment sécuriser PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-secure-postgresql-on-an-ubuntu-vps)