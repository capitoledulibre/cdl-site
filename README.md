Site du Capitole du Libre
=========================

Le site du Capitole du Libre, incluant l'appel à conférence, la gestion des propositions et des intervenants.

## Installation

Prerequis

    sudo apt-get install python-dev python-setuptools python-virtualenv build-essential

Environnement de développement (ou de production)

    virtualenv symposion2015
    source symposion2015/bin/activate
    git clone git@github.com:toulibre/cdl-site.git

Installation

    cd cdl-site
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py loaddata fixtures/*

## Démarrage

    python manage.py runserver
