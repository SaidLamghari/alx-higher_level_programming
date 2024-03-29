-- Script: 102-top_city.sql
-- Description: A script to display the top 3 cities' temperatures during July and August, ordered by temperature in descending order.
-- SAID LAMGHARI
-- Display the top 3 cities' temperatures during July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE MONTH IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
