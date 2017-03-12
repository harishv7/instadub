$(document).keypress(function(e) {
    if(e.which === 13) {
        // alert("enter pressed");
        $("#thumbnail_logo").fadeIn("slow", function() {
            console.log("done");
        });
    }
});