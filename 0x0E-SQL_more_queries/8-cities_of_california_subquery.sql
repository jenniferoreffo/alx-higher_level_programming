-- List all cities of CA in the db `hbtn_0d_usa`
-- Results are ordered by ascendung cities.id.
SELECT 'id', 'name'
FROM 'cities'
WHERE 'state_id' IN (SELECT 'id' FROM 'states' WHERE 'name' = "California")
ORDER BY 'id';
