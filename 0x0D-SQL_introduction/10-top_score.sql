-- Script: 10-top_score.sql
-- Description: A script to list all records of the 'second_table' in the 'hbtn_0c_0' database, ordered by score (top first), and displaying both the score and the name.
-- Author: SAID LAMGHARI
-- Retrieve the records from 'second_table' and order by score
SELECT score, name FROM second_table ORDER BY score DESC;
