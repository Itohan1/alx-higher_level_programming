$(document).ready(function () {
  function fetchTranslation (language) {
    if (language) {
      $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + language, function (body) {
        const newitem = body.hello + '(in + ' + language + ')';
        $('DIV#hello').text(newitem);
      });
    } else {
      alert('Please enter code');
    }
  }
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    fetchTranslation(language);
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      const language = $(this).val();
      fetchTranslation(language);
    }
  });
});
