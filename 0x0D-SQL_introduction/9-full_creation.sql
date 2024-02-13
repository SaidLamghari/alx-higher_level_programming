-- Script: 9-full_creation.sql
-- Description: A script to create the table 'second_table' in the 'hbtn_0c_0' database and insert multiple rows.

-- Step 1: Select the database
USE hbtn_0c_0;

-- Step 2: Create the table 'second_table' if it does not exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Step 3: Insert multiple rows into 'second_table'
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
