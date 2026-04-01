from flask import Flask, jsonify, request
import os
import socket
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/mydb')
client = MongoClient(mongo_uri)
db = client.mydb
collection = db.messages

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return f"""
    <html>
        <head><title>Docker App with MongoDB</title></head>
        <body>
            <h1>Hello from Docker Container!</h1>
            <p>Container Hostname: {hostname}</p>
            <p>Environment: {os.getenv('ENV', 'development')}</p>
            <p>MongoDB: Connected</p>
            <hr>
            <h2>Add a message:</h2>
            <form action="/api/message" method="post">
                <input type="text" name="message" placeholder="Enter message">
                <button type="submit">Submit</button>
            </form>
            <h2>Messages:</h2>
            <div id="messages"></div>
            <script>
                fetch('/api/messages')
                    .then(res => res.json())
                    .then(data => {{
                        const messagesDiv = document.getElementById('messages');
                        data.messages.forEach(msg => {{
                            messagesDiv.innerHTML += `<p>${{msg.text}} (ID: ${{msg._id}})</p>`;
                        }});
                    }});
            </script>
        </body>
    </html>
    """

@app.route('/api/messages')
def get_messages():
    messages = list(collection.find({}, {'_id': 1, 'text': 1}))
    for msg in messages:
        msg['_id'] = str(msg['_id'])
    return jsonify({"messages": messages})

@app.route('/api/message', methods=['POST'])
def add_message():
    message = request.form.get('message', '')
    if message:
        result = collection.insert_one({'text': message})
        return jsonify({"id": str(result.inserted_id)})
    return jsonify({"error": "No message provided"}), 400

@app.route('/health')
def health():
    return {"status": "healthy", "mongodb": "connected"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)