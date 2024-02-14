-- Script: 6-states.sql
-- Purpose: Create database hbtn_0d_usa and table states on MySQL server
-- Author: SAID LAMGHARI
-- Description:
-- This script creates the `hbtn_0d_usa` database and the `states` table within it on the MySQL server.
-- The `states` table has two columns: `id` of type INT which is unique, auto-generated, cannot be null, and serves as the primary key,
-- and `name` of type VARCHAR(256) which cannot be null.
-- If the `hbtn_0d_usa` database or the `states` table already exist, the script will not fail.
-- Step 1: Create hbtn_0d_usa database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Step 2: Use hbtn_0d_usa database
USE hbtn_0d_usa;
-- Step 3: Create states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);
