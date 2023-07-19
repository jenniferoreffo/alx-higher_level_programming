-- Lists all cities in thr db `hbtn_0d_usa`
-- Records are stored in order of ascending cities.id
SELECT c.'id', c.'name', s.'name'
From 'cities' AS c 
	INNER JOIN 'states' AS s 
	ON c.'state_id' = s.'id'
ORDER BY C.'id';
