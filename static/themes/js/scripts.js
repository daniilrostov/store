$(document).ready(function(){
	//var i = 0;
	//var btn = document.getElementsByClassName('caption');
	//var product = $('#form_buying_product');
	//var product_name = product.data("name");
	//console.log(btn);
	//$('#form_buying_product').click(function(e){
	//	i=i+1
		
	//	console.log(i);
	//})
	
});
var i = 0;
var prod = [];

function addcart(product) {
	
	var first = prod.find(myFunction);
	function myFunction(value, index, array) {
		return value == product;
	}
	
	if (first) {
		alert('Добавлено ' + product);			
	} else { console.log('Добавляется ' + product);
	prod.push(product);
	i = i + 1;}
		   
console.log(prod+' '+i);
}

