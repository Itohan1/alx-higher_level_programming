$(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (body) {
    $('DIV#hello').text(body.hello);
  });
});
