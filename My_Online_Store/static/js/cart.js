if(localStorage.getItem('cart') == null)
{
	var cart={};
}
else{
	cart= JSON.parse(localStorage.getItem('cart'));
}

$( document ).ready(function() {

    function cartLength(obj) {
        var count = 0;
        for ( var key in obj){
            count += obj[key].quantity
        }
        return count;
    }
    //javascript
    // document.getElementById("cart-items").innerHTML = cartLength(JSON.parse(localStorage.getItem('cart')));
    // jquery
    $('#cart-items').html(cartLength(JSON.parse(localStorage.getItem('cart'))));
    // jquery
    $('.add-to-cart').click(function(){
		console.log(this.dataset.price);
        var idstr= this.dataset.product.toString();
		// the cart attributes(quantity) is being updated
        if(cart[idstr]!= undefined) {

			quantity = cart[idstr].quantity
            cart[idstr].quantity =  quantity + 1;
        }
        else {
			// cart being inititlzied
            cart[idstr] = {quantity: 1,name: this.dataset.name,price: this.dataset.price,category: this.dataset.category,image:this.dataset.image };
        }
        console.log(cart)
        localStorage.setItem('cart', JSON.stringify(cart));
        $('#cart-items').html(cartLength(cart));
    });
});


$( document ).ready(function() {

	var html = "<tr><th>Image</th><th>Name</th><th>Price</th><th>Quantity</th><th>Category</th></tr>"
	for (product_id in cart ) {
        html += "<tr>";
		html += "<td><img src="+ cart[product_id].image+" width=50 height=50 class='product'  alt='My image'></td>"
        html += "<td>"+ cart[product_id].name+"</td>"
        html += "<td>"+ cart[product_id].price+"</td>"
        html += "<td>"+ cart[product_id].quantity+"</td>"
        html += "<td>"+ cart[product_id].category+"</td>"
        html += "<td><button class='btn remove-from-cart' data-id='"+product_id+"'><i class='fa fa-trash'></i></button></td>"
        html += "</tr>";

	}
    html += "<tr><td colspan='5'></td><td> <b>Total:</b> <span id='total-amount'> "+calculate_total()+"</span></td></tr>"
	$('#display-cart').html(html)
    $('.remove-from-cart').click(function(){
        if(cart[this.dataset.id].quantity === 1){
            delete cart[this.dataset.id]
        }else{
            cart[this.dataset.id].quantity = cart[this.dataset.id].quantity - 1
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        // reloads the page from cache, faster but not up to date
        location.reload();
        // reloads the page from server, slower but always uptp date
        // location.reload(true);
    });

    function calculate_total(){
        var sum = 0;
        for (item in cart){
            sum += cart[item].quantity * cart[item].price
        }
        return sum;
    }

});