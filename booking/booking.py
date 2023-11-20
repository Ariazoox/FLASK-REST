from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3201
HOST = 'localhost'

with open('{}/data/bookings.json'.format("."), "r") as jsf:
   bookings = json.load(jsf)["bookings"]

# Point d'entrée renvoyant à la page d'accueil "Welcome to the Booking service!"
@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the Booking service!</h1>"

# Point d'entrée affichant l'intégralité des réservations (bookings) de notre fichier bookings.json
@app.route("/bookings", methods=['GET'])
def get_json():
    res = make_response(jsonify(bookings), 200)
    return res

# Point d'entrée affichant la réservation d'un utilisateur à partir de son ID donné en paramètre
@app.route("/bookings/<userid>", methods=['GET'])
def get_booking_for_user(userid):
    # Boucle parcourant nos bookings
    for booking in bookings:
        # Vérification de la correspondance de l'ID donné avec les ID du fichier bookings.json
        if str(booking["userid"]) == str(userid):
            res = make_response(jsonify(booking), 200)
            # Renvoie les réservations de l'utilisateur dont on a donné l'ID en paramètre
            return res
    # Message d'erreur si les ID ne correspondent pas
    return make_response(jsonify({"error": "User ID not found"}), 400)

# Point d'entrée permettant d'ajouter une réservation pour l'utilisateur, On passe par Showtime pour vérifier la validité de la réservation demandée.
@app.route("/bookings/<userid>", methods=["POST"])
def add_booking_by_user(userid):
    data = request.get_json()
    res = requests.get("http://localhost:3202/showtimes")
    schedule = res.json()
    # Boucle parcourant les schedules
    for schedule_item in schedule:
        # Vérification de l'existence de la date de l'ID dans le fichier times.json
        if (
            schedule_item["date"] == data["date"]
            and data["movieid"] in schedule_item["movies"]
        ):
            # Boucle parcourant les bookings
            for booking in bookings:
                # Vérification de la correspondance de l'ID utilisateur, la date et l'ID
                if booking["userid"] == userid:
                    for item in booking["dates"]:
                        if item["date"] == data["date"]:
                            if data["movieid"] in item["movies"]:
                                return make_response(
                                    jsonify(
                                        # Si l'utilisateur a déjà une réservation pour ce film à cette date là, on renvoie ce message, sinon, on l'ajoute à la réservation
                                        {"error": "movie already booked by this user"}
                                    ),
                                    409,
                                )
                            item["movies"].append(data["movieid"])
                            return make_response(jsonify(booking), 200)

                    booking["dates"].append(
                        {
                            "date": data["date"],
                            "movies": [data["movieid"]],
                        }
                    )
                    return make_response(jsonify(booking), 200)
            # On considère que le user ID est valide
            bookings.append(
                {
                    "userid": userid,
                    "dates": [{"date": data["date"], "movies": [data["movieid"]]}],
                }
            )
            # On rajoute cette réservation pour l'utilisateur donné
            return make_response(jsonify(bookings[-1]), 200)

    return make_response(
        jsonify(
            {   # Dans le cas où le movie id ou la date sont inexistants, on renvoie ce message d'erreur.
                "error": "date or movie id incorrect or not provided, make sure you provide a movieid that is part of an existing date in the showtimes"
            }
        ),
        409,
    )

if __name__ == "__main__":
   print("Server running on port %s"%(PORT))
   app.run(host=HOST, port=PORT)
