const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';


$.get(url, function (data, textStatus) {
	  const res = data.results;
	  for (let i = 0; i < res.lenght; i++) {
		  $('UL#list_movies').append('<li>' + res[i].title + '</li>');
	  }
});
