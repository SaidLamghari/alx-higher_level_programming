-- Script: 15-groups.sql
-- Description: A script to list the number of records with the same score in the 'second_table' of the 'hbtn_0c_0' database, sorted by the number of records in descending order.
-- Author: SAID LAMGHARI
-- List the number of records with the same score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
