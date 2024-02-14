-- Script: 15-comedy_only.sql
-- Description: This script retrieves all Comedy shows from the hbtn_0d_tvshows database.
-- It lists the titles of the Comedy shows in ascending order by the show title.
-- Author: SAID LAMGHARI

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
