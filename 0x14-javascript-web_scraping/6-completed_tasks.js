#!/usr/bin/node
// Module requis pour effectuer des requêtes HTTP
// Autor : Said LAMGHARI
const request = require('request');

// Récupération de l'URL de l'API à partir des arguments de la ligne de commande
const apiUrl = process.argv[2];

// Envoi de la requête GET à l'URL spécifiée
request.get(apiUrl, (error, response, body) => {
  // Si une erreur s'est produite lors de
  // la requête, afficher l'objet d'erreur
  if (error) {
    console.error(error);
  }

  // Analyse du corps de la réponse JSON
  const todos = JSON.parse(body);

  // Initialisation d'un dictionnaire pour stocker
  // le nombre de tâches complétées par utilisateur
  const NbCompletedTasksU = {};

  // Filtrer les tâches complétées
  const completedTds = todos.filter(todo => todo.completed);

  // Compter les tâches complétées par utilisateur
  completedTds.forEach((todo) => {
    // Si l'utilisateur n'existe pas encore
    // dans le dictionnaire, l'initialiser à 1
    if (!NbCompletedTasksU[todo.userId]) {
      NbCompletedTasksU[todo.userId] = 1;
    } else {
    // Sinon, incrémenter le nombre de
    // tâches complétées pour cet utilisateur
      NbCompletedTasksU[todo.userId]++;
    }
  });

  // Affichage du nombre de tâches complétées par utilisateur
  console.log(NbCompletedTasksU);
});
