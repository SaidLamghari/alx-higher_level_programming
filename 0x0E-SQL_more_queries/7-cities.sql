-- Script: 7-cities.sql
-- Purpose: Create database hbtn_0d_usa and table cities on MySQL server
-- Author: SAID LAMGHARI
-- Description:
-- This script creates the `hbtn_0d_usa` database and the `cities` table within it on the MySQL server.
-- The `cities` table has three columns: `id` of type INT which is unique, auto-generated, cannot be null, and serves as the primary key,
-- `state_id` of type INT which cannot be null and is a foreign key that references the `id` column of the `states` table,
-- and `name` of type VARCHAR(256) which cannot be null.
-- If the `hbtn_0d_usa` database or the `cities` table already exist, the script will not fail.

-- Step 1: Create hbtn_0d_usa database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Step 2: Use hbtn_0d_usa database
USE hbtn_0d_usa;
-- Step 3: Create cities table if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCES states(id)
);
