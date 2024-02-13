-- Usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database_name>
-- Author: SAID LAMGHARI
-- Create the first_table if it doesn't exist
-- Date: February 13, 2024
CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(256)
);
