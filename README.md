# Prod_log_S4
Projet de production logiciel en python.

----------------------------




Utilisation :

mettez vous dans le répertoire src :
cd Prod_log_S4/src

vous avez donc lancé le serveur, vous pouvez maintenant vous y connecter à l'addresse :
http://localhost:10078/






----------------------------

"man" git : https://services.github.com/on-demand/downloads/fr/github-git-cheat-sheet.pdf

review du 09/03/17 :

- Fait :
  - récupération dans le CSV
  - classe activité pour faciliter le passage à la bd
  - début de l'insertion BD.
  - début de la création BD

- A faire /finir :
  - finir le fichier ActivityInsertBD
  - finir la creation de bd si etienne a pas fini
  - PS : j'ai fait de la merde avec les fichier, y en  a en trop qui servent à rien , ils faut les supprimer


review du 16/03/17 :
- Fait :
  - création bd
  - réorganisation des fichiers
  - j'ai supprimé les fichiers inutiles
  - blockage sur pb insert bd


- A faire /finir :
  - "copier coller" tout les fichiers de activity pour faire les instalations/équiements
  - remplir table équipAct
  - FAUT FINIR LA PARTIE REMPLISSAGE BD IMPORTANT!!!
  - si on avance bien, faire des getter pour la bd (ex: pouvoir récupérer les équipement d'une ville)

review du 23/03/17 :
- Fait :
  - pb de insert résolu, il manquait juste le commit() à la fin !!!!!!!!!!
  - importations de toutes les tables fini
  - organisation des fichiers dans le dossier "importation"

- A faire /finir :
  - voir la librairie bottle et avancer sur ca
  - faire les getters intéressant pour la bd


review du 30/03/17 :
- Fait :
  - une base avec bottle
    -> bottle marche pas comme je veux
        -> faire gaffe au chemin !!!
  - getters plus ou moins (Etienne)


- A faire /finir :
  - finir ce qu'on a commencer

review du 03/04/17 : //oui on est en retard, et alors ??
- Fait :
  - préparation des trucs à finir pour demain parce que ca marche pas trop sous windows (bloque des ports, des imports...)


- A faire /finir :
  - finir les getter
  - à recheck : ajax -> formatage des jsonObj, route bottle

LAST REVIEW (04/04/17):
- Fait :
  - des getters de base de données
  - une route -> qui renvoie du json
  - début de recherche via la page html (ajax)-> pb de formatage de la chaine json?

- Ce qui marche pas:
  - la recherche via page html

- ce qui reste à faire
  - plus de route et donc plus de getter.
  - une vue cool pour le client.
  - faire un fichier pour import toute la bd d'un coup, ca serait plus pratique.
  - ajouter une google map pour l'affichage des résultats
