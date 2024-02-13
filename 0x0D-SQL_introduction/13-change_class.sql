-- Script: 13-change_class.sql
-- Description: A script to remove all records with a score <= 5 from the 'second_table' of the 'hbtn_0c_0' database.
-- Author: SAID LAMGHARI
-- Delete the records with score <= 5
DELETE FROM second_table WHERE score <= 5;
