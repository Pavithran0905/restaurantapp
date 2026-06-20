from flask import Flask, render_template, request, redirect
import sqlite3
import os
# Project folder-oda absolute path-ah edukkum
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'database.db') # Unga database file peru
app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
def create_table():

    conn = get_db_connection()

    conn.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        price INTEGER,
        image_path TEXT,
        description TEXT
    )
    ''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS reservations (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        restaurant_name TEXT,
        name TEXT,
        date TEXT,
        time TEXT,
        guests INTEGER
    )
    ''')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS orders (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    restaurant_name TEXT,
    quantity INTEGER,
    address TEXT,
    payment TEXT

    )
    ''')
    conn.commit()
    conn.close()
def insert_data():

    conn = get_db_connection()

    for item in items:
     conn.execute('''
     INSERT INTO items ( name, category, price, image_path, description)
     VALUES ( ?, ?, ?, ?, ?)
     ''', (
        item['name'], 
        item['category'], 
        item['price'], 
        item['image_path'], 
        item['description']
      ))
    conn.commit()
    conn.close()
@app.route('/')
def home():
    return render_template('index.html')

# 1. Items List
items = [
    {"id": 1, "name": "Chicken Biryani", "category": "Main Course", "price": 250, "image_path": "Chicken.jpg", "description": "Spicy and delicious"},
    {"id": 2, "name": "Pizza", "category": "Fast Food", "price": 400, "image_path": "pizza.webp", "description": "Cheese loaded pizza"},
    {"id": 3, "name": "Mutton Biriyani", "category": "Main Course", "price": 320, "image_path": "mutton.jpg", "description": "Spicy and delicious"},
    {"id": 4, "name": "Chicken Lollipop", "category": "Fast Food", "price": 200, "image_path": "lollipop.jpg", "description": "Spicy and delicious"},
    {"id": 5, "name": "Burger", "category": "Fast Food", "price": 250, "image_path": "burger.jpg", "description": "Cheese loaded delicious Burger"},
    {"id": 6, "name": "Idly", "category": "Main Course", "price": 100, "image_path": "idly.jpg", "description": "A Traditional South Indian Dish."},
    {"id": 7, "name": "Dosa", "category": "Main Course", "price": 100, "image_path": "dosa.jpg", "description": "Made from a rice, black gram."},
    {"id": 8, "name": "Pongal & Vadai", "category": "Main Course", "price": 80, "image_path": "pongal.jpg", "description": "A Traditional South Indian dish."},
    {"id": 9, "name": "Veg Meals", "category": "Main Course", "price": 150, "image_path": "veg.jpg", "description": "Plant based Dishes"},
    {"id": 10, "name": "Ice Cream", "category": "Creamy Snacks", "price": 120, "image_path": "icecream.jpg", "description": "Creamy and Delicious"},
    {"id": 11, "name": "Tea & Coffee", "category": "Snacks", "price": 50, "image_path": "tea.jpg", "description": "Itz Tea Time..."}
]
    

# 2. Restaurants Data
restaurants_data = {
    1: [{"name": "Thalappakatti", "rating": 4.5, "time": "30 mins", "location":"Ambur"}, {"name": "A2B Bhavan", "rating": 4.2, "time": "25 mins", "location":"Vellore"}, {"name": "SS Hyderabad", "rating": 4.8, "time": "40 mins", "location":"Ambur"}],
    2: [{"name": "Domino's", "rating": 4.1, "time": "20 mins", "location":"Vaniyambadi"}, {"name": "Pizza Hut", "rating": 3.9, "time": "35 mins", "location":"Ponneri"}],
    3: [{"name": "Taj", "rating": 4.5, "time": "30 mins", "location":"Vaniyambadi"}, {"name": "A2D Bhavan", "rating": 4.2, "time": "25 mins", "location":"Ambur"}, {"name": "SS Vaniyambadi", "rating": 4.8, "time": "40 mins", "location":"Vaniyambadi"}],
    4: [{"name": "kaja", "rating": 4.5, "time": "30 mins", "location":"Vaniyambadi"}, {"name": "Hotel Bhavan", "rating": 4.2, "time": "25 mins", "location":"Tirupattur"}, {"name": "SS Hyderabad", "rating": 4.8, "time": "40 mins", "location":"Ambur"}],
    5: [{"name": "McDonald's", "rating": 4.5, "time": "30 mins", "location":"Ambur"}, {"name": "Burger King", "rating": 4.2, "time": "25 mins", "location":"Vellore"}, {"name": "Wendy's", "rating": 4.8, "time": "40 mins", "location":"Tirupattur"}],
    6: [{"name": "Vadamalai Bhavan", "rating": 4.8, "time": "30 mins", "location":"Tirupattur"}, {"name": "Sri Sai Bhavan", "rating": 4.7, "time": "25 mins", "location":"Ambur"}, {"name": "Sri Srinivan", "rating": 4.2, "time": "40 mins", "location":"Ponneri"}],
    7: [{"name": "The Aroma", "rating": 4.6, "time": "30 mins", "location":"Ambur"}, {"name": "Ahmedia", "rating": 3.2, "time": "25 mins", "location":"Vaniyambadi"}, {"name": "Ashok Bhavan", "rating": 4.8, "time": "40 mins", "location":"Vaniyambadi"}],
    8: [{"name": "Saravana Bhavan", "rating": 4.9, "time": "30 mins", "location":"Vaniyambadi"}, {"name": "Ananda Bhavan", "rating": 4.2, "time": "25 mins", "location":"Ambur"}, {"name": "Murugan Hotel", "rating": 3.8, "time": "40 mins", "location":"Ponneri"}],
    9: [{"name": "Sai Bhavan", "rating": 4.7, "time": "30 mins", "location":"Ambur"}, {"name": "Vadamalai Bhavan", "rating": 4.2, "time": "25 mins", "location":"Tirupattur"}, {"name": "Hotel Ananda", "rating": 3.8, "time": "40 mins", "location":"Vellore"}],
    10: [{"name": "The Creamery", "rating": 4.5, "time": "30 mins", "location":"Ambur"}, {"name": "Baskin-Robbins", "rating": 4.2, "time": "25 mins", "location":"Tirupattur"}, {"name": "Arun", "rating": 4.8, "time": "40 mins", "location":"Vaniyambadi"}],
    11: [{"name": "Tea Time", "rating": 4.5, "time": "30 mins", "location":"Vaniyambadi"}, {"name": "Chai Point", "rating": 4.2, "time": "25 mins", "location":"Ambur"}, {"name": "Karuppatti Coffee", "rating": 4.8, "time": "40 mins", "location":"Vellore"}]
}

