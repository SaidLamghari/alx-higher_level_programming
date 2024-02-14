-- Script: 16-shows_by_genre.sql
-- Description: This script retrieves all shows from the hbtn_0d_tvshows database along with their linked genres.
             -- It lists the show titles and their corresponding genre names, sorted in ascending order by the show title and genre name.
             -- If a show doesn't have a genre, it displays NULL in the genre column.
-- Author: SAID LAMGHARI

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
