# importing the psycopg2 package
import psycopg2
# connect to the postgress db
conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    port = 5432,
    dbname = 'my_duka',
    password = '11523#Bill'
)
# declare cursor to perform database operations
curr = conn.cursor()
# # products
# def fetch_products():
#     curr = conn.cursor()
#     curr.execute('select * from products;')
#     products = curr.fetchall()
#     return products
# myproducts =fetch_products()
# print(f" My Products========>{myproducts}")
# # display sales on the terminal
# def fetch_sales():
#     curr = conn.cursor()
#     curr.execute('select * from sales;')
#     sales = curr.fetchall()
#     return sales
# sales =fetch_sales()
# print(f" Sales========>{sales}")
# # display stock on the terminal
# def fetch_stock():
#     curr=conn.cursor()
#     curr.execute('select * from stock;')
#     stock = curr.fetchall()
#     return stock
# stock = fetch_stock()
# print(f" Stock========>{stock}")

# create functions to fetch products,sales and stock
def fetch_data(table_name):
    curr.execute(f'select * from {table_name}')
    data = curr.fetchall()
    return data
# products = fetch_data('products')
# print(products)
# stock = fetch_data('stock')
# print(stock)
# sales = fetch_data('sales')
# print(sales)
# insert products using psycopg2(read on documentation and use commit as per the documentation)
# def insert_products(values):
#     querry = "insert into products(name,buying_price,selling_price) values(%s,%s,%s);"
#     curr.execute(querry,values)
#     conn.commit()
# new_product=('mouse',1000,1150)
# insert_products(new_product)
# products=fetch_data('products')
# print(products)

def total_profit():
    query = 'select p.name,p.id, sum((p.selling_price - p.buying_price) * s.quantity) as total_profit from products as p join sales as s on p.id = s.pid group by p.name, p.id;'
    curr.execute(query)
    profit = curr.fetchall()
    return profit
profit = total_profit()
print(profit)
def total_sales():
    query = 'select p.name,p.id,sum(p.selling_price * s.quantity) as total_sales from products as p join sales as s on p.id =s.pid group by p.name,p.id'
    curr.execute(query)
    sales = curr.fetchall()
    return sales
sales = total_sales()
print(sales)