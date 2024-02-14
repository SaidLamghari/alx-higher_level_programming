-- Script: 10-genre_id_by_show.sql
-- Purpose: List all shows with linked genres in the hbtn_0d_tvshows database
-- Author: SAID LAMGHARI
-- Description:
-- This script lists all the shows in the hbtn_0d_tvshows database that have at least one genre linked.
-- It uses a single SELECT statement to join the tv_shows and tv_show_genres tables,
-- and retrieves the tv_shows.title and tv_show_genres.genre_id columns.
-- The results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
USE `hbtn_0d_tvshows`;
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
