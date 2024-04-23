#!/usr/bin/node
// Module requis pour effectuer des requêtes HTTP
// Autor: Said LAMGHARI
const request = require('request');

// Récupération de l'URL à partir
// des arguments de la ligne de commande
const urlsite = process.argv[2];

// Envoi de la requête GET à l'URL spécifiée
request.get(urlsite, (erreur, reponse) => {
  // Si une erreur s'est produite lors de la requête, afficher l'objet d'erreur
  if (erreur) {
    console.error(erreur);
    return;
  }
  // Afficher le code de statut de la réponse
  if (!erreur) {
    console.log(`code: ${reponse.statusCode}`);
  }
});
