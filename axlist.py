import time

from flask import Flask, request
from pprint import pformat

app = Flask(__name__)

@app.route("/")
def hello_world():
    ts = time.time()

    response = ["hello world!", "", ""]
    response.append(f"time: {ts}")
    response.append(f"remote_addr: {request.remote_addr}")
    response.append(f"method: {request.method}")
    response.append(f"path: {request.path}")

    return "<br>".join(response)
