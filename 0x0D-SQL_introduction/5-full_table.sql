-- Usage: cat 5-full_table.sql | mysql -hlocalhost -uroot -p <database_name>
-- Author: SAID LAMGHARI
-- Print the full description of the first_table
-- Date: February 13, 2024
SELECT CONCAT('Table\tCreate Table\n', table_name, '\t', create_statement)
FROM information_schema.tables
WHERE table_schema = '<database_name>' AND table_name = 'first_table';
