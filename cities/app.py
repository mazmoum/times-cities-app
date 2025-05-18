from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/ville/<nom>")
def infos_ville(nom):
    try:
        # Appel au service times
        response = requests.get(f"http://times-app:5000/time/{nom}", timeout=3)
        response.raise_for_status()
        
        time_data = response.json()
        
        return jsonify({
            "ville": time_data.get("ville", nom),
            "pays": "Maroc",
            "continent": "Afrique",
            "description": f"{nom} est une ville marocaine.",
            "heure_locale": time_data.get("heure", "N/A")
        })
    
    except requests.exceptions.RequestException as e:
        return jsonify({
            "erreur": "Service times indisponible",
            "details": str(e)
        }), 503
    except KeyError as e:
        return jsonify({
            "erreur": "Format de réponse invalide",
            "champ_manquant": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
