// Autor : SAID LAMGHARI
$(document).ready(function(){
    $('INPUT#btn_translate').click(function(){
        var langCode = $('INPUT#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: langCode }, function(data){
            $('DIV#hello').text(data.hello);
        });
    });
});
