//Getting the Size of the product
var oneSpanClicked = false;
var selectedSize = null;

document.querySelectorAll(".pinfo_size > span").forEach(_span => _span.addEventListener('click', () => {

    if (oneSpanClicked == false)
    {
        selectedSize = _span.innerHTML;
        sizeid = _span.getAttribute('name');
        _span.style.backgroundColor = 'black';
        _span.style.color = 'Red';
        oneSpanClicked = true;

        
    }
    else
    {
        document.querySelectorAll('.pinfo_size > span').forEach(span => {
            span.style.color=""; span.style.backgroundColor = '';
        });

        selectedSize = _span.innerHTML;
        _span.style.backgroundColor = 'black';
        _span.style.color = 'Red';
        

    }
}))


//Display Cart if there is one
displayCart();

//Index Container Dress on Click Shop 
dressClass = document.querySelectorAll('.sendID');

//Add Item to cart function
dressClass.forEach(_dress => _dress.addEventListener('click', () => {

    if (selectedSize == null)
        {
            toastr.options.progressBar = true;
            toastr.options.positionClass = "toast-top-full-width";
            toastr.error("Select Size");
            return;
        }

    var shopYN = confirm('Add item to cart?');
    if (shopYN === true) {
        addCart();
        console.log(selectedSize);
        
        selectedID = parseInt(_dress.getAttribute('name'));
        psid = selectedID + "-" + selectedSize

        $.post("/mycart", { add_cart: JSON.stringify({[psid]: {'sizeid': sizeid, 'quantity': 1}})});
       
    }

    else {
        return false;
    }
})
   
 );

//Add to Cart



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
        let productID = tr.id;
        let price = parseInt(tr.querySelector(".p_price").innerHTML.replaceAll(',', ''));
        console.log(productID)

        if (minplus[i].className.indexOf("plus") != -1)
        {

            if (inputval < 12) 
            {

            input.value = inputval + 1;
            tr.querySelector(".p_total").innerHTML = numberWithCommas(price * input.value);
            grand_total();
            addCart();
        
            $.post("/mycart", { add_cart: productID });
            
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
                tr.querySelector(".p_total").innerHTML = numberWithCommas(price * input.value);
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
        let tot = p_total.innerHTML;
        
        grandt += parseInt(tot.replaceAll(',', ''));
    
    })
    document.querySelector("#grand_total").innerHTML = numberWithCommas(grandt);
    return grandt;

}





//Admin Route Uploading Products
var fimg = null
var bimg = null
document.querySelectorAll("#imgsec img").forEach(_img => _img.addEventListener('click', () => {
  if (fimg == null)
  {
    check = new URL(_img.src)
    fimg = check.pathname;
    _img.style.border = "2.5px solid blue";
    document.querySelector("#fbhead").innerHTML = "Select Product's Back-Image";
    toastr.options.positionClass = "toast-top-center";
    toastr.success("Now Select Back Image");
    document.querySelector('#fimg').value = fimg;
  }
  else if (bimg == null)
  {
    check = new URL(_img.src);
    bimg = check.pathname;
    _img.style.border = "2.5px solid black";
    document.querySelector('#bimg').value = bimg;
    toastr.options.positionClass = "toast-top-center";
    toastr.success("Back Image Selected");
    toastr.info("To RESELECT, refresh the page.");
  }
} ) );


// document.querySelectorAll(".sendID").forEach(_id => _id.addEventListener('click', () => {
//     let pid = _id.closest("productID")
//     $.post("/mycart", pid)
// }) );

const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav_links');
    const navLinks = document.querySelectorAll('.nav_links > li');
    //Toggle Nav
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
        //Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards  ${index / 7 + 1.1}s`;
            }
        });

    });
};

// navSlide();

const srchAct = () => {

const srchIcon = document.querySelector('#srchIcon');
const searcher = document.querySelector('.searcher');

srchIcon.addEventListener('click', () =>{ 
    searcher.classList.toggle('searcher-active');
});
};




const expimg = () => {
    const hidden = document.querySelectorAll('.hidden');
    // async function start() {

    //     await new Promise(resolve => setTimeout(resolve, 100));
    //  }
    
    console.log('working');
    hidden.forEach(hidimg => {
        if (hidimg.style.opacity == 0){

            hidimg.style.opacity = '1';
            hidimg.style.zIndex = '1';
            document.querySelectorAll('.shoP').forEach(shop => {
                shop.style.opacity = '1'
            });
        }

        else {
            hidimg.style.opacity = '0';
            hidimg.style.zIndex = '0';
            document.querySelectorAll('.shoP').forEach(shop => {
                shop.style.opacity = '0'
            });
            
        };
    });
};

setInterval(expimg, 3000);



