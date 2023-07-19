-- List all genres of thr show Dexter in the db hbtn_0d_tvshows
-- Records are ordered by ascending genre name
SELECT g.'name'
  FROM 'tv_genres' AS g
	INNER JOIN 'tv_show_genres' AS s
	 ON g.'id' = s.'genre_id'
	
	INNER JOIN 'tb_shows' AS t
	 ON t.'id' = s.'shows_id'
	WHERE t.'title' = "Dexter"
ORDER BY g.'name';
