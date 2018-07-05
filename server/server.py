from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import os
import functions as fs


app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')

@socketio.on('convert')
def handle_source(json_data):
    text = fs.convert((json_data['message'].encode()))
    socketio.emit('echo', {'echo': str(text)})

if __name__ == "__main__":
    socketio.run(app)
