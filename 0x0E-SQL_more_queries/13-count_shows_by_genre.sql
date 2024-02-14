-- Script: 13-count_shows_by_genre.sql
-- Purpose: List all genres from hbtn_0d_tvshows and display the number of shows linked to each
-- Author: SAID LAMGHARI
-- Description:
-- This script lists all the genres from the hbtn_0d_tvshows database and displays the number of shows linked to each genre.
-- It uses a single SELECT statement to perform an INNER JOIN between the tv_shows and tv_show_genres tables,
-- based on the tv_shows.id and tv_show_genres.show_id columns.
-- It retrieves the genre names from the tv_show_genres table and counts the number of shows for each genre.
-- The results are grouped by genre and sorted in descending order by the number of shows linked.
SELECT tv_show_genres.genre AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_show_genres.genre
ORDER BY number_of_shows DESC;
