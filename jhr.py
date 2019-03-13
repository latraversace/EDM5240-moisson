#coding: utf-8

import json
import csv
import requests

### Bon script, qui va puiser dans un API que je ne connaissais pas.
### Qui utilise des trucs que je ne vous ai pas montrés comme des «list comprehensions» et la fonction lambda. Très bien.
### Mais votre documentation partielle me pousse à vous demander si vous comprenez réellement ce que vous avez fait?

# ficher = "Repechages_LNH.csv"
ficher = "Repechages_LNH_JHR.csv" ### Je renomme votre fichier pour tester votre script

adresse = "https://records.nhl.com/site/api/draft/"

entete = {
	"User-Agent":"Julien Latraverse - (514)266-5865 - Journaliste",
	"From":"j.lat@hotmail.ca"
}

keys = ["firstName", "lastName", "birthDate", "countryCode", "position", "pickInRound", "draftYear", "triCode"]
#les clés servent à répertorier les éléments utilisés pour le dictionnaire
### Je comprends que le contenu de la liste keys est en anglais parce que ça doit correspondre aux clés qui se trouvent dans l'API,
### mais pourquoi ne pas franciser les entêtes de colonnes?
colonnes = ["prenom", "prenom", "dateNaiss", "pays", "position", "rang", "anneeRepech", "equipe"]

mike = open(ficher, "a")
komisarek = csv.writer(mike)
# komisarek.writerow(keys)
# komisarek.writerow(colonnes)

req = requests.get(adresse, headers=entete)
if req.status_code == 200:
    json = req.json()
    
    # players = json["data"]
    joueurs = json["data"] ### Hablamos francés

    # for player in filter(lambda player: player["draftYear"] >= 2004 and player["draftYear"] <= 2018 and player["roundNumber"] == 1, players):
    # for joueur in filter(lambda joueur: joueur["draftYear"] >= 2004 and joueur["draftYear"] <= 2018 and joueur["roundNumber"] == 1, joueurs):
    # for joueur in filter(lambda joueur: joueur["draftYear"] >= 2004 and joueur["draftYear"] <= 2018, joueurs):
    for joueur in joueurs:
    	#En gros, avec la fonction filter et lambda, on applique une règle booléenne vrai et fausse sur l'année de repêchage. Si l'année de repêchage du joueur est entre 2004 et 2008, le dictionnaire va s'appliquer. 

        ### Juste sur l'année? Et «player["roundNumber"] == 1», ça fait quoi?
        ### Pourquoi de 2004 à 2018 seulement?

        # komisarek.writerow([player[k] for k in keys])
        # komisarek.writerow([joueur[k] for k in keys])
        ### Pourquoi ne pas tout ramasser, quitte à faire le ménage ensuite?
        komisarek.writerow(joueur.values())
        ### Car il y a des données intéressantes dans l'API, comme la ligue de provenance des joueurs, leur rang dans la ronde, leur poids
        ### Ces données pourraient ensuite permettre de répondre à une foule de questions: les joueurs repêchés ont-ils tendance à être plus lourds? Quelles ligues fournissent le plus de joueurs à la LNH?
        ### Voir ficher ODS inclus dans votre répertoire pour quelques idées.

        ### Ci-dessous, vous affichez dans le terminal tout le contenu que l'API contient sur un joueur sélectionné...
        print(joueur)
        print("~"*80)
        #Le csv va s'écrire avec les joueurs ayant une valeur "vraie" de la fonction booléenne selon les valeurs demandés par la clé du dictionnaire.