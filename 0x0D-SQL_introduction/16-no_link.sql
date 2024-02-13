-- Script: 16-no_link.sql
-- Description: A script to list all records from the 'second_table' of the 'hbtn_0c_0' database, excluding rows without a name value, and sorted by descending score.
-- Author: SAID LAMGHARI
-- List all records with a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
