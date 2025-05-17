from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

CITIES_TZ = {
    "rabat": "Africa/Casablanca",
    "casablanca": "Africa/Casablanca"
}

@app.route("/")
def index():
    return """
    <h1>Bienvenue sur le service d'heure par ville</h1>
    <p>Utilisez l'URL <code>/time/&lt;ville&gt;</code> pour obtenir l'heure actuelle.</p>
    <p>Exemple : <code>/time/rabat</code></p>
    """

@app.route("/time/<city>")
def get_time(city):
    city_lower = city.lower()
    if city_lower in CITIES_TZ:
        tz = pytz.timezone(CITIES_TZ[city_lower])
        now = datetime.now(tz)
        return jsonify({"ville": city.capitalize(), "heure": now.strftime("%H:%M:%S")})
    else:
        return jsonify({"erreur": f"Ville '{city}' non supportée"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

