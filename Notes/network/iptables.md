# Principes et notions

Iptables est un firewall qui touche au couches les plus basse du réseau. Se qui lui permet de faire du filtrage par ip, ports et protocole mais aussi de la translation et modifié des paquets à la volé. C'est un outils en ligne de commande qui est très puissant. Il se fait aussi appeler *netfilter* dans la communauté. Il s'agit du même programme.

Pour l'installer, c'est très simple. Si il n'est pas déjà présent dans votre distrib de base, il se trouve dans la majorité des dépôt. Il suffit donc de faire :

```bash
apt-get install iptables
```

Si vous n'avez pas apt, il suffit d'utiliser le gestionnaire de paquet par défaut de votre distrib.

## Les tables

Pour sont fonctionnement **Iptables** se base sur 3 tables. Pour configurer notre firewall, nous allons rajouter des règles dans ces tables.

### La table NAT

La table NAT s'occupe de la translation de ports et d'IP. Cette table permet de spécifié deux locations (a quel moment s'applique une règles). Soit PREROUTING (avant le firewall), soit POSTROUTING (après le firewall). En plus des 2 locations, nous pouvons spécifié 3 targets différentes. DNAT(Destination NAT) qui est l'ip de destination, SNAT(Source NAT) qui est l'IP source et MASQUERADE qui simule une passerelle par défaut.

### La table filter

Cette table sert principalement à filtrer les paquets, c'est l'endroit pour intervenir directement sur les paquets et analyser leurs contenus. 

Cette table permet l'utilisation de 3 chaines. Elle serve à spécifié  ce que nous voulons faire avec les paquets. INPUT représente les paquets entrain, OUTPUT représente les paquets sortant et FORWARD les paquets en transite.

Cette table nous permet aussi l'utilisation de plusieurs targets. Les targets sont des actions que nous pouvons faire sur des paquets. DROP permet de refuser un paquet sans retour à l'utilisateur, ACCEPT permet accepter un paquet, REJECT permet de refuser un paquet et de notifié à l'utilisateur, LOG permet de garder une trace d'un paquet dans un fichier log. 
Il existe encore beaucoup de targets, nous en verrons certaine dans ce tutoriel.

### La table mangle

Cette table est spécialisée dans la modification de paquets. Pour remplir cette tâche, elle utilise 5 targets. TOS, qui est le type de service, TTL, qui est la durée de vie du paquet(nombre de saut), MARK, qui permet de marqué (taggé) un paquet afin de le suivre, SECMARK, pareil que MARK sauf que réservé pour des outils de sécurité (type SE Linux) et CONNSECMARK, qui a aussi un rapport avec la sécurité.

# Les options et chaines

## Les options principales

- **-L** : Permet de lister les règles. Nous pouvons aussi ajouter **--line-numbers** afin d'afficher le numéro de chaque règle. Le numéro de la règle permet de l'identifié, si vous voulez éditez une règle, il faudra spécifié son numéro.
- **-t** : permet de spécifié la table. NAT, filter ou mangle.

## Type d'action chaines

- **-A** : Permet d'ajouter une règle à la chaine (-A INPUT). 
- **-D** : Permet de supprimer une règle (-D INPUT <num_règle>).
- **-R** : Permet de remplacer une règle (-R INPUT <num_règle>).
- **-I** : Permet d'insérer une règle (-I INPUT <num_règle>). Il est possible de ne pas mettre de numéro de règle. Si c'est le cas, la règle sera insérer au début du stack.
- **-F** : Permet de flush toutes les règles d'une chaine (-F INPUT) ici nous supprimons toutes les règles de la chaine INPUT.
- **-N** : Permet de créer des règles personnalisée (-N <name>). 
- **-X** : Permet de supprimer une chaine (-X <name>).
- **-P** : Permet de stipuler le comportement par défaut d'une chaine (-P INPUT DROP).

## Caractéristiques 

- **-p** : Permet de spécifier un protocole (-p tcp).
- **-s** : Permet de spécifier une source (ip, réseau).
- **-j** : Permet de spécifier l'action de règle (DROP, REJECT, ACCEPT).
- **-d** : Permet de spécifier la destination (ip, réseau).
- **-i** : Permet de spécifier l'interface d'entrée (eth0, ...).
- **-o** : Permet de spécifier l'interface de sortie (eth0, ...).
- **--sport** : Permet de spécifier le port source.
- **--dport** : Permet de spécifier le port de destination.
- **-m** : Permet de spécifier plusieurs ports dans --sport ou --dport.
- **-t** : Permet de spécifier la table (NAT, filter ou mangle).

# Première règles, DROP ping

Nous allons maintenant mettre en pratique ce que nous avons vu dans les chapitres précédent. Pour l'exemple, nous allons bloquer les pings sur notre machine. Pour le moment, aucune règle n'est spécifiée, je peux donc ping ma machine sur son IP. 

Pour ce faire, nous devons créer une règle, qui va DROP tous les paquets ICMP en entrée de notre machine. Le protocole ICMP est le protocole utiliser pour faire passer un ping.

```bash
iptables -I INPUT -p icmp --icmp-type 8 -j DROP 
```

Si vous avez suivit les chapitre précédent, cette règle devrait vous parler.

- **-I INPUT** : Indique que nous voulons insérer une règles. Ici nous spécifions pas de numéro, la règle va donc s'ajouter au début du stack. Nous spécifions aussi que nous voulons ajouter la règle à la chaine INPUT.
- **-p icmp** : indique que nous voulons travailler sur le protocole ICMP.
- **--icmp-type 8** : Nous n'avons pas encore vu cet argument. ICMP permet de spécifié un type d'élément. Ici le type 8 correspond à l'echo request. C'est le type de ping le plus commun qui permet interroger une machine pour savoir si elle est up.
- **-j DROP** : Indique que nous voulons DROP les paquets.

Afin de nous assurer que la règle est bien passé. Il suffit de passer la commande **iptables -L** afin d'afficher les règles. Vous devriez la voir apparaitre. Un foi fait, vous pouvez essayer de pinger la machine, si tous c'est bien passé, elle ne devrait pas répondre.  

Nous allons maintenant supprimer cette règle. Pour se faire, nous devons connaitre le numéro de la règle. Nous allons faire un **iptables -L --line-numbers** afin de chopper l'info. Pour le moment, cette manipe n'est pas très utile car nous avons créer qu'une règle. Cela va s'avérer beaucoup plus utile quand nous aurons beaucoup de règle !

```bash
iptables -L --line-numbers
```

Ici, nous pouvons donc constater que notre règle a le numéro 1. Grâce à cette information, nous pouvons maintenant supprimer la règle.

```bash
iptables -D INPUT 1
```

Ici, nous avons demander à iptables du supprimer la première règle de la chaine INPUT. Nous pouvons constater que cela à marché avec un iptables -L et en pingant la machine.

Pour l'exemple, nous allons créer un règle qui empêche notre machine de pinger. Nous allons donc jouer avec la chaine OUTPUT. Cette foi, nous n'avons pas besoin de spécifié un type icmp, car nous voulons bloquer tous les type.

```bash
iptable -I OUTPUT -p icmp -j DROP
```

De nouveau, nous pouvons constater que la règle est bien passée avec un -L et en pingant une ip depuis la machine.

Cette règle n'est pas vraiment utile et n'a pas vraiment de sens. Je la présente ici comme exemple. Je la supprime directement car elle n'a pas de raison d'être. 
```bash
iptable -L --line-numbers
iptable -D OUTPUT 1
```

# Combinaison de règles

Nous allons ici aller un peu plus loin dans la pratique. Dans mon labo j'ai actuellement 3 machines qui ont la configuration suivante :

| Nom  | IP            | Desc     |
| ---- | ------------- | -------- |
| Lab1 | 192.168.8.129 | VM       |
| Lab2 | 192.168.8.130 | VM       |
| L390 | 192.168.8.123 | Physique |

Le but de exercice est de créer un petit serveur web sur la machine **Lab1** qui écoutera sur le port 8000. Une foi que le serveur web tourne, le but va être de le rendre joigne que via la machine **Lab2**, les autres machine devront être bloquée.

## Serveur web

Comme serveur web, je vais utiliser Python. En effet python, que se soit la version 2 comme 3 vient avec un petit serveur web de test. Ce n'est pas un serveur très robuste, il ne faut absolument pas l'utiliser en production, mais il sera parfait pour faire nos tests.

Sur la machine *Lab1*, je commence par créer un dossier web à la racine de mon user. J'y ajoute un petit fichier *index.html*.

```bash
> mkdir web
> cd web
> nano index.html
<html>
<head>
	<title>test</title>
</head>
<body>
	<h1>Test de page web</h1>
</body>
</html>
```

Pour lancer le serveur web, il suffit de se rendre dans ce nouveau dossier et de lancer le serveur.
**Python 2** `python -m SimpleHTTPServer 8000`
**Python 3** `python -m http.server 8000 `

Afin de tester le serveur web, nous pouvons nous connecter à l'adresse de *Lab1* depuis le navigateur d'un machine qui est dans le même réseau. Si vous ne voyez pas la page HTML que nous avons créer mais une arborescence de fichier, c'est que vous n'étiez pas dans le dossier web que nous avons créer lors que vous avez lancer le serveur web. 

## Création des règles

Maintenant que nous avons notre infra de test qui est fonctionnel, nous allons pouvoir mettre en place la configuration d'iptables. La configuration sera faite sur la machine *Lab1* qui fait tourner le serveur web.

Une bonne pratique à mettre en place dans ce genre de situation et de commencer par une règles qui refuse toute connexion et par la suite, plus haut dans le stack, mettre des règles pour autorisé que certaine machine.
`iptables -I INPUT -p tcp --dport 8000 -j DROP`
Description de la règle:

- -I INPUT : Nous voulons travailler sur les paquets en entrée
- -p tcp : les paquets qui sont du protocole TCP
- --dport : qui viennent depuis le port 8000
- -j DROP : seront drop

Maintenant que cette règle est en place, vous pouvez tester de vous connecter au serveur web depuis une autre machine du réseau. Si la règle est bien passé, vous devez avoir une erreur.

Nous allons pouvoir ajouter la règles qui autorise ma machine *Lab2*. Avant de le faire, il faut comprendre comment marche le stack. Quand vous avez plusieurs règles, elle prenne chaque une un numéro. Au moment ou un paquet arrive, les règles du stack vont s'appliquer en commencent par la première. Ceci est un peu tricky car il faut que nos règles exécute dans le bon ordre. Actuellement, si nous rajoutons une règles pour autoriser notre machine à la suite de la règle que nous venons de créer, cela ne va pas marcher car il va appliquer la règle qui rejette tous les paquets sur le port 8000. Nous devons donc mettre la règles qui autorise notre machine avant la règle qui bloque tous. 

Nous avons vu plus haut, qu'il existait plusieurs arguments pour ajouter une règle au stack Nous avons vu **-A** et **-I**. Il faut savoir que **-A** ajoute une règles à la fin du stack et que **-I** ajoute une règles au début du stack. Ici nous allons donc utiliser **-I**.
`iptable -I INPUT -s 192.168.8.130 -p tcp --dport 8000 -j ACCEPT`  

Maintenant que la règle est passé, vous pouvez tester de vous connecter au serveur web depuis la machine *Lab2* et *L390*. Si tous c'est bien passé, vous pouvez vous connecter depuis *Lab2* et pas depuis *L390*. 
A se stade, il est intéressant de faire un `iptables -L --line-nummbers` afin d'afficher les règles ainsi que leur position dans le stack. Nous pouvons constater que la règle *ACCEPT* se trouve à la position 1 et que la règle *DROP* se trouve à la position 2. Si ce n'est pas le cas, votre configuration ne marchera pas.

Maintenant que tous marche, nous pouvons supprimer les règles que nous venons de créer. Elle ne nous servirons pas pour la suite et n'était la que pour l'exemple et pour comprendre comment marche le stack.

```bash
iptables -D INPUT 1
iptables -D INPUT 1
```

Ici, je supprime 2 fois à la suite la règle 1 car quand je la supprime pour la première foi, la numérotation du stack est recalculé. La règle 2 prend donc le numéro 1.

Une foi que les règles sont supprimée, nous pouvons constater que toues la machine du réseau peuvent de nous se connecter à notre serveur web.

# Sécurisé une machine

Nous allons ici définir des règles de bonne pratique afin de sécurisé une machine avec Iptables. Nous l'avons vu dans la chapitre précédent, il est une bonne idée de bloqué tous le trafic vers la machine et d'autoriser au cas par cas en fonction des besoins.

Pour commencer, je vais supprimer toutes les règles présente afin de repartir d'une bonne base.

```bash
iptables -F
```

Maintenant que nous avons supprimer les règles, nous allons pouvoir mettre en place nos règles. La première chose que je fais, c'est autoriser le SSH. Je fait cela car j'accède à la machine via SSH et je ne veux pas perdre la connexion.

```bash
iptables -t filter -I INPUT -p tcp --dport 22 -j ACCEPT
iptables -t filter -I OUTPUT -p tcp --sport 22 -j ACCEPT
```

Maintenant que j'ai passé cette règles, je suis sur que je ne vais pas me bloqué. Nous allons pouvoir demander à iptables de bloqué toutes les connexions par défaut.

```bash
iptables -t filter -P INPUT DROP
iptables -t filter -P OUTPUT DROP
iptables -t filter -P FORWARD DROP
```

Ici, nous créons 3 nouvelles règles, une par chaine de la table filter. L'argument **-P** permet de spécifier un comportement par défaut. Ici nous disons donc, que nous voulons drop toute les connexions sur toutes les chaines de la table filter.
Nous pouvons constater le résultat avec **-L**.

```bash
iptables -L
Chain INPUT (policy DROP)
target     prot opt source               destination
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh

Chain FORWARD (policy DROP)
target     prot opt source               destination

Chain OUTPUT (policy DROP)
target     prot opt source               destination
ACCEPT     tcp  --  anywhere             anywhere             tcp spt:ssh
```

Nous voyons que la default policy pour chaque chaine est DROP. Nous pouvons aussi voir les 2 règles que nous avons passer plus tôt afin d'autoriser le SSH.

Maintenant que nous bloquons tous le trafic, nous allons créer des règles qui permette à la machine d'accepter les trafic dans le sens retour d'une connexion. Cela permet que si vous arriver à établir une connexion avec une autre machine, que les paquets qui sont retourner soit accepté.

```bash
iptables -I INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -I OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
```

Maintenant, nous avons la configuration de base. Nous allons pouvoir commencer à ouvrir les ports dont nous avons besoin.
Je commence par autoriser le ping. Cela n'est pas une nécessité mais le ping peu s'avérer pratique pour connaitre l'état d'une machine sur le réseau.

```bash
iptables -t filter -A INPUT -p icmp -j ACCEPT
iptables -t filter -A OUTPUT -p icmp -j ACCEPT
```

Maintenant que le ping est autoriser, nous pouvons nous rendre compte que si nous voulons pinger un serveur web depuis notre machine, cella ne marche pas. Cela vient du fait que les ports pour les DNS sont fermer et donc la résolution ne peu pas se faire. Nous allons ajouter des règles afin de régler ce problème.

```bash
iptables -A INPUT -p udp --sport 53 -j ACCEPT
iptables -A INPUT -p udp --dport 53 -j ACCEPT
iptables -A OUTPUT -p udp --sport 53 -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
```

Si vous pouvez pinger un TLD externe, c'est que la configuration DNS est bonne.

Je vais maintenant autoriser la connexion au port 80 et 443 afin que la machine puisse ce connecter au web.

```bash
iptables -t filter -A OUTPUT -p tcp --dport 80 -j ACCEPT
iptables -t filter -A OUTPUT -p tcp --dport 443 -j ACCEPT
```

Pour le moment cette configuration me suffit. Elle protège ma machine de manière convenable et me permet d'utiliser les services dont j'ai besoin. Voici un résumer de cette configuration.

```bash
iptables -L --line-numbers
Chain INPUT (policy DROP)
num  target     prot opt source               destination
1    ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
2    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh
3    ACCEPT     icmp --  anywhere             anywhere
4    ACCEPT     udp  --  anywhere             anywhere             udp spt:domain
5    ACCEPT     udp  --  anywhere             anywhere             udp dpt:domain

Chain FORWARD (policy DROP)
num  target     prot opt source               destination

Chain OUTPUT (policy DROP)
num  target     prot opt source               destination
1    ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
2    ACCEPT     tcp  --  anywhere             anywhere             tcp spt:ssh
3    ACCEPT     icmp --  anywhere             anywhere
4    ACCEPT     udp  --  anywhere             anywhere             udp spt:domain
5    ACCEPT     udp  --  anywhere             anywhere             udp dpt:domain
6    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:http
7    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:https
```

# Faire du Load-Balancing avec Iptables

# Sauvegarde et restauration

Nous allons voir dans ce chapitre comment sauvegarder les règles que nous avons créer. En effet, actuellement, si la machine reboot, toutes les règles disparaitront. Cela est un problème car c'est long et difficile de mettre en place toutes les règles.

Nous allons utiliser la commande `iptables-save > <path>`. Cette commande est présente dans le paquet *iptables* que nous avons installer au tout début. Vu que c'est un fichier de configuration, je vais le stocker ce fichier dans le dossier courant de mon utilisateur dans un dossier nommer *conf*. 

```bash
iptables-save > ~/conf/sav-iptables.rules
```

Maintenant, je peu constater que le fichier existe et qu'il contient bien toutes mes règles.

```bash
cat ~/conf/sav-iptables.rules
# Generated by iptables-save v1.6.1 on Tue Apr 28 18:50:15 2020
*filter
:INPUT DROP [2401:175296]
:FORWARD DROP [0:0]
:OUTPUT DROP [6:450]
-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
-A INPUT -p icmp -j ACCEPT
-A INPUT -p udp -m udp --sport 53 -j ACCEPT
-A INPUT -p udp -m udp --dport 53 -j ACCEPT
-A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
-A OUTPUT -p tcp -m tcp --sport 22 -j ACCEPT
-A OUTPUT -p icmp -j ACCEPT
-A OUTPUT -p udp -m udp --sport 53 -j ACCEPT
-A OUTPUT -p udp -m udp --dport 53 -j ACCEPT
-A OUTPUT -p tcp -m tcp --dport 80 -j ACCEPT
-A OUTPUT -p tcp -m tcp --dport 443 -j ACCEPT
COMMIT
# Completed on Tue Apr 28 18:50:15 2020
```

Maintenant que notre fichier est créer, nous pouvons le restaurer avec `iptables-restore < ~/conf/sav-iptables.rules`.
Pour se faire, je commence par redémarrer ma machine afin de faire disparaitre toutes mes règles.

```bash
iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
```

Effectivement, nos règles ont bien disparu. Afin de les restaurer, il me suffi de :

```bash
iptables-restore < ~/conf/sav-iptables.rules
iptables -L --line-numbers
Chain INPUT (policy DROP)
num  target     prot opt source               destination
1    ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
2    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh
3    ACCEPT     icmp --  anywhere             anywhere
4    ACCEPT     udp  --  anywhere             anywhere             udp spt:domain
5    ACCEPT     udp  --  anywhere             anywhere             udp dpt:domain

Chain FORWARD (policy DROP)
num  target     prot opt source               destination

Chain OUTPUT (policy DROP)
num  target     prot opt source               destination
1    ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
2    ACCEPT     tcp  --  anywhere             anywhere             tcp spt:ssh
3    ACCEPT     icmp --  anywhere             anywhere
4    ACCEPT     udp  --  anywhere             anywhere             udp spt:domain
5    ACCEPT     udp  --  anywhere             anywhere             udp dpt:domain
6    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:http
7    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:https
```

Nous nous sommes déjà bien facilité le travail en créant ce fichier de configuration. Nous pouvons encore aller plus loin en automatisant le restaure au lancement de la machine. Il nous faut aussi nous assurer que la configuration soit appliquer le plus rapidement possible. Ceci est important car quelqu'un de mal intentionné pourrait utiliser le moment de battement qu'il y a entre le moment ou le routeur reboot et le moment ou la configuration est effectivement appliquée pour faire des choses qui normalement sont interdite par les règles.

Pour se faire, nous pouvons invoqué le binaire *pre-up* dans la configuration de notre carte réseau. Pour se faire, il faut éditer le fichier */etc/network/interfaces* et y ajouter notre commande pre-up.

```bash
cat /etc/network/interfaces
# interfaces(5) file used by ifup(8) and ifdown(8)
auto lo
iface lo inet loopback

auto enp0s3
iface enp0s3 inet dhcp
        pre-up iptables-restore < ~/conf/sav-iptables.rules
```

Comme vous pouvez le voir, dans la configuration de mon interface principale (enp0s3), j'ai rajouter la ligne `pre-up iptables-restore < ~/conf/sav-iptables.rules`. C'est cette ligne qui stipule que nous voulons restaurer notre configuration au moment ou le réseau est disponible. 
Pour tester que notre configuration est bien passée, je reboot la machine et j'affiche les règles.

```bash
iptables -L --line-numbers
Chain INPUT (policy DROP)
num  target     prot opt source               destination
1    ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
2    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh
3    ACCEPT     icmp --  anywhere             anywhere
4    ACCEPT     udp  --  anywhere             anywhere             udp spt:domain
5    ACCEPT     udp  --  anywhere             anywhere             udp dpt:domain

Chain FORWARD (policy DROP)
num  target     prot opt source               destination

Chain OUTPUT (policy DROP)
num  target     prot opt source               destination
1    ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
2    ACCEPT     tcp  --  anywhere             anywhere             tcp spt:ssh
3    ACCEPT     icmp --  anywhere             anywhere
4    ACCEPT     udp  --  anywhere             anywhere             udp spt:domain
5    ACCEPT     udp  --  anywhere             anywhere             udp dpt:domain
6    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:http
7    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:https
```

Toutes mes règles ont étés re-appliquée et au meilleur moment du point de vue de la sécurité.

