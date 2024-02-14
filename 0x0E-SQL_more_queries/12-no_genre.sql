-- Script: 12-no_genre.sql
-- Purpose: List all shows without a genre linked in the hbtn_0d_tvshows database
-- Author: SAID LAMGHARI
-- Description:
-- This script lists all the shows in the hbtn_0d_tvshows database that do not have a genre linked.
-- It uses a single SELECT statement to perform a LEFT JOIN between the tv_shows and tv_show_genres tables,
-- based on the tv_shows.id and tv_show_genres.show_id columns.
-- It retrieves the tv_shows.title and tv_show_genres.genre_id columns.
-- The results are filtered to include only records where tv_show_genres.genre_id is NULL,
-- and sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
