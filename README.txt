Réalisations dans le TP FLASK, REST et OpenAPI :

Création de plusieurs points d'entrée commentés dans le service Movie permettant la réalisation de différentes actions (Ajouts, Suppressions, Mises à jour, Affichage) à l'aide de plusieurs méthodes (GET, POST, PUT, DELETE), le tout en manipulant les données présentes dans le fichier "movies.json" faisant office de base de données.

Création des points d'entrée commentés, cette fois-ci pour le service Showtime, qui serviront à obtenir le programme des films prévus pour une date renseignée, le tout en utilisant les données du fichier "times.json" cette fois-ci.

Création des points d'entrée commentés pour le service Booking ayant pour objectif d'afficher les réservations des films des utilisateurs, d'afficher les réservations d'un seul utilisateur, et d'ajouter, pour un utilisateur donné, une réservation pour un film à une certaine date fixée.

Création des points d'entrée commentés pour le service User afin de pouvoir afficher les utilisateurs du fichier "users.json" ou un seul utilisateur grâce à son ID donné en paramètre. Dans le service User, le dernier point d'entrée permet d'appeler à la fois le service Booking et Movie pour pouvoir afficher toutes les réservations d'un seul utilisateur donné.

Instructions pour lancer le code :

Installer PyCharm (version 2023.1.3 de préférence).
Installer Postman.
Télécharger le contenu du dépôt git suivant : https://github.com/Ariazoox/FLASK-REST.git
Extraire le dossier "FLASK-REST" sur votre bureau ou dans n'importe quel dossier.
Lancer PyCharm, sélectionner "Open", puis ouvrir le dossier "FLASK-REST".
Vous recevrez un message automatique de PyCharm pour installer un interprète Python ; cliquez sur "Install".
Vous recevrez ensuite un autre message pour installer les requirements, donc une fois de plus, cliquez sur "Install". Sinon, ouvrez le "Terminal" en bas, puis collez la commande suivante : pip install -r requirements.txt.
Vous pourrez ensuite lancer chaque service en appuyant sur "Run" en haut à droite.
Cliquez sur le lien affiché dans la console en bas à gauche, puis copiez l'adresse du lien.
Lancez Postman, appuyez sur "New", puis sur "HTTP", collez le lien dans la barre qui s'affichera.
Complétez votre lien après le "/" et sélectionnez la bonne méthode selon le point d'entrée que vous voulez tester. Exemple : pour @app.route("/movies/<movieid>", methods=['GET']), sélectionnez la méthode "GET" dans Postman, et le lien sera : "http://localhost:3200/movies/720d006c-3a57-4b6a-b18f-9b713b073f3c" pour l'ID du film "The Good Dinosaur" récupéré dans le fichier "movies.json".
PS : Pour @app.route("/bookings/<userid>", methods=["POST"]) dans Booking, ajoutez dans Postman > Body > Raw : {"date":"<date>","movieid":"<movieid>"}. Pour @app.route("/moviesbytitle", methods=['GET']) dans Movie, le lien est le suivant : http://localhost:3200/moviesbytitle?title=<title>.
