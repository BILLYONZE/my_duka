# Importing flask 
from flask import Flask,render_template
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
def prods():
    products = fetch_data('products')
    print(products)
    return render_template('products.html',products=products)
    
# sales route
@app.route('/sales')
def sales():
    sales = fetch_data('sales')
    print(sales)
    return render_template('sales.html',sales=sales)

# stock route
@app.route('/stock')
def stock():
    
    return render_template('stock.html')
app.run()

# How to use JInja
# 1. Variables are written inside double curly braces{{}} and the Variable itself must be declared in a render_template function
# 2.A python operstion is written inside single curly braces{} with percentage signs{ % for i in sequence% } and the operation must be closed{%endfor%}
