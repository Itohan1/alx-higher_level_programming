$(document).ready(function() {
  $("INPUT#btn_translate").click(function() {
    let languageCode = $("INPUT#language_code").val();
    let input = "?lang=$" ${languageCode};
    $.getJSON("https://www.fourtonfish.com/hellosalut/hello/" + input, function(body) {
        let newitem = body;
	$("DIV#hello").text(newitem);
    });
 });
});
