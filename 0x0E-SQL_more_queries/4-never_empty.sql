-- Script: 4-never_empty.sql
-- Purpose: Create table id_not_null on MySQL server
-- Author: SAID LAMGHARI
-- Description:
-- This script creates the `id_not_null` table on the MySQL server.
-- The table has two columns: `id` of type INT with a default value of 1, and `name` of type VARCHAR(256).
-- If the `id_not_null` table already exists, the script will not fail.
-- Step 1: Create id_not_null table
-- The following query creates the `id_not_null` table if it doesn't exist.
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,
  name VARCHAR(256)
);
