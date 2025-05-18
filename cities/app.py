from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/ville/<nom>")
def infos_ville(nom):
    try:
        # Correction du port 8080 -> 5000
        time_resp = requests.get(f"http://times-app:5000/time/{nom}", timeout=3)
        
        if time_resp.status_code != 200:
            return jsonify(time_resp.json()), 404

        time_data = time_resp.json()
        
        return jsonify({
            "ville": time_data["ville"],
            "pays": "Maroc",
            "continent": "Afrique",
            "description": f"{time_data['ville']} est une ville marocaine.",
            "heure_locale": time_data["heure"]
        })
    
    except requests.exceptions.ConnectionError:
        return jsonify({"erreur": "Service times indisponible"}), 503
    except KeyError as e:
        return jsonify({"erreur": f"Champ manquant: {str(e)}"}), 500
