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


# create functions to fetch products,sales and stock
def fetch_data(table_name):
    curr.execute(f'select * from {table_name}')
    data = curr.fetchall()
    return data


# insert products using psycopg2(read on documentation and use commit as per the documentation)
def insert_products(values):
    querry = "insert into products(name,buying_price,selling_price) values(%s,%s,%s);"
    curr.execute(querry,values)
    conn.commit()


# insert sales 
def insert_sales(values):
    querry = "insert into sales(pid,quantity,created_at) values(%s,%s,%s);"
    curr.execute(querry,values)
    conn.commit()


# inserting stock
def insert_stock(values):
    querry = "insert into stock(pid,stock_quantity) values(%s,%s);"
    curr.execute(querry,values)
    conn.commit()

# Inserting users
def insert_users(values):
    querry = 'insert into users(full_name,email,password) values(%s,%s,%s);'
    curr.execute(querry,values)
    conn.commit()


# profits function
# Profit = (product selling_price  -  product buying_price) * sales quantity of the product
def total_profit():
    query = 'select p.name, sum((p.selling_price - p.buying_price) * s.quantity) as total_profit from products as p join sales as s on p.id = s.pid group by p.name;'
    curr.execute(query)
    profit = curr.fetchall()
    return profit

# sales function
def total_sales():
    query = 'select p.name,p.id,sum(p.selling_price * s.quantity) as total_sales from products as p join sales as s on p.id =s.pid group by p.name,p.id;'
    curr.execute(query)
    sales = curr.fetchall()
    return sales
# Profit per day
def get_profit_day():
    querry='SELECT DATE (S.created_at) AS sale_date,sum((p.selling_price-p.buying_price)*s.quantity) AS total_profit ' \
    'FROM sales AS S Join products P on s.id=p.id group by DATE(s.created_at)' \
    ' ORDER BY sale_date;'
    curr.execute(querry)
    rows=curr.fetchall()
    # print (data)
    return rows

 # sales per day
def get_sales_per_day():
    curr = conn.cursor()
    querry = "SELECT DATE(s.created_at) AS day,SUM(p.selling_price * s.quantity) AS total_sales FROM sales AS s JOIN products AS p ON s.pid = p.id GROUP BY DATE(s.created_at)ORDER BY DATE(s.created_at);"
    curr.execute(querry)
    rows = curr.fetchall()
    result = tuple((row[0], float(row[1] or 0)) for row in rows)
    return result


# def sales_day():
#     query='SELECT DATE (s.created_at) AS Day,sum(p.selling_price * s.quantity) AS Total_sales FROM sales AS S JOIN products AS P on s.id=p.id GROUP BY DATE (s.created_at) ORDER BY DATE(s.created_at);'
#     curr.execute(query)
#     data=curr.fetchall()
#     # print (data)
#     return data

# get sales per day
# def get_sales_per_day():
#     querry="SELECT DATE(s.created_at) AS day, SUM(p.selling_price * s.quantity) AS total_sales FROM sales AS s JOIN products AS p ON s.pid = p.id GROUP BY DATE(s.created_at) ORDER BY DATE(s.created_at);",
#     curr.execute(querry)
#     data=curr.fetchall()
#     return data
# check email
def check_email(email):
    querry="select * from users where email =%s ;"
    curr.execute(querry,(email,))
    data = curr.fetchone()
    return data
