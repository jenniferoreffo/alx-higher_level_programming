const $ = window.$;
$.get('ttps://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
	$('DIV#hello').text(data.hello);
});
