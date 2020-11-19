import queries
from collections import defaultdict
from flask import session

#Getting Price Ranges and Their respective products
def pricerange():
    initprice = 0
    pricerange = 0
    pricedict = defaultdict(list)
    for i in queries.priceq():
        price = int(i['price'])
        if pricerange < price:
            initprice = price
            pricerange = price + 500
        pricedict[f'Price Range: {initprice} - {pricerange}'].append(i['id'])

    return pricedict

#Removing '[]' from Lists
def multiIdQ(toProcess):
    forQuery = str(toProcess).translate({ord(i):None for i in '[]\''})
    return forQuery

#Count the occurance of object in the list

# Add Item to Cart
def add2CartFunc(add2cart):
    #Creating cart in the session for user
    if 'cart' not in session:
        session['cart'] = {}
        
    if not session['cart']:
        session['cart'].update(add2cart)

    else:
        citem = session['cart'].get(list(add2cart.keys())[0])
        if citem:
             citem['quantity'] += 1
        else:
            session['cart'].update(add2cart)


def minusCart(pinfo):
    citem = session['cart'].get(list(pinfo.keys())[0])
    if citem['quantity'] > 1:
        citem['quantity'] -= 1

def delCart(pinfo):
    del session['cart'][list(pinfo.keys())[0]]

    

        
