-- Script: 100-move_to_utf8.sql
-- Author: SAID LAMGHARI
-- Step 3: Convert the field to UTF8

-- Create database
DROP DATABASE IF EXISTS hbtn_0c_0;
CREATE DATABASE IF NOT EXISTS hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;

-- Create table
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    score INT
);
