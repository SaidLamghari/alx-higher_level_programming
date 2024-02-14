-- Script: 101-not_a_comedy.sql
-- Description: This script retrieves all shows from the hbtn_0d_tvshows database that do not have the genre "Comedy".
        -- It lists the titles of the shows that are not categorized as Comedy and sorts them in ascending order.
-- Author: SAID LAMGHARI

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_show_genres.show_id
    FROM tv_show_genres
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy')
ORDER BY tv_shows.title ASC;
