-- Count shows
-- script to list all genres and display number of shows linked to each
SELECT tv_genres.name AS g, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres 
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY g
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;

