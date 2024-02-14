-- Script: 100-move_to_utf8.sql
-- Description: A script to convert the hbtn_0c_0 database, the first_table table, and the name field in the first_table to UTF8 (utf8mb4, collate utf8mb4_unicode_ci).
-- Author: SAID LAMGHARI
-- Step 1: Convert the database to UTF8
-- Step 2: Convert the table to UTF8
-- Step 3: Convert the field to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
