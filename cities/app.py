from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/ville/<nom>")
def infos_ville(nom):
    try:
        time_resp = requests.get(f"http://times:5000/time/{nom}")
        time_data = time_resp.json()

        if time_resp.status_code != 200:
            return jsonify({"erreur": time_data.get("erreur", "Erreur inconnue")}), 404

        message = {
            "ville": time_data["ville"],
            "pays": "Maroc",
            "continent": "Afrique",
            "description": f"{time_data['ville']} est une ville marocaine.",
            "heure_locale": time_data["heure"]
        }
        return jsonify(message)

