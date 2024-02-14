-- Script: 0-privileges.sql
-- Purpose: Retrieve privileges for MySQL users
-- Author: SAID LAMGHARI
-- Description:
-- This script retrieves the privileges for the MySQL users 'user_0d_1' and 'user_0d_2' on the localhost server.
-- Step 1: Select User Privileges
-- The following query selects the relevant columns from the `mysql.user` table for the specified users on the `localhost` host.
-- The columns represent various privileges such as `Grant_priv`, `Super_priv`, `Create_priv`, `Insert_priv`, `Update_priv`, `Delete_priv`, `Select_priv`, and `Drop_priv`.
SELECT User, Host, Grant_priv, Super_priv, Create_priv, Insert_priv, Update_priv, Delete_priv, Select_priv, Drop_priv
FROM mysql.user
WHERE User IN ('user_0d_1', 'user_0d_2') AND Host = 'localhost';
