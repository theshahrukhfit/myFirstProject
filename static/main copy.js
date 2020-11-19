//Logging email from user input
/*myForm = document.querySelector('#myForm');
inputName = document.querySelector('#exampleInputEmail1');

myForm.addEventListener('submit', OnSubmit);

function OnSubmit(a) {
    a.preventDefault();

    console.log(inputName.value);
}*/

//Testing
/*
const imgHtext = () => {
    const allimg = document.querySelectorAll('.containerxyz img');
    const imgcontainer = document.querySelector('.containerxyz')

    allimg.forEach(eimg => { 
        eimg.addEventListener('mouseover', () =>
        {
            var divOverlay = document.createElement('div');
            divOverlay.innerHTML = 'Shop Now';
            divOverlay.style.backgroundColor = 'red';
            divOverlay.style.width = '300px';
            document.getElementById('imgcont').appendChild(divOverlay);
        })
        
    });
}

imgHtext(); */

//Index Container Dress on Click Shop 
// dressClass = document.querySelectorAll('.econt');
// var counter = 0;

// var cartDict = []
// //Add Item to cart function
// dressClass.forEach(_dress => _dress.addEventListener('click', () => {
//     var shopYN = confirm('Add item to cart?');
//     if (shopYN === true) {
//         productID = _dress.querySelector('.productID').innerHTML

//         cartDict.push({
//             key:   "ProductID",
//             value: productID
// });
//     }

//     else {
//         return false;
//     }
// } ));
// console.log(cartDict)

// if (window.location.pathname == "/mycart") {
// console.log(cartDict)
// console.log("yes")
//         $.ajax({
//             type: "POST",
//             url: "/mycart",
//             contentType: "application/json",
//             data: JSON.stringify(cartDict),
//             dataType: "json",
//             success: function(response) {
//                 console.log(response);
//             },
//             error: function(err) {
//                 console.log(err);
//             }
//         });
//     };

// dressClass = document.querySelectorAll('.econt');
// dressClass.forEach(_dress => _dress.addEventListener('click', () => {




// } ));


// //Get Innerhtml of the nav-dressdrpd
// cates = document.querySelectorAll('.navdrpd li')

//Getting the item on click
// $.ajax({
//     type:'POST'
// })

// $.ajax({
//     type: "POST",
//     url: "/categories",
//     contentType: "application/json",
//     data: JSON.stringify('hi'),
//     dataType: "json",
//     success: function(response) {
//         console.log(response);
//     },
//     error: function(err) {
//         console.log(err);
//     }
// });

//AJAX - Send variable to python
// $.ajax({
//     type: "POST",
//     url: "{{ url_for("get_post_json") }}",
//     contentType: "application/json",
//     data: JSON.stringify({hello: "world"}),
//     dataType: "json",
//     success: function(response) {
//         console.log(response);
//     },
//     error: function(err) {
//         console.log(err);
//     }
// });

 //Cart Quantity
//  $(document).ready(function(){
//     $('.count').prop('disabled', true);
//        $(document).on('click','.plus',function(){
//         $('.count').val(parseInt($('.count').val()) + 1 );
//         console.log($('.count').val())
//     });
//     $(document).on('click','.minus',function(){
//         $('.count').val(parseInt($('.count').val()) - 1 );
//             if ($('.count').val() == 0) {
//                 $('.count').val(1);
//             }
//         });
//  });

// plusclick = document.querySelectorAll('.plus')

// plusclick.forEach(_plus => _plus.addEventListener('click', () => {
//     value_count = Number(document.querySelector('.count').value) + 1;

    
//     console.log(value_count);
// }))




//  //Getting the value of the changed quantity
//  document.querySelectorAll('.cart_row').forEach(_row => _row.querySelectorAll('#' + _row.id + ' .minus, #' + _row.id + ' .plus').forEach(_minpls => _minpls.addEventListener('click', () => {
    
//     var input = _row.querySelector('#' + _row.id + " input");
//     var inputval = parseInt(input.value);

//     if (_minpls.className.indexOf("plus") == -1)
//     {
//         if (inputval > 1)
//         {

//             input.value = inputval - 1;
//             let total = parseFloat(_row.querySelector(".p_price").innerHTML.replace("Rs", "")) * input.value;
//             _row.querySelector(".p_total").innerHTML = numberWithCommas(total);
//             document.querySelector("#grand_total").innerHTML


//         }

//         else
//         {
//             alert("Invalid Quantity");

//         }
//     }

//     else
//     {
//         if (inputval < 12 )
//         {

//             input.value = parseInt(input.value) + 1;
//             let total = parseFloat(_row.querySelector(".p_price").innerHTML.replace("Rs", "")) * input.value;
//             _row.querySelector(".p_total").innerHTML = numberWithCommas(total)

//         }

//         else 
//         {
//             alert("Quantity limit reached. Only 12 allowed per item.");
//         }
//     }

//  })),
 
//  )

//  document.querySelectorAll('.p_total').forEach(price_row => {
//      var testv = price_row.innerHTML;
//      console.log(testv)
//  } )

//Function to add commas


// console.log(document.querySelector("#tta .classtest").innerHTML);
// console.log(document.querySelector("#test8 .classtest").innerHTML);

// var all_rowsc =  document.querySelectorAll('.cart_row');

// var grand_total = 0;

