$( document ).ready(function() {
    if (user === "AnonymousUser"){
        $('#user-info').hide()
    }
    console.log(cartLength())
    $('#total_items').html(cartLength());
    $('#total').html("€ "+calculateTotal());
});
