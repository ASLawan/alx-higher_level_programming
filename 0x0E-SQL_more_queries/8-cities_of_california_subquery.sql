-- Display cities in california
-- Script to display cities from California
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = "California"
	);
