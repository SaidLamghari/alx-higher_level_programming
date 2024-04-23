#!/usr/bin/node
// Module requis pour les opérations sur le système de fichiers
// Autor : Said LAMGHARI

const fs = require('fs');

// Extraction du chemin du fichier et du contenu à écrire
// à partir des arguments de la ligne de commande
const cheminFcher = process.argv[2];
const contenu = process.argv[3];

// Écriture du contenu dans le fichier spécifié
fs.writeFile(cheminFcher, contenu, 'utf-8', (erreur) => {
  // Si une erreur s'est produite lors de
  // l'écriture, afficher l'objet d'erreur
  if (erreur) {
    console.error(erreur);
    return;
  }
});
