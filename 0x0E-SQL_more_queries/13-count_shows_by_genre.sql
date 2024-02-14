-- Script: 13-count_shows_by_genre.sql
-- Purpose: List all genres from hbtn_0d_tvshows and display the number of shows linked to each
-- Author: SAID LAMGHARI
-- Description:
-- This script lists all the genres from the hbtn_0d_tvshows database and displays the number of shows linked to each genre.
-- It uses a single SELECT statement to perform an INNER JOIN between the tv_shows and tv_show_genres tables,
-- based on the tv_shows.id and tv_show_genres.show_id columns.
-- It retrieves the genre names from the tv_show_genres table and counts the number of shows for each genre.
-- The results are grouped by genre and sorted in descending order by the number of shows linked.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
