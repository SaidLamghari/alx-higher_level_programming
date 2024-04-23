#!/usr/bin/node
// Module requis pour effectuer des requêtes HTTP
// Autor: Said LAMGHARI
const request = require('request');

// Récupération de l'URL de l'API Star Wars à
// partir des arguments de la ligne de commande
const apiLnk = process.argv[2];

// ID du personnage "Wedge Antilles"
const chrctrId = '18';

// Envoi de la requête GET à l'URL spécifiée
request.get(apiLnk, function (erreur, response, bd) {
  // Si une erreur s'est produite lors
  // de la requête, afficher l'objet d'erreur
  if (erreur) {
    console.error(erreur);
    return;
  }

  // Analyse du corps de la réponse JSON
  const flmsData = JSON.parse(bd).results;

  // Initialisation du compteur de films
  // où le personnage "Wedge Antilles" est présent
  let cnt = 0;

  // Parcourir chaque film pour vérifier la présence du personnage
  flmsData.forEach((film) => {
    // Vérifier si le personnage "Wedge Antilles"
    // est présent dans la liste des personnages du film
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${chrctrId}/`)) {
      cnt++;
    }
  });

  // Affichage du nombre de films où
  // le personnage "Wedge Antilles" est présent
  console.log(cnt);
});
