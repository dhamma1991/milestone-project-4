(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.dropdown-trigger').dropdown({
      coverTrigger: false
    });
    $('select').formSelect();

  }); // end of document ready
})(jQuery); // end of jQuery name space