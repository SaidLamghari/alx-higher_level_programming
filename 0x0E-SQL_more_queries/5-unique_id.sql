-- Script: 5-unique_id.sql
-- Purpose: Create table unique_id on MySQL server
-- Author: SAID LAMGHARI
-- Description:
-- This script creates the `unique_id` table on the MySQL server.
-- The table has two columns: `id` of type INT with a default value of 1 and must be unique, and `name` of type VARCHAR(256).
-- If the `unique_id` table already exists, the script will not fail.
-- Step 1: Create unique_id table
-- The following query creates the `unique_id` table if it doesn't exist.
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);
