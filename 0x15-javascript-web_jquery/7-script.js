$(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (movies) {
    $('DIV#character').text(movies.name);
  });
});
