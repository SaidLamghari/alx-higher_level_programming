-- Script: 100-not_my_genres.sql
-- Description: This script retrieves all genres that are not linked to the show "Dexter" from the hbtn_0d_tvshows database.
       -- It lists the genre names that are not associated with the show "Dexter" and sorts them in ascending order.
-- Author: SAID LAMGHARI

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    WHERE show_id = (
        SELECT id
        FROM tv_shows
        WHERE title = 'Dexter'
    )
)
ORDER BY tv_genres.name ASC;
