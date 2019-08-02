$(document).ready(function(){
	var form = $('#form_buying_product');
	form.on('submit', function(e){
		e.preventDefault();
		
		var nmb = $('#number').val();
		
		var submit_btn = $('#submit_btn');
		var product = submit_btn.data("product_id");
		if (nmb == 0) {
			alert("Укажите количество");
		} else {console.log(product+' '+nmb+' штуки.');}
		
	})
});




var i = 1;
var sum = 0
var prod = new Map();
function addcart(product) {
	
	if( prod.has(product) ) {
		var n = prod.get(product);
		
		prod.set(product, n+1);
	} else 
		{prod.set(product, i);}
		   
prod.forEach(function(value,key) {
	console.log('Количество = ' + key +' ' +value+ ' штук');   
	//sum += +value;
	//console.log(value);
});
};

