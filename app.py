#pip install flask
#pip install pyodbc

from flask import Flask, render_template, request, redirect, url_for, flash
import pyodbc
import os

SERVER = os.environ['SERVER']
DATABASE = os.environ['DATABASE']
USERNAME = os.environ['NAME']
PASSWORD = os.environ['PASSWORD']


app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Required for session management (e.g., flashing messages)

# Route to display the review form
@app.route('/')
def index():
    return render_template('review_form.html')

# Route to handle form submissions
@app.route('/submit_review', methods=['POST'])
def submit_review():
    try:
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']
        rating = request.form['rating']

        # Here, you would typically save these data to a database
        # Azure SQL connection string
        connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

        # Establish connection
        conn = pyodbc.connect(connectionString) 

        # Create cursor
        cursor = conn.cursor()

        # Insert data into table
        cursor.execute(
            "INSERT INTO review_table (CustomerName, CustomerEmail, Review, Rating) VALUES (?, ?, ?, ?))",
            name, email, review, rating
        )

        # Commit transaction
        conn.commit()

        print('Data stored successfully')
    
    except Exception as e:
        print(f'Error: {str(e)}')

        # redirect to the thank you page

    return redirect(url_for('thank_you', name=name))

@app.route('/thank_you/<name>')
def thank_you(name):
    return render_template('thank_you.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
