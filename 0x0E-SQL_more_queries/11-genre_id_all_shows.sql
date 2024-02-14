-- Script: 11-genre_id_all_shows.sql
-- Purpose: List all shows with their genres (including NULL) in the hbtn_0d_tvshows database
-- Author: SAID LAMGHARI
-- Description:
-- This script lists all the shows in the hbtn_0d_tvshows database, along with their genres.
-- It uses a single SELECT statement to perform a LEFT JOIN between the tv_shows and tv_show_genres tables,
-- based on the tv_shows.id and tv_show_genres.show_id columns.
-- It retrieves the tv_shows.title and tv_show_genres.genre_id columns.
-- The results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
