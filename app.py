# A simple Flask application that returns the hostname of the pod
# it is running in, along with a message indicating it was deployed
# automatically by Jenkins CI/CD.        

from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Served from pod: {socket.gethostname()} — Deployed automatically by Jenkins CI/CD!"

app.run(host="0.0.0.0", port=5000)