// for (let i = 0; i < all_rowsc.length; i++)
// {
//     var minplus = all_rowsc[i].querySelectorAll('.minus, .plus')

//     var input = all_rowsc[i].querySelector("input");
//     var inputval = parseInt(input.value);

//     //Plus and Minus button
//     for (let mp = 0; mp < minplus.length; mp++)
//     {  
//             console.log(minplus.length)
//         minplus[mp].addEventListener("click", () => {

//             if (minplus[mp].className.indexOf("plus") == -1)
//             {
//                 if (inputval > 1)
//                 {

//                     input.value = inputval - 1;
//                     let total = parseFloat(all_rowsc[i].querySelector(".p_price").innerHTML.replace("Rs", "")) * input.value;
//                     all_rowsc[i].querySelector(".p_total").innerHTML = numberWithCommas(total);

//                 }

//                 else
//                 {
//                     alert("Invalid Quantity, less than 1.");
//                 }
                
//             }

//             else
//             {
//                 if (inputval < 12)
//                 {
//                     input.value = parseInt(input.value) + 1;
//                     let total = parseFloat(all_rowsc[i].querySelector(".p_price").innerHTML.replace("Rs", "")) * input.value;
//                     all_rowsc[i].querySelector(".p_total").innerHTML = numberWithCommas(total)
//                 }

//                 else 
//                 {
//                     alert("Quantity limit reached. Only 12 allowed per item.");
//                 }

//             }



//         })

// }

// }


//Display Cart if there is one
displayCart()

//Index Container Dress on Click Shop 
dressClass = document.querySelectorAll('.sendID');

//Add Item to cart function
dressClass.forEach(_dress => _dress.addEventListener('click', () => {
    var shopYN = confirm('Add item to cart?');
    if (shopYN === true) {
        
        addCart()
        
        console.log(selectedSize);
        
        $.post("/mycart", { add_cart: {selectedSize: selectedSize }})
    }

    else {
        return false;
    }
})
   
 );

 //Function to display cart

 function displayCart() 
 {

    if (sessionStorage.cart_quan)
    {
        shopCounter = document.querySelector('#shopCounter');
        shopCounter.style.backgroundColor = 'red';
        shopCounter.innerHTML = sessionStorage.cart_quan;
    
    }

}

//Cart Route
var minplus = document.querySelectorAll('.minus, .plus, .cart_del');

for (let i = 0; i < minplus.length; i++)
{
    minplus[i].addEventListener("click", () => {

        let tr = minplus[i].closest("tr");
        let input = tr.querySelector("input");
        let inputval = parseInt(input.value);
        let productID = parseInt(tr.id);
        let price = parseInt(tr.querySelector(".p_price").innerHTML);

        if (minplus[i].className.indexOf("plus") != -1)
        {

            if (inputval < 12) 
            {

            input.value = inputval + 1;
            tr.querySelector(".p_total").innerHTML = price * input.value;
            grand_total();
            addCart();
        
            $.post("/mycart", { 'add_cart': productID });
            
            }
            
        }

        else if (minplus[i].className.indexOf("cart_del") != -1)
        {
            $.post("/mycart", { 'del_item': productID });
            subCart(inputval);
            tr.remove();
            grand_total();
            
        }

        else
        {
            if (inputval > 1)
            {       
                input.value = inputval - 1;
                tr.querySelector(".p_total").innerHTML = price * input.value;
                grand_total();
                subCart();
                $.post("/mycart", { 'minus_cart': productID });
            }

        }

    })
}

function check_out(){


}

//Keeping track of Cart
function addCart(){

    if (sessionStorage.cart_quan)
    {
        sessionStorage.cart_quan = Number(sessionStorage.cart_quan) + 1;
        displayCart();
    }

    else 
    {
        sessionStorage.cart_quan = 1;
        displayCart();
    }    

}

function subCart(inputval){

    if (sessionStorage.cart_quan)
    {
        if (inputval)
        {
            sessionStorage.cart_quan = Number(sessionStorage.cart_quan) - inputval;
            displayCart();

        }

        else
        {
            sessionStorage.cart_quan = Number(sessionStorage.cart_quan) - 1;
            displayCart();
        }
    }

}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}



var lrg = document.querySelector('.dtlslrg img');

document.querySelectorAll('.dtlsimgcont img').forEach(_img => _img.addEventListener('click', () => {

    lrg.src = _img.src
    
} ))


//Getting the grand total in the cart route
function grand_total() 
{
    let grandt = 0;
    document.querySelectorAll(".p_total").forEach(p_total =>{ 
        
        grandt += parseInt(p_total.innerHTML);
    
    })
    document.querySelector("#grand_total").innerHTML = grandt;
    return grandt;

}


//Getting the Size of the product
var oneSpanClicked = false;
var selectedSize = null;

document.querySelectorAll(".pinfo_size > span").forEach(_span => _span.addEventListener('click', () => {

    if (oneSpanClicked == false)
    {
        selectedSize = _span.getAttribute('name')
        _span.style.backgroundColor = 'black';
        _span.style.color = 'Red';
        oneSpanClicked = true;

        
    }
    else
    {
        document.querySelectorAll('.pinfo_size > span').forEach(span => {
            span.style.color=""; span.style.backgroundColor = '';
        });

        selectedSize = _span.getAttribute('name')
        _span.style.backgroundColor = 'black';
        _span.style.color = 'Red';
        

    }
}))



