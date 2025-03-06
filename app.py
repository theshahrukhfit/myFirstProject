import os
import re
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from collections import defaultdict
from helpers import apology, login_required, usd, success
from database import db

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure upload folder
app.config['UPLOAD_PATH'] = 'static/images/dresses'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']

# Configure session to use filesystem
app.config["SESSION_FILE_DIR"] = os.path.join(os.getcwd(), 'sessions')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # Initialize db with the app instance
from queries import *
from logic import *


# Custom filter for formatting currency
def pkr(value):
    return f"{value:,}"
app.jinja_env.filters['pkr'] = pkr

# Global variable for dynamic nav drop-down menu
@app.context_processor
def context_processor():
    dcatelist = allCategories()
    return dict(dcatelist=dcatelist)

@app.route("/", methods=["GET", "POST"])
def index():
    dressimgs = displayAllProducts()
    colors = colorOption()
    checkrange = pricerange()
    return render_template("index.html", dressimgs=dressimgs, colors=colors, priceap=checkrange)

@app.route("/categories", defaults={'cid': 1}, methods=['GET', 'POST'])
@app.route("/categories/<int:cid>", methods=['GET', 'POST'])
def category(cid):
    query = productCategoryWise(cid)
    dressimgs = displayAllProducts()
    colors = colorOption()
    checkrange = pricerange()
    catedict = defaultdict(list)
    for row in query:
        catedict[row.catname].append({
            'id': row.id,
            'fimg': row.fimg,
            'bimg': row.bimg,
            'price': row.price,
            'name': row.name,
            'catname': row.catname,
            'catid': row.catid
        })
    return render_template("dresses.html", catedict=catedict, colors=colors, priceap=checkrange)

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        rows = checkLogin(request.form.get("username"))
        if len(rows) != 1 or not check_password_hash(rows[0].hash, request.form.get("password")):
            flash("Enter a valid username and password")
            return apology("invalid username and/or password", 403)
        session["user_id"] = rows[0].id
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    if request.method == 'POST':
        rows = checkLogin(request.form.get("username"))
        specialC = re.findall(r"\W", request.form.get("password"))
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
            return apology("User already exists, try a different username.", 403)
        else:
            registerUser(request.form.get("username"), generate_password_hash(request.form.get("password")), request.form.get("email"))
            return redirect("/login")
    return render_template("login.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/testroute", methods=['POST', 'GET'])
def testroute():
    if request.method == 'POST':
        if 'cart' not in session:
            session['cart'] = {}
        if request.form.get('add_cart'):
            dit = json.loads(request.form.get('add_cart'))
            add2CartFunc(dit)
    return 'OK'

@app.route("/mycart", methods=['POST', 'GET'])
def mycart():
    if request.method == "POST":
        if request.form.get('minus_cart'):
            minusCart(json.loads(request.form.get('minus_cart')))
            return 'ok'
        elif request.form.get('add_cart'):
            productnSize = request.form.get('add_cart')
            if "null" in productnSize:
                return "Don't proceed"
            add2cart = json.loads(productnSize)
            add2CartFunc(add2cart)
            return 'OK'
        elif request.form.get('del_item'):
            product_id_to_del = request.form.get('del_item')
            delCart(json.loads(product_id_to_del))
            return 'Ok'
    if 'cart' in session:
        getdata = getAllDictP(session['cart'])
        dbcounted = []
        for key, val in session['cart'].items():
            skey = key.split('-')
            for row in getdata:
                if int(skey[0]) == row.id:
                    rowcpy = {
                        'id': row.id,
                        'name': row.name,
                        'cateid': row.cateid,
                        'stock': row.stock,
                        'price': row.price,
                        'fimg': row.fimg,
                        'size': skey[1],
                        'sizeid': val['sizeid'],
                        'Quantity': val['quantity']
                    }
                    dbcounted.append(rowcpy)
        return render_template("mycart.html", dbcounted=dbcounted)
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
            userid = session.get('user_id')
            orderid = check_out(
                userid, request.form.get("firstName"), request.form.get("midName"),
                request.form.get("lastName"), request.form.get("email"), request.form.get("mobile"),
                request.form.get("address"), request.form.get("address2"), request.form.get("inputCity"),
                request.form.get("state"), request.form.get("inputZip")
            )
            return success("Checkout Successful. Your Order ID is " + str(orderid))
    return render_template("checkout.html")

@app.route("/search", methods=['POST', 'GET'])
def search():
    if request.method == "POST":
        query = searchAttributes(request.form)
        return render_template("search.html", query=query)
    return render_template("search.html")

@app.route("/vitem/<int:proid>", methods=['GET', 'POST'])
def itemdtls(proid):
    product_details = get_product(proid)
    size = getSize()
    pimgs = get_pimgs(proid)
    return render_template('itemdetls.html', product=product_details, size=size, pimgs=pimgs)

@app.route("/admin", methods=['GET', 'POST'])
@login_required
def uploadimg():
    if session.get("user_id") == 1:
        colors = colorOption()
        categories = allCategories()
        if request.method == "POST":
            if request.files.getlist('imgfiles'):
                file_list = request.files.getlist('imgfiles')
                if 'file' in session:
                    session['file'].clear()
                for uploaded_file in file_list:
                    filename = secure_filename(uploaded_file.filename)
                    if filename:
                        file_ext = os.path.splitext(filename)[1]
                        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                            return apology("File type not supported", 400)
                        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
                        if 'file' not in session:
                            session['file'] = []
                        session['file'].append('/' + os.path.join(app.config['UPLOAD_PATH'], filename).replace('\\', '/'))
                files = session['file']
                return render_template("admin.html", colors=colors, categories=categories, files=files)
            else:
                if not request.form.get("pname"):
                    flash("Provide Product's Name")
                elif not request.form.get("pprice"):
                    flash("Provide Product's Price")
                elif not request.form.get("pstock"):
                    flash("Provide Product's Stock")
                elif not request.form.get("pcolor"):
                    flash("Select a color")
                elif not request.form.get("pcate"):
                    flash("Select Provide's Category")
                elif not request.form.get("fimg") and not request.form.get("bimg"):
                    flash("Select Product's Image")
                    files = os.listdir(app.config['UPLOAD_PATH'])
                    return render_template("admin.html", colors=colors, categories=categories, files=files)
                else:
                    fimg, bimg = request.form.get("fimg"), request.form.get("bimg")
                    pname, pprice, pstock, pcolor, pcate = request.form.get("pname"), request.form.get("pprice"), request.form.get("pstock"), request.form.get("pcolor"), request.form.get("pcate")
                    makeProduct(pname, pprice, pstock, pcolor, pcate, fimg, bimg)
                    return success("Product has been added to Database.")
        return render_template("admin.html", colors=colors, categories=categories)
    return apology("Access Denied")

@app.route('/viewproducts')
def viewpro():
    products = displayAllProducts()
    return render_template("allpro.html", products=products)

@app.route('/delpro/<int:proid>')
@login_required
def delpro(proid):
    if session['user_id'] == 1:
        deleteProduct(proid)
    return redirect(url_for('viewpro'))

def errorhandler(e):
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    app.run(debug=True)