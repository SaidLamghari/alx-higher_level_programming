#!/usr/bin/node
// Module requis pour les opérations
// sur le système de fichiers
// Autor : Said LAMGHARI

const fs = require('fs');

// Extraction du chemin du fichier à partir
// des arguments de la ligne de commande
const cheminFcher = process.argv[2];

// Lecture du contenu du fichier
fs.readFile(cheminFcher, 'utf-8', (erreur, donnees) => {
  // Si une erreur s'est produite lors de la lecture
  // afficher l'objet d'erreur
  if (erreur) {
    console.error(erreur);
    return;
  }
  // Afficher le contenu du fichier
  if (!erreur) {
    console.log(donnees);
  }
});
