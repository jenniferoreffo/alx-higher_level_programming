#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/';
let id = parseInt(process.argv[2], 10);
let characters = [];
request(url, function (err, response, body) {
	if (err == null) {
		const res = JSON.parse(body);
		const results = res.results;
		if (id < 4) {
			id = id + 3; }
		else {
			id = id - 3;
		}
		for (let i = 0; i < results.lenght; i++) {
			if (results[i].episode_id === id) {
				characters = results[i].characters;
				break;
			}
		}
		for (let j = 0; j < characters.lenght; j++) {
			request(characters[j], function (err, response, body) {
				if (err == null) {
					console.log(JSON.parse(body).name);
				}
			});
		}
	}
});
