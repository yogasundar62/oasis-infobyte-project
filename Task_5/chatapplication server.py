from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chat-secret'
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('send_message')
def handle_message(data):
    print(f"Received: {data}")
    try:
        username = data['username']
        message = data['message']
        emit('receive_message', {'username': username, 'message': message}, broadcast=True)
    except Exception as e:
        print(f"Error handling message: {e}")
        emit('error', {'error': str(e)})

@app.route('/')
def home():
    return "Chat server is running!"

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5050)
