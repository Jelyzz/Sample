from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="Voluntary"
)

# Create cursor
cursor = conn.cursor()

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Insert data into MySQL
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

