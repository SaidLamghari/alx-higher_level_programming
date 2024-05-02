// Autor : SAID LAMGHARI
$(document).ready(function(){
    function fetchTranslation() {
        var langCode = $('INPUT#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: langCode }, function(data){
            $('DIV#hello').text(data.hello);
        });
    }

    $('INPUT#btn_translate').click(fetchTranslation);

    $('INPUT#language_code').keypress(function(event){
        if (event.which === 13) {
            fetchTranslation();
        }
    });
});
