-- Script: 11-best_score.sql
-- Description: A script to list all records with a score >= 10 from the 'second_table' in the 'hbtn_0c_0' database, ordered by score (top first), and displaying both the score and the name.
-- Author: SAID LAMGHARI
-- Retrieve the records with score >= 10 from 'second_table' and order by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
