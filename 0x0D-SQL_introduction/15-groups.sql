-- List the number of records with the same score
-- In the table 'second_table' of the database 'hbtn_0c_0'
-- in MYSQL server 
SELECT score, COUNT('score') as number 
FROM second_table
GROUP BY score
ORDER BY score DESC;
