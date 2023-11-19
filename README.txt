Réalisations dans le TP FLASK,REST et OpenAPI:

Création de plusieurs points d'entrée commentés dans le service Movie permettant la réalisation de différents actions (Ajouts,Suppressions,Mises à jour,Affichage) à l'aide de plusieurs méthodes (GET,POST,PUT,DELETE) le tout en manipulant les données présentes dans le fichier "movies.json" faisant office de base de données.

Création des points d'entrée commentés cette fois pour le service Showtime qui serviront à obtenir le programme des films prévus pour une date renseignée le tout en utilisant les données cette fois ci du fichier "times.json".

Création des points d'entrée commentés pour le service Booking qui auront pour objectif d'afficher les résérvations des films des utilisateurs, d'afficher les résérvations d'un seul utilisateur et d'ajouter pour un utilisateur donné, une résérvation pour un film à une certaine date fixée.

Création des points d'entrée commentés pour le service User pour pouvoir afficher les utilisateurs du fichier users.json ou un seul utilisateur grâce à son ID donné en paramètre. Dans le service User, le dernier point d'entrée permet d'appeler à la fois le service booking et movie pour pouvoir afficher toutes les résérvations d'un seul utilisateur donné.

Instructions pour pouvoir lancer le code:

- Installer PyCharm (version 2023.1.3 de préfèrence).
- Installer Postman.
- Télécharger le contenu du repository git suivant: https://github.com/Ariazoox/FLASK-REST.git
- Extraire le dossier "FLASK-REST" dans votre bureau ou dans n'importe quel dossier.
- Lancer PyCharm, séléctionner "Open" puis ouvrez le dossier "FLASK-REST".
- Vous aurez un message automatique de PyCharm pour installer un intérprète Python, cliquez sur "Install".
- Vous aurez ensuite un autre message pour installer les requirements donc encore une fois, cliquez sur "Install" (sinon vous ouvre le "Terminal" en bas puis vous collez la commande suivante: pip install -r requirements.txt.
- Vous pourrez ensuite lancer chaque service en appuyant sur "Run" en haut à droite.
- Cliquez sur le lien que vous affichera la console en bas à gauche puis copiez l'adresse du lien.
- Lancez Postman > Appuyez sur "New" > HTTP > collez le lien dans la barre qui s'affichera.
- Complétez votre lien après le "/" et séléctionnez la bonne méthode selon le point d'entrée que vous voulez tester. Exemple: pour "@app.route("/movies/<movieid>", methods=['GET'])", il faut séléctionner la méthode "GET" dans Postman et le lien sera: "http://localhost:3200/movies/720d006c-3a57-4b6a-b18f-9b713b073f3c" pour l'id du film "The Good Dinosaur" récupéré dans le fichier movies.json

PS: Pour "@app.route("/bookings/<userid>", methods=["POST"])" dans booking, il faut rajouter dans Postman > Body > Raw: {"date":"<date>","movieid":"<movieid>"}
    Pour "@app.route("/moviesbytitle", methods=['GET'])" dans movie, le lien est le suivant http://localhost:3200/moviesbytitle?title=<title>
