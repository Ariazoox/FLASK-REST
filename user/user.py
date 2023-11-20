from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3203
HOST = 'localhost'

with open('{}/databases/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]
   print(users)


# point d'entrée qui renvoie à la page d'accueil "Welcome to the User service!"
@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

# point d'entrée qui affiche l'intégralité des utilisateurs de notre fichier users.json
@app.route("/users", methods=['GET'])
def get_json():
    res = make_response(jsonify(users), 200)
    # Renvoie la liste des users
    return res

# point d'entrée pour afficher un utilisateur selon son ID
@app.route("/users/<userid>", methods=['GET'])
def get_user_byid(userid):
    # Boucle qui parcourt nos users
    for user in users:
        # Vérification de la correspondance des ID
        if str(user["id"]) == str(userid):
            res = make_response(jsonify(user),200)
            # Renvoie le user avec l'ID renseigné
            return res
    # Message d'erreur au cas où l'ID serait inexistant
    return make_response(jsonify({"error":"User ID not found"}),400)

# Point d'accès qui affiche pour un utilisateur donné, ses résérvations.
@app.route("/users/<userid>/bookings", methods=["GET"])
def get_user_bookings(userid):
    # requête pour appeler le service booking par le biais de son API REST
    res = requests.get("http://localhost:3201/bookings/{}".format(userid))
    booking = res.json()
    # Boucle qui parcourt les dates dans nos bookings
    for date_item in booking["dates"]:
        mapped_movies = []
        # Boucle qui parcourt les movies
        for movie_id in date_item["movies"]:
            # requête pour appeler le service movie par le biais de son API REST
            res = requests.get("http://localhost:3200/movies/{}".format(movie_id))
            movie = res.json()
            moviedirector= movie["director"]

            mapped_movies.append({"director" : moviedirector})
        date_item["movies"] = mapped_movies
    # Renvoie les résérvations de l'utilisateur dont l'ID a été renseigné
    return make_response(jsonify(booking), res.status_code)

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
