Troisieme_programme/
│
├── main.py                 # point d’entrée
├── requirements.txt
│
├── core/                   # LOGIQUE DU JEU (agnostique du rendu)
│   ├── __init__.py
│   ├── player.py           # joueur (pv, classe, attaques)
│   ├── combat.py           # pve(), règles de combat
│   ├── map.py              # map logique (grille, collisions)
│   ├── mobs.py             # définition des ennemis
│
├── spells/                 # attaques / sorts
│   ├── __init__.py
│   ├── player_spells.py
│   ├── mob_spells.py
│
├── render/                 # AFFICHAGE
│   ├── __init__.py
│   ├── console.py          # affichage texte (optionnel)
│   ├── pygame_renderer.py  # affichage graphique
│
├── assets/                 # ressources graphiques
│   ├── tiles/
│   │   ├── ground.png
│   │   ├── wall.png
│   │   ├── grass.png
│   │   └── center.png
│   ├── player/
│   │   └── player.png
│   └── mobs/
│       ├── poule.png
│       └── boss.png
│
├── maps/
└── saves/
    └── save.json