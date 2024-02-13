-- Script: 103-max_state.sql
-- Description: A script to display the maximum temperature of each state, ordered by state name.
-- Author: SAID LAMGHARI
-- Display the maximum temperature of each state
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