@app.route('/menu')
def menu():
    return render_template('menu.html', items=items)

@app.route('/item/<int:item_id>')
def item_detail(item_id):
    selected_item = next((item for item in items if item['id'] == item_id), None)
    available_restaurants = restaurants_data.get(item_id, [])
    return render_template('item_detail.html', item=selected_item, restaurants=available_restaurants)

@app.route('/place_order/<string:item_name>/<string:res_name>')
def place_order(item_name, res_name):
    return render_template('order.html', item_name=item_name, res_name=res_name)

@app.route('/confirm_order', methods=['POST'])
def confirm_order():

    if request.method == 'POST':

        item_name = request.form.get('item_name')
        res_name = request.form.get('res_name')
        quantity = request.form.get('quantity')
        address = request.form.get('address')
        payment = request.form.get('payment')

        conn = get_db_connection()

        conn.execute("""
        INSERT INTO orders
        (item_name, restaurant_name, quantity, address, payment)
        VALUES (?, ?, ?, ?, ?)
        """, (
            item_name,
            res_name,
            quantity,
            address,
            payment
        ))

        conn.commit()
        conn.close()

        return render_template(
            'order_success.html',
            item_name=item_name,
            res_name=res_name,
            quantity=quantity,
            address=address,
            payment=payment
        )
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/admin')
def admin_dashboard():
    total_unique_restaurants = 0
    
    if 'restaurants_data' in globals():
        
        unique_names = set()
        
        
        for category_id, restaurant_list in restaurants_data.items():
          
            for restaurant in restaurant_list:
              
                unique_names.add(restaurant['name'])

        total_unique_restaurants = len(unique_names)

    stats = {
        "restaurants_data_count": total_unique_restaurants, 
        "menu_items_count": len(items) if 'items' in globals() else 0
    }
    
    return render_template('admin.html', stats=stats)


@app.route('/admin/reservations')
def admin_reservations():

    conn = get_db_connection()

    all_bookings = conn.execute(
        'SELECT * FROM reservations'
    ).fetchall()

    conn.close()

    return render_template(
        'admin_reservations.html',
        bookings=all_bookings
    )
@app.route('/delete_reservation/<int:id>')
def delete_reservation(id):

    conn = get_db_connection()

    conn.execute(
        'DELETE FROM reservations WHERE id = ?',
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/admin/reservations')
@app.route('/admin/orders')
def admin_orders():

    conn = get_db_connection()

    all_orders = conn.execute(
        'SELECT * FROM orders'
    ).fetchall()

    conn.close()

    return render_template(
        'admin_orders.html',
        orders=all_orders
    )
@app.route('/delete_order/<int:id>')
def delete_order(id):

    conn = get_db_connection()

    conn.execute(
        'DELETE FROM orders WHERE id = ?',
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/admin/orders')

@app.route('/select_restaurant')
def select_restaurant():

    unique_restaurants = []
    seen_names = set()
    
    for res_list in restaurants_data.values():
        for res in res_list:
            if res['name'] not in seen_names:
                seen_names.add(res['name'])
                unique_restaurants.append(res)
                

    return render_template('restaurants.html', restaurants=unique_restaurants)



@app.route('/reservation', methods=['GET', 'POST'])
def reservation():

    if request.method == 'POST':

        restaurant_name = request.form.get('restaurant_name')
        name = request.form.get('name')
        date = request.form.get('date')
        time = request.form.get('time')
        guests = request.form.get('guests')

        conn = get_db_connection()

        conn.execute("""
        INSERT INTO reservations
        (restaurant_name, name, date, time, guests)
        VALUES (?, ?, ?, ?, ?)
        """, (restaurant_name, name, date, time, guests))

        conn.commit()
        conn.close()

        return render_template(
            'booking_success.html',
            restaurant_name=restaurant_name,
            name=name,
            date=date,
            time=time,
            guests=guests
        )

    selected_restaurant = request.args.get('restaurant', '')

    return render_template(
        'reservation.html',
        restaurant_name=selected_restaurant
    )

if __name__ == '__main__':
    create_table()
    insert_data()
    app.run(debug=True)