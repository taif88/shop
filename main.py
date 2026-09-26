from flask import *
from dataBase.db import *

app = Flask(__name__)
app.secret_key = "00000"

setup_database()

@app.route("/",methods=['GET','POST'])
def main_page():
    if 'name' in session and session['name'] :
        print(session['cart'])
        return render_template("index.html" ,name =session['name'])
    else:
        return redirect(url_for('signup_page'))
    

@app.route("/signup",methods=['GET','POST'])
def signup_page():
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('password')
    print(name)
    db=Database()
    check  = db.add_user(name,email,password)
    print(check)
    if check == True :
        session['name'] = name
        return redirect(url_for('main_page'))
    return render_template("signup.html")

@app.route("/login",methods=['GET','POST'])
def login_page():
    email = request.args.get('email')
    password = request.args.get('password')
    db=Database()
    check  = db.get_user(email,password)
    if email ==None and password == None :
        error = ""
        return render_template("login.html",error=error)
    elif  check == 1:
        error = "The passowrd is wrong"
        return render_template("login.html",error=error)
    elif check == 0 :
        error = "The email is not used"
        return render_template("login.html",error=error)
    elif check != 0 and check != 0 :
        error = ""
        session['name'],session['id'] = check
        session['cart'] = []
        return redirect(url_for('main_page'))
    error = ""
    return render_template("login.html",error=error)


@app.route("/explore",methods=['GET','POST'])
def explore_page():
    name = request.args.get('search')
    return render_template("explore.html",Name=name,name =session['name'])
@app.route("/api/explore",methods=['GET','POST'])
def explore_request():
    name = request.args.get('search')
    db = Database()
    productsr=db.get_products(name)
    products={}
    for product in productsr:
        p={"productid":product[0],"productname":product[1],"productdis":product[2],"productpri":product[3],"productcat":product[4]}
        pn = f"product{product[0]}"
        products[pn] = p
    return jsonify(products)

@app.route("/api/main",methods=['GET','POST'])
def main_request():
    name = request.args.get('search')
    db = Database()
    productsr=db.get_products(name)
    products={}
    for product in productsr:
        p={"productid":product[0],"productname":product[1],"productdis":product[2],"productpri":product[3],"productcat":product[4]}
        pn = f"product{product[0]}"
        products[pn] = p
    return jsonify(products)

@app.route("/logout",methods=['GET','POST'])
def logout_page():
    try:
        session['name'] = None
        return redirect(url_for("signup_page"))
    except :
        return redirect(url_for("main_page"))


@app.route("/wishlist",methods=['GET','POST'])
def wishlist_page():
    return render_template("wishlist.html",name =session['name'])

@app.route("/api/wishlist",methods=['POST'])
def wishlist():
    data=request.get_json() or {}
    db = Database()
    if data.get("wishlist") == "True":
        db.set_wishlist(session["id"],data.get("productid"))
    else:
        print("t")
    return json({"":""})
    

@app.route("/api/wishlist",methods=['GET'])
def wishlist_check():
    id= request.args.get("id")
    db = Database()
    response={"inwishlist":db.get_wishlist(session["id"],id)}
    return jsonify(response)

@app.route("/profile")
def profile():
    if 'name' in session and session['name'] :
        db = Database()
        name = session['name']
        return render_template("profile.html" ,Name = name,email = db.get_email(session['name']))
    else:
        return redirect(url_for('signup_page'))

@app.route("/addcart")
def add_cart():
    id = request.args.get('id')
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(id)
    session.modified=True
    print(session['cart'])
    return redirect(url_for('main_page'))

@app.route("/cart")
def cart_page():
    return render_template("cart.html",name =session['name'])

@app.route("/api/cart")
def cart():
    db =Database()
    products = db.get_product_by_ids(session['cart'])
    projs={}
    for product in products:
        pro={"pron":product[1],"propri":product[3]}
        print(product)
        pron=f"pronum{products.index(product)}"
        projs[pron]= pro
    print(projs)
    return jsonify(projs)


@app.route("/product")
def product_page():
    id = request.args.get('id')
    db = Database()
    # print(db.get_product_by_id(id))
    return render_template("product.html",name =session['name'],product=db.get_product_by_id(id))

@app.route("/orders")
def orders_page():
    return render_template("orders.html",name =session['name'])

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404error.html",name =session['name'])



if __name__ == "__main__" :

    app.run(debug = True , port=2000)

