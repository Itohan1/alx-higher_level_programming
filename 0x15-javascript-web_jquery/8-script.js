$(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (body) {
    for (const i of body.results) {
      const listitem = $('<li></li>');
      listitem.text(i.title);
      $('UL#list_movies').append(listitem);
    }
  });
});
