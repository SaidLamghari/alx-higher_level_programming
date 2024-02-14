-- Script: 102-rating_shows.sql
-- Description: Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Results are sorted in descending order by the rating.
-- Usage: cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
-- Author: SAID LAMGHARI

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating_sum
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id, tv_shows.title
ORDER BY rating_sum DESC;
