#Some changes done by my to check the monmgodb connectivity
from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

db_connection_status = "Not connected to MongoDB"
try:
    mongodb_uri = os.environ.get("MONGODB_URI", "mongodb://mongodb-service:27017/")
    client = MongoClient(mongodb_uri)
    client.admin.command('ping')
    db_connection_status = "Connected to MongoDB successfully!"
    print("Connected to MongoDB successfully!")  # Log to terminal
except Exception as e:
    db_connection_status = f"Failed to connect to MongoDB: {e}"
    print(f"Failed to connect to MongoDB: {e}")  # Log to terminal

db = client.flask_db
collection = db.data

@app.route('/')
def index():
    return f"Welcome to the Flask app! The current time is: {datetime.now()}. {db_connection_status}"

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        data = request.get_json()
        collection.insert_one(data)
        return jsonify({"status": "Data inserted"}), 201
    elif request.method == 'GET':
        data = list(collection.find({}, {"_id": 0}))
        return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
