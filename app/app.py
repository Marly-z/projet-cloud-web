
import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# connexion Mongo
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)
collection = client["catalogue"]["ordinateurs"]

DONNEES = [
    {"marque":"Dell","modele":"Latitude 7440","os":"Windows 11","prix":1450},
    {"marque":"Apple","modele":"MacBook Air M3","os":"macOS","prix":1599},
    {"marque":"Lenovo","modele":"ThinkPad X1","os":"Ubuntu 24.04","prix":1750},
]

if collection.count_documents({}) == 0:

 collection.insert_many(DONNEES)

@app.route("/")
def index():
    ordis = list(collection.find({}, {"_id": 0}))
    return render_template("index.html", ordinateurs=ordis)

@app.route("/ajouter", methods=["POST"])
def ajouter():
    collection.insert_one({
        "marque": request.form.get("marque","").strip(),
        "modele": request.form.get("modele","").strip(),
        "os": request.form.get("os","").strip(),
        "prix": int(request.form.get("prix") or 0),
    })
    return redirect(url_for("index"))
