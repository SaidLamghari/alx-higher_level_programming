-- Script: 101-avg_temperatures.sql
-- Description: A script to display the average temperature (in Fahrenheit) by city, ordered by temperature in descending order.
-- Author: SAID LAMGHARI
-- Display the average temperature by city
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
