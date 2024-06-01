$(function () {
  const element = $('header');
  const clickelement = $('DIV#toggle_header');

  $(clickelement).click(function () {
    const current = $(element).attr('class');

    if (current === 'red') {
      $(element).removeClass('red').addClass('green');
    } else if (current === 'green') {
      $(element).removeClass('green').addClass('red');
    } else {
      $(element).addClass('red');
    }
  });
});
