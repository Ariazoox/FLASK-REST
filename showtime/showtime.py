from flask import Flask, render_template, request, jsonify, make_response
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3202
HOST = 'localhost'

with open('{}/databases/times.json'.format("."), "r") as jsf:
   schedule = json.load(jsf)["schedule"]

# Point d'entrée renvoyant à la page d'accueil "Welcome to the Showtime service!"
@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the Showtime service!</h1>"

# Point d'entrée affichant l'intégralité des horaires de notre fichier times.json
@app.route("/showtimes", methods=['GET'])
def get_schedule():
    # Renvoie les horaires
    res = make_response(jsonify(schedule), 200)
    return res

# Point d'entrée permettant de récupérer les films prévus à partir de la date donnée en paramètre
@app.route("/showmovies/<date>", methods=['GET'])
def get_movies_by_date(date):
    # Boucle parcourant les horaires
    for showtime in schedule:
        # Vérification de l'existence de la date dans le fichier times.json
        if str(showtime["date"]) == str(date):
            res = make_response(jsonify(showtime), 200)
            # Renvoie les films pour une date donnée en paramètre
            return res
    # Message d'erreur si la date n'existe pas
    return make_response(jsonify({"error": "Date not found"}), 400)

if __name__ == "__main__":
   print("Server running on port %s"%(PORT))
   app.run(host=HOST, port=PORT)
