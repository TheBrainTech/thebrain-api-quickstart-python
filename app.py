import os
import requests
import json

from flask import Flask, render_template, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

apiKey = os.getenv("API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    return render_template("index.html")


@socketio.on('submit_form')
def handle_form_submission(data):
    brainId = data['brainId']
    thtName = data['thtName']
    kind = 1
    thtLabel = data['thtLabel']
    typeId = None
    srcThtId = data['srcThtId']
    relation = 1
    acType = 0

    url = f'https://api.bra.in/thoughts/{brainId}'
    headers = {
        'Authorization': f'Bearer {apiKey}',
        'Content-Type': 'application/json'
    }
    body = {
        'name': thtName,
        'kind': kind,
        'label': thtLabel,
        'typeId': typeId,
        'sourceThoughtId': srcThtId,
        'relation': relation,
        'acType': acType
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        response_data = response.json()
        newThoughtId = response_data
        socketio.emit('form_response', {'message': f'Success! New Thought ID: {newThoughtId}'})
    else:
        errorMessage = response.text
        socketio.emit('form_response', {'message': f'Error: {response.text}'})
