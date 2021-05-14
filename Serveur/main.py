from fastapi import FastAPI
from fastapi.responses import JSONResponse

import requests

app = FastAPI()

id = ""

def Creation_Deck():
    global id
    deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    json = deck.json()
    id = json["deck_id"]


@app.get("/")
def readRoot():
    return {"API : https://deckofcardsapi.com/"}

@app.get("/creer-un-deck")
def Creer_Deck():
    Creation_Deck()
    return {"deck_id":id}

@app.post("/cartes")
def Tirer_Carte():
    
    return res