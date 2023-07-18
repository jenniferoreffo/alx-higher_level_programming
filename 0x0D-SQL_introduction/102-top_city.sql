-- displays the average temp of 3 cities 
-- during July and August 
-- order by temperature desc
SELECT city, AVG(value) AS avg_temp
FROM tempretures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

