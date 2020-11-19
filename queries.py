from cs50 import SQL
import logic
import json
import ast
from flask import session

    
#Configuring sqlite

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")

#Getting all products
def displayAllProducts():

    #Query for the most purchased products - Displaying Top Picks Dresses on index.html 
    dressimgs = db.execute("SELECT products.id, products.price, products.fimg, products.bimg, products.name FROM products;")

    return dressimgs

#Getting a specific product from database
def get_product(pid):
    getp = db.execute("SELECT products.id, products.stock, products.price, products.fimg, colortable.color, products.name, pcategory.catname FROM color colortable JOIN products ON colortable.id = products.color JOIN pcategory ON products.cateid = pcategory.id WHERE products.id = :proid;", proid = pid)
    return getp

#Get the Size attribute from the DB
def getSize():
    size = db.execute('SELECT id, size FROM sizes;')
    return size

#Get product all of products imgs
def get_pimgs(pid):
    getImgs = db.execute('SELECT url FROM productimg WHERE id = :pid;', pid=pid)
    return getImgs

#Price Query for search
def priceq():
    price = db.execute("SELECT products.price, products.id FROM products ORDER BY price;")
    return price


def productCategoryWise(cid):

    cateID = cid

    #Query for whichever category user clicked on
    query = db.execute("SELECT products.id, fimg, bimg, products.price, products.name, pcategory.catname, pcategory.id AS catid FROM products JOIN pcategory ON products.cateid = pcategory.id ORDER BY CASE WHEN catid = :cateID THEN 1 ELSE 2 END, catid;", cateID = cateID)
    return query

#All Categories
def allCategories():
    dcatelist = db.execute("SELECT id, catname FROM pcategory;")
    return dcatelist


def getAllDictP(cart):
    #Placing the user Selected Product ID into DB querry
    forQ = ''
    for i in str(cart.keys()):
        if i.isdigit() or i == ',':
            forQ += i
    ex_str = 'SELECT p.id, p.name, p.cateid, p.stock, p.price, p.fimg FROM products p WHERE p.id IN (' + forQ + ') ORDER BY p.id ; '
    dbcounted = db.execute(ex_str)

    return dbcounted

#Dynamic Search Option
def colorOption():
    colors = db.execute('SELECT * FROM color;')
    return colors

def registerUser(username, password, email):
    db.execute("INSERT INTO users (username, hash, email) VALUES (?, ?, ?)", username, password, email)
    return "Complete"

def checkLogin(username):
    row = db.execute("SELECT * FROM users WHERE username = :username", username=username)
    return row

#Search feature for searching products with their respective attributes
def searchAttributes(immuDict):
    ex_str = 'SELECT p.id, p.name, pc.catname, p.stock, p.price, colortable.color, p.fimg FROM products p JOIN color colortable ON colortable.id = p.color JOIN pcategory pc ON p.cateid = pc.id WHERE '
    for i, (key, val) in enumerate(immuDict.items()):
        if key == 'p.id' or key == 'p.cateid' or key == 'p.color':
            if i == 0:
                qstr = str(key) + ' IN (' + logic.multiIdQ(val) + ')'
                ex_str = ex_str + qstr

            else:
                qstr = ' AND ' + str(key) + ' IN (' + logic.multiIdQ(val) + ')'
                ex_str = ex_str + qstr

    return db.execute(ex_str)
    
    
def check_out(userid, firstName, midName, lastName, email, mobile, address, address2, city, state, zipcode):

    import sqlite3
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    sql = 'INSERT INTO cart (id, firstName, middleName, lastName, mobile ,email, line1, line2, city, province, zip) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(sql, (userid, firstName,
    midName, lastName, mobile, email, address, address2, city, state, zipcode))

    lastrid = cursor.lastrowid

    #Adding Cart Items into Database
    grand_total = 0
    for key, val in session['cart'].items():
        pid = key.split('-')[0]
        sizeid = val['sizeid']
        qty = val['quantity']
        price = db.execute("SELECT price FROM products WHERE id = :pid", pid = pid)[0]['price'] #Getting pro price from DB
        grand_total += price * qty
        sql = 'INSERT INTO cart_products (pid, sizeid, quantity, price, cart_id) VALUES (?, ?, ?, ?, ?)'
        cursor.execute(sql, (pid, sizeid, qty, price, lastrid))

    sql = "INSERT INTO orders (userid, cart_id, grand_total) VALUES (?, ?, ?)"
    cursor.execute(sql, (userid, lastrid, grand_total))
    orderid = cursor.lastrowid
    sql = "UPDATE products SET stock = stock - :qty WHERE id = :pid;"
    cursor.execute(sql, (qty, pid))

    connection.commit()
    cursor.close()
    connection.close()

    return orderid

def makeProduct(pn, pp, ps, pclr, pc, fimg, bimg):
    import sqlite3
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    sql = "INSERT INTO products (name, cateid, stock, price, color, fimg, bimg) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, (pn, pc, ps, pp, pclr, fimg, bimg))
    pid = cursor.lastrowid
    for value in session['file']:
        sql = "INSERT INTO productimg (id, url) VALUES (?, ?)"
        cursor.execute(sql, (pid, value))

    connection.commit()
    cursor.close()
    connection.close()

    return 0

def deleteProduct(proid):
    db.execute('DELETE FROM products WHERE id = :proid', proid=proid)
    return 0
    

    
