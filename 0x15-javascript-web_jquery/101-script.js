$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('ul li:last-child').remove();
  });
  $('DIV#clear_list').click(function () {
    $('ul li').remove();
  });
});
