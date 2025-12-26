from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Served from pod: {socket.gethostname()} — Deployed automatically by Jenkins CI/CD!"

app.run(host="0.0.0.0", port=5000)
