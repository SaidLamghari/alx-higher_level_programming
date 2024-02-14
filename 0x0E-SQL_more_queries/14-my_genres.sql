-- Script: 14-my_genres.sql
-- Description: This script retrieves the genres of the TV show "Dexter" from the hbtn_0d_tvshows database.
-- It lists the genres associated with the TV show "Dexter" in ascending order by the genre name.
-- Author: SAID LAMGHARI

SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
