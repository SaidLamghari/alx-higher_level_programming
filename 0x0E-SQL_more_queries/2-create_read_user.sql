-- Script: 2-create_read_user.sql
-- Purpose: Create MySQL database hbtn_0d_2 and user user_0d_2
-- Author: SAID LAMGHARI
-- Description:
-- This script creates the MySQL database `hbtn_0d_2` and the user `user_0d_2`.
-- The `user_0d_2` user has only SELECT privilege on the `hbtn_0d_2` database.
-- If the `hbtn_0d_2` database or `user_0d_2` user already exists, the script will not fail.

-- Step 1: Create hbtn_0d_2 database
-- The following query creates the `hbtn_0d_2` database if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Step 2: Create user_0d_2 user
-- The following query creates the `user_0d_2` user with the specified password.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Step 3: Grant SELECT privilege to user_0d_2
-- The following query grants only SELECT privilege to the `user_0d_2` user on the `hbtn_0d_2` database.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Step 4: Flush privileges
-- The following query flushes the privileges to apply the changes immediately.
FLUSH PRIVILEGES;
