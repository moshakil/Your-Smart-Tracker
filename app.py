from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB URI 
mongo_uri = "mongodb+srv://shakil:<Shakil12>@cluster0.sjvbflf.mongodb.net/?retryWrites=true&w=majority"

# Create a MongoClient instance
mongo_client = MongoClient(mongo_uri)

# Access MongoDB database 
db = mongo_client.Cluster0

# Define MongoDB collections
users_collection = db.users
vehicles_collection = db.vehicles

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Insert the user data into the MongoDB 'users' collection
        users_collection.insert_one({
            'username': username,
            'password': password
        })

        flash('Registration successful', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for vehicle maintenance scheduling
@app.route('/vehicles', methods=['GET', 'POST'])
def vehicles():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']

        # Insert the vehicle data into the MongoDB 'vehicles' collection
        vehicles_collection.insert_one({
            'make': make,
            'model': model,
            'year': year
        })

        flash('Vehicle added', 'success')
    return render_template('vehicles.html')

# Route for the root URL
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
