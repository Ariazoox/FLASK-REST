from flask import Flask, render_template, request, jsonify, make_response
import json
import sys
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3200
HOST = 'localhost'

with open('{}/databases/movies.json'.format("."), "r") as jsf:
   movies = json.load(jsf)["movies"]

# point d'entrée qui renvoie à la page d'accueil "Welcome to the Movie service!"
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>",200)

# point d'entrée pour le template
@app.route("/template", methods=['GET'])
def template():
    return make_response(render_template('index.html', body_text='This is my template for Movie service'),200)

# point d'entrée qui affiche l'intégralité des movies de notre fichier movies.json
@app.route("/json", methods=['GET'])
def get_json():
    res = make_response(jsonify(movies), 200)
    return res

# point d'entrée permettant de récupérer les informations d'un movie à partir de son id donné en paramètre
@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_byid(movieid):
    # Boucle qui parcourt les movies
    for movie in movies:
        # Vérification de l'existence de l'id donné en paramètre dans movies.json
        if str(movie["id"]) == str(movieid):
            res = make_response(jsonify(movie),200)
            return res
    # Message d'erreur si l'ID n'existe pas
    return make_response(jsonify({"error":"Movie ID not found"}),400)

# point d'entrée qui affiche un movie selon son titre donné en paramètre
@app.route("/moviesbytitle", methods=['GET'])
def get_movie_bytitle():
    json = ""
    if request.args:
        req = request.args
        # Boucle pour parcourir nos movies
        for movie in movies:
            # Vérification de l'existence du titre donné en paramètre dans movies.json
            if str(movie["title"]) == str(req["title"]):
                json = movie

    if not json:
        # Message d'erreur si le titre est inexistant
        res = make_response(jsonify({"error":"movie title not found"}),400)
    else:
        res = make_response(jsonify(json),200)
    return res

# Point d'entrée permettant de créer un movie en lui donnant un id unique
@app.route("/movies/<movieid>", methods=['POST'])
def create_movie(movieid):
    req = request.get_json()
    # Boucle pour parcourir nos movies
    for movie in movies:
        # Si l'id existe déjà dans le fichier movies.json, on renvoie un message d'erreur
        if str(movie["id"]) == str(movieid):
            return make_response(jsonify({"error":"movie ID already exists"}),409)

    movies.append(req)
    # L'id n'existe pas, alors on peut créer le film
    res = make_response(jsonify({"message":"movie added"}),200)
    return res

# point d'entrée pour mettre à jour la note (rating) d'un movie.
@app.route("/movies/<movieid>/<rate>", methods=['PUT'])
def update_movie_rating(movieid, rate):
    # Boucle pour parcourir nos movies
    for movie in movies:
        # Vérification de l'existence de l'id donné en paramètre dans movies.json
        if str(movie["id"]) == str(movieid):
            # Mise à jour du rating
            movie["rating"] = float(rate)
            res = make_response(jsonify(movie),200)
            return res
    # Message d'erreur si l'ID n'existe pas
    res = make_response(jsonify({"error":"movie ID not found"}),201)
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
            return make_response(jsonify(movie),200)

    # Message d'erreur si l'ID n'existe pas
    res = make_response(jsonify({"error":"movie ID not found"}),400)
    return res



if __name__ == "__main__":
    #p = sys.argv[1]
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)