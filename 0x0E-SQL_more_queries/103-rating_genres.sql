-- Script: 103-rating_genres.sql
-- Description:
-- This script retrieves the list of genres in the hbtn_0d_tvshows_rate database along with their corresponding ratings. The genres are sorted in descending order based on their rating sum.
-- Author: SAID LAMGHARI

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
