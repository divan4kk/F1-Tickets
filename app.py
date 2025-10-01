from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

races = [
    {"id": 1, "name": "Australian Grand Prix", "date": "16. März 2025", "location": "Melbourne", "image": "australia.jpg"},
    {"id": 2, "name": "Saudi Arabian Grand Prix", "date": "23. März 2025", "location": "Jeddah", "image": "saudi.jpg"},
    {"id": 3, "name": "Japanese Grand Prix", "date": "6. April 2025", "location": "Suzuka", "image": "japan.jpg"},
    {"id": 4, "name": "Chinese Grand Prix", "date": "20. April 2025", "location": "Shanghai", "image": "china.jpg"},
    {"id": 5, "name": "Miami Grand Prix", "date": "4. Mai 2025", "location": "Miami", "image": "miami.jpg"},
    {"id": 6, "name": "Emilia Romagna Grand Prix", "date": "18. Mai 2025", "location": "Imola", "image": "imola.jpg"},
    {"id": 7, "name": "Monaco Grand Prix", "date": "25. Mai 2025", "location": "Monaco", "image": "monaco.jpg"},
    {"id": 8, "name": "Spanish Grand Prix", "date": "1. Juni 2025", "location": "Barcelona", "image": "spain.jpg"},
    {"id": 9, "name": "Canadian Grand Prix", "date": "15. Juni 2025", "location": "Montreal", "image": "canada.jpg"},
    {"id": 10, "name": "Austrian Grand Prix", "date": "29. Juni 2025", "location": "Spielberg", "image": "austria.jpg"},
    {"id": 11, "name": "British Grand Prix", "date": "6. Juli 2025", "location": "Silverstone", "image": "uk.jpg"},
    {"id": 12, "name": "Hungarian Grand Prix", "date": "20. Juli 2025", "location": "Budapest", "image": "hungary.jpg"},
    {"id": 13, "name": "Belgian Grand Prix", "date": "27. Juli 2025", "location": "Spa", "image": "belgium.jpg"},
    {"id": 14, "name": "Dutch Grand Prix", "date": "31. August 2025", "location": "Zandvoort", "image": "netherlands.jpg"},
    {"id": 15, "name": "Italian Grand Prix", "date": "7. September 2025", "location": "Monza", "image": "italy.jpg"},
    {"id": 16, "name": "Azerbaijan Grand Prix", "date": "21. September 2025", "location": "Baku", "image": "azerbaijan.jpg"},
    {"id": 17, "name": "Singapore Grand Prix", "date": "5. Oktober 2025", "location": "Singapore", "image": "singapore.jpg"},
    {"id": 18, "name": "United States Grand Prix", "date": "19. Oktober 2025", "location": "Austin", "image": "usa.jpg"},
    {"id": 19, "name": "Mexico City Grand Prix", "date": "26. Oktober 2025", "location": "Mexico City", "image": "mexico.jpg"},
    {"id": 20, "name": "São Paulo Grand Prix", "date": "9. November 2025", "location": "São Paulo", "image": "brazil.jpg"},
    {"id": 21, "name": "Las Vegas Grand Prix", "date": "22. November 2025", "location": "Las Vegas", "image": "vegas.jpg"},
    {"id": 22, "name": "Qatar Grand Prix", "date": "30. November 2025", "location": "Lusail", "image": "qatar.jpg"},
    {"id": 23, "name": "Abu Dhabi Grand Prix", "date": "7. Dezember 2025", "location": "Yas Marina", "image": "abu_dhabi.jpg"},
]

@app.route("/")
def index():
    return render_template("index.html", races=races)

@app.route("/buy/<int:race_id>", methods=["GET", "POST"])
def buy_ticket(race_id):
    race = next((r for r in races if r["id"] == race_id), None)
    if not race:
        flash("Rennen nicht gefunden!")
        return redirect(url_for("index"))
    
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        quantity = request.form.get("quantity")
        flash(f"Tickets für {race['name']} erfolgreich bestellt! ({quantity} Stück für {name})")
        return redirect(url_for("index"))

    return render_template("buy.html", race=race)

if __name__ == "__main__":
    app.run(debug=True)
