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

# profits function
def total_profit():
    query = 'select p.name,p.id, sum((p.selling_price - p.buying_price) * s.quantity) as total_profit from products as p join sales as s on p.id = s.pid group by p.name, p.id;'
    curr.execute(query)
    profit = curr.fetchall()
    return profit

# sales function
def total_sales():
    query = 'select p.name,p.id,sum(p.selling_price * s.quantity) as total_sales from products as p join sales as s on p.id =s.pid group by p.name,p.id'
    curr.execute(query)
    sales = curr.fetchall()
    return sales
