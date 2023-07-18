-- display max temprature of each state
-- order by statename
SELECT state, MAX(value) AS max_temp
FROM tempratures
GROUP BY state
ORDER BY state;
