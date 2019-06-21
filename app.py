from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def postNgrokAddress():
    if request.method == "GET":
        if readAddr() == "":
            return "Fatal: your address is not provided yet."
        return readAddr()
    elif request.method == "POST":
        if not request.data:
            return "Fatal: your address is not provided."
        data = request.data.decode('utf-8')
        data = json.loads(data)
        requests.get(data['url'] + '/' + data['path'])
        return "success"
