$(document).ready(function() {


   
    $(".floated").toggle( $("#is_floated").is(":checked"));
    $("#is_floated").click(function() {
        if($(this).is(":checked")) {
            $(".floated").show(300);
        } else {
            $(".floated").hide(200);
        }
    });




    $(".floated").toggle(
        $("#is_floated").prop("checked") // For checked attribute it returns true/false;
                                            // Return value changes with checkbox state
    );


});