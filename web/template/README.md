# Template

## Objectif

Mon but est de créer un template `HTML` + `CSS` qui soit responsive. Il doit se décliner en 3 versions : mobile, tablette et ordinateur.

Ce projet doit me permettre d'apprendre l'utilisation des grid et des flexbox CSS afin de faire un site responsive. Il me permet aussi d'avoir un template que je peux réutiliser et modifier à la volée.

Je vais sûrement réutiliser ce template pour mon cv internet. Cela sera un bon moyen de le tester dans de vrais cas d'utilisation et voir comment il s'adapte au contenu.

Afin de rendre le template facile à étendre et facile a migrer, je vais utiliser la notation BEM (
Block, Element and Modifier). Cette notation permet de facilement réutiliser des portions de code et se marrie très bien avec SASS.

### Key Words

- Responsive
- Mobile First
- MediaQuery
- HTML + CSS
- BEM

## Conception

### POC

- [premier jet (excalidraw)](https://excalidraw.com/#json=5405009382473728,8E_HyQGC5HLAUJ1sBliIMg)
- Maquette ([Tool](https://penpot.app/?source=korben.info))

### HTML

```html
<div id="grid-container">
    <header>
        <div id="hamburger_open"></div>
        <div id="title"></div>
        <div id="breadcrumb"></div>
    </header>
    <nav>
        <div id="hamburger_close"></div>
        <div id="search"></div>
        <div id="login"></div>
        <div id="menu"></div>
        <div id="social"></div>
    </nav>
    <section id="main"></section>
    <aside></aside>
    <footer></footer>
</div>
```

Voici la structure de base que j'ai en tête pour la page. le but est de mettre en page ces sections grace à la grille CSS.

Il faudra sûrement revoir cette structure en fonction de de ce que j'apprend en cours de route. Par exemple, je ne sais pas si je pourrais garder la structure de l'icone hamburger, surtout pour l'icone `hamburger_close`.

### CSS

Pour le css, je pense le séparer en plusieurs fichier afin de rendre la personalisation et la réutilisation plus facile. Les feuilles de style qui me viennet en tête à l'heure actuelle :

- reset.css
- template.css
- elements.css
- typo.css

Cette structure va sûrement changer au fur et à mesure du projet. Il faudra que je réfléchisse profondément à cette structure afin de facilité la migration vers SCSS qui pourrait se faire par la suite.

#### reset.css

Cette feuille de style doit permettre de supprimer tous les styles par défaut appliqué par les navigateurs. Elle permet d'avoir une page de base uniforme sur tous les naviageteur et de partir sur de bonne base.

Il existe beaucoup de fichier reset déjà fait sur internet. Je vais en choisir un et l'utiliser. Le critère principal de cette feuille de style et d'être légère afin de garder le template adaptable à toute situation.

#### template.css

Ce fichier va contenir tous les styles qui ont un rapport avec la structure de la page. Le but de ce fichier est d'avoir une seul feuille de style à modifié afin de changer le template.

Ce fichier va aussi contenir toute les mediaQuery qui permettrons à notre site d'être responsive et donc agréable à parcourir depuis tous les devices.

#### elements.css

Ce fichier va acuillr tous les styles qui ont un rapport avec la mise en forme des elements html.

C'est ici que nous allons retrouver la configuration de nos bouttons par exemple.

#### typo.css

Cette feuille de style va contenir ce qui a un rapport avec la typographie.

#### Futur

Il faudra peut être spliter le fichier `elements.css` en plusieurs fichier. Cela pourrait permettre de mieux séparer chaque fonctionalité. Par exemple, nous pourrions avoir un fichier `form.css` qui va gérer l'affichage des formulaires et un fichier `button.css` pour l'affichage des boutons. Cela va aussi peu être permettre de faire plus facilement la migration vers SCSS.

Je réfléchis aussi à ajouter un fichier `responsive.css` afin de gérer les mediaQuery qui on un rapport avec la partie responsive de la page.

Pour répondre à ces questions, il faut que je me mette sérieusement dans la doc.

## Liens

- [CSS grid off-Canvas Menu](https://webdesign.tutsplus.com/tutorials/how-to-build-an-off-canvas-navigation-with-css-grid--cms-28191)
- [CSS Grid Responsive](https://blogs.infinitesquare.com/posts/web/creer-une-mise-en-page-avec-css-grid-layout)
- [Hamburger Icon](https://www.w3schools.com/howto/howto_css_menu_icon.asp)
- [Responsive Typo - Technique 62.5%](https://www.youtube.com/watch?v=zEFzBxM7g-k)
- [Mobile First](https://www.youtube.com/watch?v=TldlZRKBpAk)
- [BEM website](http://getbem.com/)
- [BEM vidéo](https://www.youtube.com/watch?v=er1JEDuPbZQ)

## Réalisation

## Améliorations

- Ajouter thème sombre en full CSS [info](https://css-tricks.com/a-complete-guide-to-dark-mode-on-the-web/#os-level)
- Utilise SCSS
