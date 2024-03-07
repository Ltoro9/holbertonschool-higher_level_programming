-- script that lists all records with a score >= 10 ordered by score(top first) in the table second_table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;