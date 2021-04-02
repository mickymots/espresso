$(document).ready(function() {

    // JQuery code to be added in here.

    // $('.floated').dependsOn('#is_floated');
    $(".floated").hide(100);
    $("#is_floated").click(function() {
        if($(this).is(":checked")) {
            $(".floated").show(300);
        } else {
            $(".floated").hide(200);
        }
    });


   

});