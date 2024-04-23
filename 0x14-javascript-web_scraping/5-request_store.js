#!/usr/bin/node
// Module requis pour effectuer des requêtes HTTP
// Autor : Said LAMGHARI
const request = require('request');
// Module requis pour effectuer des
// opérations sur le système de fichiers
const fs = require('fs');

// Récupération de l'URL à partir
// des arguments de la ligne de commande
const apLnk = process.argv[2];
// Récupération du chemin du fichier à partir
// des arguments de la ligne de commande
const cheminFcher = process.argv[3];

// Envoi de la requête GET à l'URL spécifiée
request.get(apLnk, (error, response, body) => {
  // Si une erreur s'est produite lors
  // de la requête, afficher l'objet d'erreur
  if (error) {
    console.error(error);
    return;
  }

  // Écriture du corps de la réponse dans le fichier spécifié
  fs.writeFile(cheminFcher, body, 'utf-8', (erreur) => {
    // Si une erreur s'est produite lors de l'écriture, afficher l'objet d'erreur
    if (erreur) {
      console.error(erreur);
    }
  });
});
