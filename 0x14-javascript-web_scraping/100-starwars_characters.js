#!/usr/bin/node
// Module requis pour effectuer des requêtes HTTP
// Autor : Said LAMGHARI
const request = require('request');

// Récupération de l'ID du film à partir
// des arguments de la ligne de commande
const mvieId = process.argv[2];

// URL de l'API Star Wars pour récupérer les détails du film
const apiLnk = `https://swapi-api.alx-tools.com/api/films/${mvieId}/`;

// Envoi de la requête GET à l'URL spécifiée
request.get(apiLnk, (error, response, body) => {
  // Si une erreur s'est produite lors
  // de la requête, afficher l'objet d'erreur
  if (error) {
    console.error(error);
  }

  // Analyse du corps de la réponse JSON
  const movieData = JSON.parse(body);

  // Récupération des URL des personnages présents dans le film
  const charactersUrls = movieData.characters;

  // Fonction pour récupérer les noms des personnages à partir de leurs URL
  const getChrcterNmes = async (urls) => {
    // Tableau pour stocker les noms des personnages
    const characterNom = [];

    // Parcourir chaque URL de personnage
    for (const lnk of urls) {
      // Envoi de la requête GET à l'URL du personnage
      await new Promise(resolve => {
        request.get(lnk, (error, response, body) => {
          // Si une erreur s'est produite lors
          // de la requête, afficher l'objet d'erreur
          if (error) {
            console.error(error);
            resolve();
            return;
          }

          // Analyse du corps de la réponse JSON
          const characterDonne = JSON.parse(body);

          // Ajout du nom du personnage au tableau
          characterNom.push(characterDonne.name);

          // Résolution de la promesse pour indiquer la fin de la requête
          resolve();
        });
      });
    }

    // Affichage des noms des personnages, un par ligne
    characterNom.forEach(name => console.log(name));
  };

  // Appel de la fonction pour récupérer les noms des personnages à partir de leurs URL
  getChrcterNmes(charactersUrls);
});
