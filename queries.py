from logic import multiIdQ
from flask import session
from database import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    cateid = db.Column(db.Integer, db.ForeignKey('pcategory.id'))
    stock = db.Column(db.Integer)
    price = db.Column(db.Float)
    color = db.Column(db.Integer, db.ForeignKey('color.id'))
    fimg = db.Column(db.String)
    bimg = db.Column(db.String)

class Pcategory(db.Model):
    __tablename__ = 'pcategory'
    id = db.Column(db.Integer, primary_key=True)
    catname = db.Column(db.String)

class Color(db.Model):
    __tablename__ = 'color'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String)

class Size(db.Model):
    __tablename__ = 'sizes'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String)

class ProductImg(db.Model):
    __tablename__ = 'productimg'
    id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    url = db.Column(db.String)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    hash = db.Column(db.String)
    email = db.Column(db.String)

class Cart(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('users.id'))
    firstName = db.Column(db.String)
    middleName = db.Column(db.String)
    lastName = db.Column(db.String)
    mobile = db.Column(db.String)
    email = db.Column(db.String)
    line1 = db.Column(db.String)
    line2 = db.Column(db.String)
    city = db.Column(db.String)
    province = db.Column(db.String)
    zip = db.Column(db.String)

class CartProduct(db.Model):
    __tablename__ = 'cart_products'
    cart_product_id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey('products.id'))
    sizeid = db.Column(db.Integer, db.ForeignKey('sizes.id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'))

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'))
    grand_total = db.Column(db.Float)

def displayAllProducts():
    return Product.query.with_entities(Product.id, Product.price, Product.fimg, Product.bimg, Product.name).all()

def get_product(pid):
    return db.session.query(Product.id, Product.stock, Product.price, Product.fimg, Color.color, Product.name, Pcategory.catname)\
        .join(Color, Color.id == Product.color)\
        .join(Pcategory, Pcategory.id == Product.cateid)\
        .filter(Product.id == pid).all()

def getSize():
    return Size.query.all()

def get_pimgs(pid):
    return ProductImg.query.filter_by(id=pid).all()

def priceq():
    return Product.query.order_by(Product.price).all()

def productCategoryWise(cid):
    return db.session.query(Product.id, Product.fimg, Product.bimg, Product.price, Product.name, Pcategory.catname, Pcategory.id.label('catid'))\
        .join(Pcategory, Product.cateid == Pcategory.id)\
        .order_by(db.case([(Pcategory.id == cid, 1)], else_=2), Pcategory.id).all()

def allCategories():
    return Pcategory.query.all()

def getAllDictP(cart):
    product_ids = [int(key.split('-')[0]) for key in cart.keys()]
    return Product.query.filter(Product.id.in_(product_ids)).order_by(Product.id).all()

def colorOption():
    return Color.query.all()

def registerUser(username, password, email):
    new_user = User(username=username, hash=password, email=email)
    db.session.add(new_user)
    db.session.commit()
    return "Complete"

def checkLogin(username):
    return User.query.filter_by(username=username).all()

def searchAttributes(immuDict):
    query = db.session.query(Product.id, Product.name, Pcategory.catname, Product.stock, Product.price, Color.color, Product.fimg)\
        .join(Color, Color.id == Product.color)\
        .join(Pcategory, Pcategory.id == Product.cateid)
    for key, val in immuDict.items():
        if key == 'p.id':
            query = query.filter(Product.id.in_([int(v) for v in val]))
        elif key == 'p.cateid':
            query = query.filter(Product.cateid.in_([int(v) for v in val]))
        elif key == 'p.color':
            query = query.filter(Product.color.in_([int(v) for v in val]))
    return query.all()

def check_out(userid, firstName, midName, lastName, email, mobile, address, address2, city, state, zipcode):
    new_cart = Cart(id=userid, firstName=firstName, middleName=midName, lastName=lastName, mobile=mobile, email=email,
                    line1=address, line2=address2, city=city, province=state, zip=zipcode)
    db.session.add(new_cart)
    db.session.commit()
    lastrid = new_cart.cart_id
    grand_total = 0
    for key, val in session['cart'].items():
        pid = int(key.split('-')[0])
        sizeid = val['sizeid']
        qty = val['quantity']
        product = Product.query.get(pid)
        price = product.price
        grand_total += price * qty
        new_cart_product = CartProduct(pid=pid, sizeid=sizeid, quantity=qty, price=price, cart_id=lastrid)
        db.session.add(new_cart_product)
        product.stock -= qty
    new_order = Order(userid=userid, cart_id=lastrid, grand_total=grand_total)
    db.session.add(new_order)
    db.session.commit()
    session.pop('cart', None)
    return new_order.order_id

def makeProduct(pn, pp, ps, pclr, pc, fimg, bimg):
    new_product = Product(name=pn, cateid=int(pc), stock=int(ps), price=float(pp), color=int(pclr), fimg=fimg, bimg=bimg)
    db.session.add(new_product)
    db.session.commit()
    pid = new_product.id
    for value in session['file']:
        new_img = ProductImg(id=pid, url=value)
        db.session.add(new_img)
    db.session.commit()
    session.pop('file', None)
    return 0

def deleteProduct(proid):
    Product.query.filter_by(id=proid).delete()
    ProductImg.query.filter_by(id=proid).delete()
    db.session.commit()
    return 0