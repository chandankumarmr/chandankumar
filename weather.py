
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/weather")
def weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Please enter a city name"}), 400

    try:
        # Get city coordinates
        geo_response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1},
            timeout=10
        )
        geo_response.raise_for_status()
        geo = geo_response.json()

        if not geo.get("results"):
            return jsonify({"error": "City not found"}), 404

        latitude = geo["results"][0]["latitude"]
        longitude = geo["results"][0]["longitude"]

        # Get current weather
        weather_response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m"
            },
            timeout=10
        )
        weather_response.raise_for_status()
        data = weather_response.json()

        return jsonify({
            "city": city,
            "temperature": data["current"]["temperature_2m"]
        })

    except requests.RequestException:
        return jsonify({"error": "Unable to fetch weather data"}), 502

if __name__ == "__main__":
    app.run(debug=True)
