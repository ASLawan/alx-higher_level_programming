-- Display data from two tables
-- script that uses join to display data about cities and states
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id;
