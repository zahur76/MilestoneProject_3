$(document).ready(function(){
    /* Nav bar collpase activation */
    $('.sidenav').sidenav();
    /* Modal activation */
    $('.modal').modal();
    /* requiured for dropdown menu from materialize */
    $('select').formSelect();
    $('.tooltipped').tooltip();  
    
    /* Function to ensure modal does not close if fields are invalid */
    $(".submit").click(function(){
        let username_attr = $("#username").attr("class");
        let password_attr = $("#username").attr("class");        
        if(username_attr=="validate valid" || password_attr=="validate valid"){
            $(".submit").addClass("modal-close")
        }        
    })

    /* Code to provide validation for dropdown field */
    /* code source https://stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown */
    $("select[required]").css({display: "block", height: 0, padding: 0, width: 0, position: 'absolute'});

    /* Function to allow modals swap over */    
    $(".login-modal").click(function(){        
        $(".login-modal").addClass("modal-close");        
    })

    $(".register-modal").click(function(){        
        $(".register-modal").addClass("modal-close");       
    })

    /* Function to clear flash messages after 5's*/  
    setTimeout(function(){
        $(".flash-message").hide("slow");
    }, 5000 ); // 5 secs    
})


    