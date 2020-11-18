import time

from flask import Flask, request, render_template
from pprint import pformat

app = Flask(__name__)

@app.route("/")
def hello_world():
    ts = time.time()

    axlist = [
        {
            "ts": ts,
            "remote_addr": request.remote_addr,
            "method": request.method,
            "path": request.path,
        }
    ]

    return render_template("accesslist.html", axlist=axlist)
