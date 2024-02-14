-- Script: 102-rating_shows.sql
-- Description: Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Results are sorted in descending order by the rating.
-- Usage: cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
-- Author: SAID LAMGHARI

SELECT t.title, SUM(r.rate) AS rating
FROM tv_shows AS t
INNER JOIN tv_show_ratings AS r ON t.id = r.show_id
GROUP BY t.title
ORDER BY rating DESC;
