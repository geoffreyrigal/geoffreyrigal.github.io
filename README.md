# Portfolio - Geoffrey Rigal

Bienvenue sur le dépôt de mon portfolio personnel, accessible en ligne à l'adresse **[geoffreyrigal.github.io](https://geoffreyrigal.github.io)**.

Ce site web a été conçu pour regrouper et présenter mes différents projets (personnels et académiques réalisés au cours de mon BUT Informatique à l'IUT du Limousin), ainsi que mon CV.

---

## Fonctionnalités

- **Chargement dynamique des projets** : L'ensemble des projets est stocké dans le fichier `content.json`. Le menu de navigation (classé par catégories : *Personnel*, *Scolaire*, etc.) ainsi que le contenu des fiches projets sont générés dynamiquement en JavaScript, permettant d'ajouter ou de modifier un projet sans toucher au code HTML/JS.
- **Carrousel d'images interactif** : Navigation entre les captures d'écran d'un projet via des boutons, des indicateurs (points), les flèches du clavier (`←` / `→`) ou par glissement tactile (*swipe*) sur mobile.
- **Thème Clair / Sombre (Dark Mode)** : Bascule entre le thème clair et sombre avec détection automatique des préférences du système (`prefers-color-scheme`) et sauvegarde du choix dans le `localStorage`.
- **Design Responsive** : Interface adaptée aux écrans d'ordinateur et aux appareils mobiles (avec un menu déroulant dédié sur petit écran).
- **Consultation du CV** : Page dédiée intégrant directement mon CV au format PDF.

---

## Technologies utilisées

- **HTML5** : Structure sémantique des pages.
- **CSS3** : Mise en page responsive, variables CSS pour la gestion des thèmes clair/sombre.
- **JavaScript (Vanilla)** : Manipulation du DOM, récupération asynchrone des données (`fetch`), gestion du carrousel et du thème.
- **JSON** : Stockage structuré des données des projets.
- **GitHub Pages** : Hébergement du site statique.

---

## Structure du projet

```text
├── index.html          # Page principale (présentation des projets)
├── cv.html             # Page de consultation du CV
├── style.css           # Feuille de style principale et thèmes
├── cv.css              # Styles spécifiques à la page CV
├── script.js           # Logique d'injection des projets, carrousel et thème
├── content.json        # Données de tous les projets affichés sur le site
├── content/            # Fichiers téléchargeables / intégrés (CV en PDF)
└── img/                # Captures d'écran des projets et icônes SVG
```

---

## Ajouter un nouveau projet

Pour ajouter un projet au portfolio, il suffit d'ajouter une nouvelle entrée dans le tableau du fichier `content.json` en respectant le format suivant :

```json
{
    "category": "Personnel",
    "title_menu": "Nom court (affiché dans le menu)",
    "title": "Titre complet du projet",
    "date": "Période de réalisation",
    "languages": ["Langage 1", "Langage 2"],
    "techno": ["Technologie 1", "Outil 2"],
    "usage": "Contexte et objectif du projet.",
    "description": "Description détaillée de la conception et de la réalisation.",
    "link_img": ["img/image1.png", "img/image2.png"],
    "alt_img": "Texte alternatif des images",
    "repo": "https://github.com/geoffreyrigal/nom-du-repo"
}
```

> **Note :** Si le projet ne possède pas de dépôt public ou d'images, laissez simplement `"repo": ""` ou `"link_img": []` ; l'interface masquera automatiquement les sections correspondantes.

---

## Exécution en local

Comme le script utilise l'API `fetch()` pour lire le fichier `content.json`, l'ouverture directe du fichier `index.html` via le protocole `file://` peut être bloquée par les règles CORS du navigateur. Il est recommandé de lancer un petit serveur local :

```bash
# Avec Python 3
python3 -m http.server 8000
```

Puis d'ouvrir `http://localhost:8000` dans votre navigateur (ou d'utiliser l'extension **Live Server** sur VS Code).

---

## Contact

- **Email** : [rigalgeoffrey19@gmail.com](mailto:rigalgeoffrey19@gmail.com)
- **Téléphone** : 07-66-28-11-83
- **LinkedIn** : [Geoffrey Rigal](https://www.linkedin.com/in/rigal-geoffrey-820a33341)
