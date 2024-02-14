-- Script: 9-cities_by_state_join.sql
-- Purpose: List all cities with their corresponding state names in the hbtn_0d_usa database
-- Author: SAID LAMGHARI
-- Description:
-- This script lists all the cities contained in the hbtn_0d_usa database.
-- It uses a single SELECT statement to join the cities and states tables,
-- and retrieves the cities.id, cities.name, and states.name columns.
-- The results are sorted in ascending order by cities.id.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
