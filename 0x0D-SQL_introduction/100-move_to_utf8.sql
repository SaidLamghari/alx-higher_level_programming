-- Script: 100-move_to_utf8.sql
-- Author: SAID LAMGHARI
-- Step 3: Convert the field to UTF8

-- Create a new table with the desired collation
CREATE TABLE new_table LIKE first_table;
ALTER TABLE new_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

-- Copy data from the original table to the new table
INSERT INTO new_table SELECT * FROM first_table;

-- Optionally, you can drop the original table
DROP TABLE first_table;

-- Rename the new table to the original table name
RENAME TABLE new_table TO first_table;
