#coding: utf-8

import json
import csv
import requests

ficher = "Repechages_LNH.csv"
adresse = "https://records.nhl.com/site/api/draft/"
entete = {
	"User-Agent":"Julien Latraverse - (514)266-5865 - Journaliste",
		"From":"j.lat@hotmail.ca"
}
keys = ["firstName", "lastName", "birthDate", "countryCode", "position", "pickInRound", "draftYear", "triCode"]
#les clés servent à répertorier les éléments utilisés pour le dictionnaire
mike = open(ficher, "a")
komisarek = csv.writer(mike)
komisarek.writerow(keys)
req = requests.get(adresse, headers=entete)
if req.status_code == 200:
    json = req.json()
    players = json["data"]
    for player in filter(lambda player: player["draftYear"] >= 2004 and player["draftYear"] <= 2018 and player["roundNumber"] == 1, players):
    	#En gros, avec la fonction filter et lambda, on applique une règle booléenne vrai et fausse sur l'année de repêchage. Si l'année de repêchage du joueur est entre 2004 et 2008, le dictionnaire va s'appliquer. 
        komisarek.writerow([player[k] for k in keys])
        print(player)
        print("~"*80)
        #Le csv va s'écrire avec les joueurs ayant une valeur "vraie" de la fonction booléenne selon les valeurs demandés par la clé du dictionnaire.
