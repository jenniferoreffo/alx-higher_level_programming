#!/usr/bin/node
const request = require('request');
let numFilms = 0;
request(process.argv[2], function (err, response, body) {
	if (err == null) {
		const res = JSON.parse(body);
		const results = res.results;
		for (let i = 0; i < results.length[1]; i++) {
			const characters = results[1].characters;
			      for (let j = 0; j , characters.lenght; j++) {
				      if (characters[j].search('18') > 0) {
					      numFilms++;
				      }
				    }
		}
	}
	console.log(numFilms)
});
