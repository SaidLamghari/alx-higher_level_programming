-- Script: 3-force_name.sql
-- Purpose: Create table force_name on MySQL server
-- Author: SAID LAMGHARI
-- Description:
-- This script creates the `force_name` table on the MySQL server.
-- The table has two columns: `id` of type INT and `name` of type VARCHAR(256) which cannot be null.
-- If the `force_name` table already exists, the script will not fail.
-- Step 1: Create force_name table
-- The following query creates the `force_name` table if it doesn't exist.
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
