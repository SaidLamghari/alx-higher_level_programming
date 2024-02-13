-- Script: 9-full_creation.sql
-- Description: A script to create the table 'second_table' in the 'hbtn_0c_0' database and insert multiple rows.
-- Author: SAID LAMGHARI
-- Insert multiple rows into 'second_table'
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
