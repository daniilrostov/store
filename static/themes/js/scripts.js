$(document).ready(function(){

//	$().addcart(product);
	
});
var i = 1;
var prod = new Map();

function addcart(product) {
	
	if( prod.has(product) ) {
		n = prod.get(product);
		prod.set(product, n+1);
	} else 
		{prod.set(product, i);}
		   
document.getElementById(count).value = 9;
}

