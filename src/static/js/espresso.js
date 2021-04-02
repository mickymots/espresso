$(document).ready(function() {


   
    $(".floated").hide();
    $("#is_floated").click(function() {
        if($(this).is(":checked")) {
            $(".floated").show(300);
        } else {
            $(".floated").hide(200);
        }
    });


   

});