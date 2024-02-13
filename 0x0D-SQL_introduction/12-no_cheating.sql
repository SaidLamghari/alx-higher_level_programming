-- Script: 12-no_cheating.sql
-- Description: A script to update the score of Bob to 10 in the 'second_table' of the 'hbtn_0c_0' database, without using Bob's id value, and only relying on the name field.
-- Author: SAID LAMGHARI
-- Update the score of Bob to 10
UPDATE second_table SET score = 10 WHERE name = 'Bob';
