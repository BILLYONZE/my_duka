# Importing flask 
from flask import Flask,render_template,request,redirect,url_for,flash,session
from database import fetch_data, get_profit_day, get_sales_per_day,insert_products,insert_sales,insert_stock,total_profit,insert_users,check_email,total_sales
from flask_bcrypt import Bcrypt

# importing the fetch data function to main
from database import fetch_data

# instance of the flask class
app = Flask(__name__)

# instance of Flash
app=Flask(__name__)
app.secret_key= "broooooo/"

# instance of Password Bcrypt
bcrypt = Bcrypt(app)
# creating a route
@app.route('/')
def home():
    return render_template ('index.html')

# product routes
@app.route('/products')
def products():
    products = fetch_data('products')
    # print(products)
    return render_template('products.html',products=products)

# adding Products
@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method =='POST':
        product_name = request.form['product_name']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        added_product =(product_name,buying_price,selling_price)
        insert_products(added_product)
        flash('Added a New Product','success')
        return redirect(url_for('products'))
    return redirect(url_for('products'))
    
# sales route
@app.route('/sales')
def sales():
    sales = fetch_data('sales')
    # print(sales)
    products=fetch_data('products')
    return render_template('sales.html',sales=sales, products=products)

# adding sales
@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    if request.method=='POST':
        product_id=request.form['pid']
        sales_quantity =request.form['s.quantity']
        created_at = request.form['created_at']
        sales_data =(product_id,sales_quantity,created_at)
        insert_sales(sales_data)
        return redirect(url_for('sales'))
    return redirect(url_for('sales'))

# adding stock
@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method=='POST':
        product_id=request.form['pid']
        stock_quantity =request.form['st.quantity']
        stock_added =(product_id,stock_quantity)
        insert_stock(stock_added)
        flash("New stock added",'info')
        return redirect(url_for('stock'))
    return redirect(url_for('stock'))

# stock route
@app.route('/stock')
def stock():
    stock=fetch_data('stock')
    # print(stock)
    products=fetch_data('products')
    return render_template('stock.html', stocks = stock ,products=products)

# dashboard
@app.route('/dashboard')
def dashboard():
    profits = total_profit()
    sales = total_sales()
    product_name =[]
    product_profit=[]
    total_sale = []
    # profit per product
    for i in profits:
        product_name.append(i[0])
        product_profit.append(float(i[1]))
    # total sales
    for j in sales:
        product_name.append(j[0])
        total_sale.append(float(j[2]))
    # Profit per day and # sales per day
    p_day = get_profit_day()
    sales_data = get_sales_per_day()
    dates = [row[0].strftime('%Y-%m-%d') for row in sales_data]
    sales_per_day = [float(row[1]) for row in sales_data]
    # profit_per_day = [i[1] for i in p_day]   
    return render_template( 'dashboard.html',product_name=product_name ,
    product_profit=product_profit,total_sale=total_sale,dates=dates,sales_per_day=sales_per_day)
    # profit_per_day=profit_per_day

# @app.route('/dashboard')
# @login_required
# def dashboard():
#     # --- sales per day ---
#     sales_data = get_sales_per_day()

#     # unpack tuples
#     dates = tuple(item[0] for item in sales_data)
#     sales_per_day = tuple(item[1] for item in sales_data)

#     return render_template(
#         'dashboard.html',
#         dates=dates,
#         sales_per_day=sales_per_day,
#         # … include other context variables …
#     )

# register
@app.route('/register', methods =['GET','POST'])
def register():
# check the method
    if request.method =='POST':
        # get form data
        fname = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        # hash password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        # to insert new user
        new_user=(fname,email,hashed_password)
        # check the email
        check = check_email(email)
        if check == None:
        # insert user
            insert_users(new_user)
            flash("Account successfully Created. You can log in")
            return redirect(url_for('login'))
        else:
            flash("You already have an account. Log in")
            return redirect(url_for('login'))    
    return render_template('register.html')

#  login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':
        email = request.form["email"]
        password = request.form["password"]

        check = check_email(email)
        if check==None:
            flash("Account not found.Kindly Sign Up","danger")
            return redirect(url_for("register"))
        else:
             if bcrypt.check_password_hash(check[-1],password):
                session['email']=email
                flash ("Login Successfully",'success')
                return redirect(url_for("dashboard"))
             else:
                flash("Invalid Password",'danger')
                return redirect(url_for("register"))
    return render_template("login.html")     
   
app.run(debug=True)
 
# How to use Jinja
# 1. Variables are written inside double curly braces{{}} and the Variable itself must be declared in a render_template function
# 2.A python operstion is written inside single curly braces{} with percentage signs{ % for i in sequence% } and the operation must be closed{%endfor%}

# HTTP METHODS
#1.GET
#2.POST


