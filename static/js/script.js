$(document).ready(function(){
    /* Nav bar collpase activation */
    $('.sidenav').sidenav();
    /* Modal activation */
    $('.modal').modal();
    /* requiured for dropdown menu from materialize */
    $('select').formSelect();
    $('.tooltipped').tooltip();
    /* Scrollspy for main item page from materialize */
    $('.scrollspy').scrollSpy();
    /* Media box from materialize */
    $('.materialboxed').materialbox();  
    
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

    /* Function to reopen modals if password or username is incorrect or already exists*/  
    setTimeout(function(){
        flash_message = $(".flash-message").text()        
        if(flash_message=="Incorrect Username/Password"){
            $("#login").modal("open");
            /* Provide message in modal */
            $("#login-message").text("Incorrect Username/Password!")
        }
        if(flash_message=="Username already exists!"){
            $("#register").modal("open");
            /* Provide message in modal */
            $("#register-message").text("Username already exists!")
        }
        if(flash_message=="Email already exists!"){
            $("#register").modal("open");
            /* Provide message in modal */
            $("#register-message").text("Email already exists!")
        }
    }, 3000 ); // 5 secs    
})    