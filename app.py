from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def postNgrokAddress():
    if request.method == "GET":
        if readAddr() == "":
            return "Fatal: your address is not provided yet."
        return readAddr()
    elif request.method == "POST":
        if not request.data:
            return "Fatal: your address is not provided."
        writeAddr(request.data.decode())
        return "success"

def writeAddr(addr):
    with open("./address.txt", "w") as f:
        f.write(addr)
        return True

def readAddr():
    addr = ""
    try:
        with open("./address.txt") as f:
            addr = f.read()
    except:
        return ""
    return addr
