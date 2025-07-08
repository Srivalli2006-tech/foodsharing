from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB_NAME = 'donations.db'

@app.route('/')
def home():
    return render_template('donate.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Collect data from form
    name = request.form['name']
    phone = request.form['phone']
    description = request.form['description']
    address = request.form['address']
    pickup_time = request.form['pickup_time']

    # Save to SQLite database
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            INSERT INTO donations (name, phone, description, address, pickup_time)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, phone, description, address, pickup_time))

    return redirect('/thankyou')

@app.route('/thankyou')
def thankyou():
    return "<h2>Thank you for your donation!</h2>"

# Run the server
if __name__ == '__main__':
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS donations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone TEXT,
                description TEXT,
                address TEXT,
                pickup_time TEXT
            )
        ''')
    app.run(debug=True)
