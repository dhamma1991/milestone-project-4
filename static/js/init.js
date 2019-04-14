// (function($){
//   $(function(){

//     $('.button-collapse').sidenav();
//     $('.dropdown-button').dropdown({
//         // belowOrigin: true
//     });

//   }); // end of document ready
// })(jQuery); // end of jQuery name space

(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.dropdown-trigger').dropdown({
      coverTrigger: false
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space