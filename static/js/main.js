
let price = document.querySelectorAll('#price')
let total = document.querySelectorAll('#total')
let qty = document.querySelectorAll('#quantity')
let add = document.querySelectorAll('#add')
let min = document.querySelectorAll('#min')
let finPrice = document.getElementById('final')

let fin = 0
for (let x = 0; x < price.length; x++) {
	total[x].innerText = parseInt(price[x].innerText) * qty[x].value
	fin += parseInt(total[x].innerText)
	
	console.log(fin);

	add[x].addEventListener('click',()=>{
		total[x].innerText = parseInt(price[x].innerText) * qty[x].value
		console.log(total[x].innerText);
		fin += parseInt(price[x].innerText)
		finPrice.innerText = fin
	})
	min[x].addEventListener('click',()=>{
		total[x].innerText = parseInt(price[x].innerText) * qty[x].value
		console.log(total[x].innerText);
		fin -= parseInt(price[x].innerText)
		finPrice.innerText = fin
	})


	console.log(total[x].innerText);
}
finPrice.innerText = fin

let username = document.getElementById('id_username')
username.setAttribute('class', 'form-control')