-- Script: 8-cities_of_california_subquery.sql
-- Purpose: List all cities of California in the hbtn_0d_usa database without using JOIN
-- Author: SAID LAMGHARI
-- Description:
-- This script lists all the cities of California in the hbtn_0d_usa database.
-- It uses a subquery to find the state_id of California from the states table,
-- and then selects the cities that have the corresponding state_id from the cities table.
-- The results are sorted in ascending order by cities.id.
-- Step 1: Use hbtn_0d_usa database
USE hbtn_0d_usa;
-- Step 2: List cities of California
SELECT * FROM cities
WHERE state_id = (
  SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
