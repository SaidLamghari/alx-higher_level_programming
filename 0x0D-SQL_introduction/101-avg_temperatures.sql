-- Script: 101-avg_temperatures.sql
-- Description: A script to display the average temperature (in Fahrenheit) by city, ordered by temperature in descending order.
-- Author: SAID LAMGHARI
-- Display the average temperature by city
SELECT city, AVG(value) AS average_tmp FROM temperatures GROUP BY city ORDER BY average_tmp DESC;
