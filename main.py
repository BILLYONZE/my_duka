# Importing flask 
from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_products,insert_sales,insert_stock


# importing the fetch data function to main
from database import fetch_data

# instance of the flask class
app = Flask(__name__)

# creating a route
@app.route('/')
def home():
    return render_template ('index.html')

# product routes
@app.route('/products')
def products():
    products = fetch_data('products')
    print(products)
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
        return redirect(url_for('products'))
    return redirect(url_for('products'))
    
# sales route
@app.route('/sales')
def sales():
    sales = fetch_data('sales')
    print(sales)
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
        return redirect(url_for('stock'))
    return redirect(url_for('stock'))

# stock route
@app.route('/stock')
def stock():
    stock=fetch_data('stock')
    print(stock)
    products=fetch_data('products')
    return render_template('stock.html', stocks = stock ,products=products)
app.run(debug=True)

# How to use JInja
# 1. Variables are written inside double curly braces{{}} and the Variable itself must be declared in a render_template function
# 2.A python operstion is written inside single curly braces{} with percentage signs{ % for i in sequence% } and the operation must be closed{%endfor%}

# HTTP METHODS
#1.GET
#2.POST

