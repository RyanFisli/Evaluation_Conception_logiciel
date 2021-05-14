import requests
import json

url = "http://localhost:8000"

def get_id():
    return requests.get(url+"/creer-un-deck/")

id = get_id().json()["deck_id"]
print("id = ", id)

nb_cartes = 10
jeu = {"nombre_cartes": nb_cartes}
requete = requests.post(url+"cartes",json=jeu)
jeu_de_cartes = requete.json()

def compte(jeu_cartes):
    H,S,D,C = 0,0,0,0
    for c in jeu_cartes["cartes"]:
        if c["suit"] == "HEARTS":
            H += 1
        elif c["suit"] == "SPADES":
            S += 1
        elif c["suit"] == "DIAMONDS":
            D += 1
        elif c["suit"] == "CLUBS":
            C += 1
    return {"H" : H, "S" : S, "D" : D, "C" : C}

print(compte(jeu_de_cartes))