import os
import re

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import sys
from collections import defaultdict

from helpers import apology, login_required, usd, success
from forms import *
from logic import *


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#GLOBAL Variable for dynamic nav drop-down menu
@app.context_processor
def context_processor():
    dcatelist = allCategories()
    return dict(dcatelist = dcatelist)


#Routes
@app.route("/", methods=["GET", "POST"])
def index():
            
    #Getting All dresses and its related information for display
    dressimgs = displayAllProducts()
    colors = searchOption()
    checkrange = pricerange()

    return render_template("index.html", dressimgs = dressimgs, colors = colors, priceap = checkrange)

@app.route("/categories", defaults={'cid': '1'}, methods=['GET', 'POST'])
@app.route("/categories/<int:cid>", methods=['GET', 'POST'])
def category(cid):

    #Query
    query = productCategoryWise(cid)
    dressimgs = displayAllProducts()
    colors = searchOption()
    checkrange = pricerange()

    #Creating distinct category under which its items falls
    catedict = defaultdict(list)

    for row in query:
        catedict[row['catname']].append(row)

    print(query)
    return render_template("dresses.html", catedict = catedict, colors = colors, priceap = checkrange)


#Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = checkLogin(request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):

            flash("Enter a valid useername and password")
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

#Register User
@app.route("/register", methods=["GET", "POST"])
def register():

    session.clear()

    if request.method == 'POST':

        #Checking whether username and password field are not empty & both password fields match
        #Database
        rows = checkLogin(request.form.get("username"))

        #Unique password with special character REGEX
        specialC = re.findall("\W", request.form.get("password"))

        if not request.form.get("username"):
            return apology("Provide username to register.", 403)

        elif not request.form.get("password"):
            return apology("Provide password", 403)

        elif not specialC:
            return apology("Include any one special character in your password to make it stronger.")

        elif not request.form.get("password1"):
            return apology("Password retype field empty.", 403)

        elif request.form.get("password") != request.form.get("password1"):
            return apology("Passwords do not match. Retry.", 403)

        elif not request.form.get("email") or not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", request.form.get("email")):
            return apology("Not a valid email or field was empty.")

        elif len(rows) == 1:
            return apology("User already exist, try different username.", 403)
        else:
            registerUser(request.form.get("username"), generate_password_hash(request.form.get("password")), request.form.get("email"))
            return redirect("/login")

    return render_template("login.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

##Cart Route
@app.route("/mycart", methods=['POST', 'GET'])
def mycart():

    if request.method == "POST":

        if request.form.get('minus_cart'):
            product_id1 = request.form.get('minus_cart')
            session['cart'].remove(int(product_id1))
            return 'ok'

        #AJAX Request to add to cart
        elif request.form.get('add_cart'):
            product_id = request.form.get('add_cart')

            #Creating cart in the session for user
            if 'cart' not in session:
                session['cart'] = []
            
            #Appending the value(productID) into temp list that user clicked on
            session['cart'].append(int(product_id))
            
            return 'OK'
        
        #Deleting Item from Cart
        elif request.form.get('del_item'):
            product_id_to_del = int(request.form.get('del_item'))
            session['cart'] = list(filter((product_id_to_del).__ne__, session['cart']))
     
            return 'Ok'

    if 'cart' in session:

        #Counting the quantity of selected products if more than one add their quantity
        counter = {}
        for i in session['cart']:
            counter[i] = counter.get(i, 0)+1

        #Getting All Products inside Dictionary from Database
        dbcounted = getAllDictP(counter)

        #Adding the counted quantity dictionary into the query
        for j in range(len(dbcounted)):
            dbcounted[j].update({'Quantity': counter[dbcounted[j]['id']]})
        
        print(dbcounted)

        return render_template("mycart.html", dbcounted = dbcounted)
    
    return render_template("mycart.html")

@app.route("/checkout", methods=["POST", "GET"])
def checkout():
    if request.method == "POST":
        if not request.form.get("firstName"):
            flash("Provide First Name")

        elif not request.form.get("midName"):
            flash("Provide Middle Name")

        elif not request.form.get("lastName"):
            flash("Provide Last Name")

        elif not request.form.get("email"):
            flash("Provide an Email")

        elif not request.form.get("mobile"):
            flash("Provide mobile contact")

        elif not request.form.get("address"):
            flash("Provide an address")

        elif not request.form.get("inputCity"):
            flash("City field is empty")

        elif not request.form.get("state"):
            flash("State field is empty")

        elif not request.form.get("inputZip"):
            flash("Zip field is empty")

        else:
            if 'user_id' in session:
                userid = session['user_id']

            else:
                userid = None

            check_out(userid, request.form.get("firstName"), request.form.get("midName"), request.form.get("lastName"), request.form.get("email"),
            request.form.get("mobile"), request.form.get("address"), request.form.get("address2"), request.form.get("inputCity"), request.form.get("state"),
            request.form.get("inputZip"))
            return success("Checkout Successful")


    return render_template("checkout.html")


@app.route("/search", methods=['POST', 'GET'])
def search():
    if request.method == "POST":

        if request.form.get("colorcheckbox") or request.form.get("pricecheckbox"):

            query = searchAttributes(request.form)

            return render_template("search.html", query = query)

    return render_template("search.html")

@app.route("/vitem", methods=['POST', 'GET'])
def itemdtls():
    return render_template('itemdetls.html')


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)