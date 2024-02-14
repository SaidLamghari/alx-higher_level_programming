-- Script: 1-create_user.sql
-- Purpose: Create MySQL server user user_0d_1
-- Author: SAID LAMGHARI
-- Description:
-- This script creates the MySQL server user `user_0d_1` with all privileges and sets the password to `user_0d_1_pwd`.
-- If the `user_0d_1` user already exists, the script will not fail.
-- Step 1: Create user_0d_1
-- The following query creates the user_0d_1 user with the specified password and all privileges on the MySQL server.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Step 2: Grant all privileges to user_0d_1
-- The following query grants all privileges to the user_0d_1 user on all databases and tables.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Step 3: Flush privileges
-- The following query flushes the privileges to apply the changes immediately.
FLUSH PRIVILEGES;
