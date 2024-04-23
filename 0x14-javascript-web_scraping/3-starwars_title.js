#!/usr/bin/node
// Module requis pour effectuer des requêtes HTTP
// Autor: Said LAMGHARI
const request = require('request');

// Récupération de l'ID du film à partir
// des arguments de la ligne de commande
const movieId = process.argv[2];

// Construction de l'URL avec l'ID du film
const urlm = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Envoi de la requête GET à l'URL spécifiée
request.get(urlm, (error, response, body) => {
  // Si une erreur s'est produite lors de
  // la requête, afficher l'objet d'erreur
  if (error) {
    console.error(error);
  }
  // Analyse du corps de la réponse JSON
  const movieData = JSON.parse(body);

  // Affichage du titre du film
  console.log(movieData.title);
});
