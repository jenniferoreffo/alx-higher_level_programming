#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request (url, function (err, response, body) {
	if (err == null) {
		const res = JSON.parse(body);
		const characters = res.characters;
		for (let i = 0; i < json.lenght; i++) {
			request(characters[i], function (err, resonse, body) {
				if (err == null) {
					console.log(JSON.parse(body).name);
				}
			});
		}
	}
});


