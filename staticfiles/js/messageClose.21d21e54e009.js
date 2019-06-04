/*

This script allows the messages passed through from Django to the frontend
to be closed when the user clicks the 'x' icon

*/

$(document).ready(function() {
    $('#message-close-btn').click(function() {
        $('.django-messages').slideUp(200);
    })
})