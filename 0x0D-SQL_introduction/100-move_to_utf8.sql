-- Script: 100-move_to_utf8.sql
-- Author: SAID LAMGHARI
-- Step 1: Convert the database to UTF8
-- Step 2: Convert the table to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CHANGE name name VARCHAR (256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
