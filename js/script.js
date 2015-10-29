/* Just some mobile overrides. */
if ($(window).width() <= 1000) {
    $("img").remove();
    $("#mp3_player").remove();
    $("#for-mobile").html("<br><br><br><br><br><br><br><br><br><br>");
    $("p").css({'font-size': '32px'});
    $("#final-word").css({'font-size': '32px'});
}

$(window).resize(function() {
    if ($(window).width() <= 800) {
        $("img").remove();
        $("#mp3_player").remove();
        $("#for-mobile").html("<br><br><br><br><br><br><br><br><br><br>");
        $("p").css({'font-size': '32px'});
        $("#final-word").css({'font-size': '32px'});
    }
});
