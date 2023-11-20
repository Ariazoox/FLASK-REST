from flask import Flask, render_template, request, jsonify, make_response
import json
import sys
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3200
HOST = 'localhost'

with open('{}/data/movies.json'.format("."), "r") as jsf:
   movies = json.load(jsf)["movies"]

# Point d'entrée renvoyant à la page d'accueil "Welcome to the Movie service!"
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>", 200)

# Point d'entrée pour le template
@app.route("/template", methods=['GET'])
def template():
    return make_response(render_template('index.html', body_text='This is my template for Movie service'), 200)

# Point d'entrée affichant l'intégralité des movies de notre fichier movies.json
@app.route("/json", methods=['GET'])
def get_json():
    # Renvoie la liste des movies
    res = make_response(jsonify(movies), 200)
    return res

# Point d'entrée permettant de récupérer les informations d'un movie à partir de son id donné en paramètre
@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_by_id(movieid):
    # Boucle parcourant les movies
    for movie in movies:
        # Vérification de l'existence de l'id donné en paramètre dans movies.json
        if str(movie["id"]) == str(movieid):
            res = make_response(jsonify(movie), 200)
            # Renvoie les informations du movie dont l'id a été donné en paramètre
            return res
    # Message d'erreur si l'ID n'existe pas
    return make_response(jsonify({"error": "Movie ID not found"}), 400)

# Point d'entrée affichant un movie selon son titre donné en paramètre
@app.route("/moviesbytitle", methods=['GET'])
def get_movie_by_title():
    json_data = ""
    if request.args:
        req = request.args
        # Boucle pour parcourir nos movies
        for movie in movies:
            # Vérification de l'existence du titre donné en paramètre dans movies.json
            if str(movie["title"]) == str(req["title"]):
                json_data = movie

    if not json_data:
        # Message d'erreur si le titre est inexistant
        res = make_response(jsonify({"error": "movie title not found"}), 400)
    else:
        # Renvoie le movie dont le titre a été donné en paramètre
        res = make_response(jsonify(json_data), 200)
    return res

# Point d'entrée permettant de créer un movie en lui donnant un id unique
@app.route("/movies/<movieid>", methods=['POST'])
def create_movie(movieid):
    req = request.get_json()
    # Boucle pour parcourir nos movies
    for movie in movies:
        # Si l'id existe déjà dans le fichier movies.json, on renvoie un message d'erreur
        if str(movie["id"]) == str(movieid):
            return make_response(jsonify({"error": "movie ID already exists"}), 409)

    movies.append(req)
    # L'id n'existe pas, alors on peut créer le film
    res = make_response(jsonify({"message": "movie added"}), 200)
    return res

# Point d'entrée pour mettre à jour la note (rating) d'un movie.
@app.route("/movies/<movieid>/<rate>", methods=['PUT'])
def update_movie_rating(movieid, rate):
    # Boucle pour parcourir nos movies
    for movie in movies:
        # Vérification de l'existence de l'id donné en paramètre dans movies.json
        if str(movie["id"]) == str(movieid):
            # Mise à jour du rating
            movie["rating"] = float(rate)
            res = make_response(jsonify(movie), 200)
            # Affiche le film mis à jour avec son rating
            return res
    # Message d'erreur si l'ID n'existe pas
    res = make_response(jsonify({"error": "movie ID not found"}), 201)
    return res

# Point d'entrée pour supprimer un movie
@app.route("/movies/<movieid>", methods=['DELETE'])
def del_movie(movieid):
    # Boucle pour parcourir nos movies
    for movie in movies:
        # Vérification de l'existence de l'id donné en paramètre dans movies.json
        if str(movie["id"]) == str(movieid):
            # Suppression du movie
            movies.remove(movie)
            return make_response(jsonify(movie), 200)

    # Message d'erreur si l'ID n'existe pas
    res = make_response(jsonify({"error": "movie ID not found"}), 400)
    return res

if __name__ == "__main__":
    # p = sys.argv[1]
    print("Server running on port %s" % (PORT))
    app.run(host=HOST, port=PORT)
