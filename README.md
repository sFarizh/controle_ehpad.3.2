# Structure du projet
``` bash
main.py
README.md
_ data
    |_ input
        demo.xlsx
    |_ to_csv
        demo.csv
    |_ output
        demo.csv
    |_ database
        controle_ehpad.db
	demo.db
_ modules
    |_ init_db
        init_db.py
    |_ transform
        transform.py
    |_ export
        export.py
_ utils
        utils.py
_ settings
        settings.json
        settings_demo.json
```

# Fonctionnalités du script
Ce script permet de générer un fichier excel qui contient les données de ciblage et de controle des établissements de santé.
Pour l'utiliser il faut appeler les commandes mentionnées ci-dessous et elles permettent:
* create_csv : de créer un csv pour chacun des fichiers déposé dans input
* init_db : initialise la base de donné
* load_csv :  charge chaque csv comme une table
* export : exécute les requêtes sql permettant de générer le fichier d'export pour la région demandée et renvoie l'export dans output avec 1 sheet ciblage et 1 sheet controle.

# Prérequis
Pour les données dans input : 
* les fichiers doivent être organisés par dossier, un dossier par source.
* les csv doivent être avoir comme séparateur ';'
* les fichiers excel et csv doivent avoir le titre des colonnes sur la première, aucune colonne vide avant.
* les settings présents dans settings.demo : 
    `* le nom de la base de données`
    `* les noms de régions à afficher pour l'output` 

# Commandes du script
* python main.py create_csv
* python main.py init_database
* python main.py load_csv
* python main.py export [code_region]
* python main.py all [code_region]
