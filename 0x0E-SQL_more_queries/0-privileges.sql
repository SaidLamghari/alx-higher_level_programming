-- Script: 0-privileges.sql
-- Purpose: Retrieve privileges for MySQL users
-- Author: SAID LAMGHARI
-- Description:
-- This script retrieves the privileges for the MySQL users 'user_0d_1' and 'user_0d_2' on the localhost server.
SHOW GRANTS
	FOR user_0d_1@localhost;

SHOW GRANTS
	FOR user_0d_2@localhost;
