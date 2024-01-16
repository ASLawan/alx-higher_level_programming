-- list records
-- script to list all records that have name value
SELECT score, name 
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
