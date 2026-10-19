
from flask import Flask, request
import socket
import time
import random

app = Flask(__name__)

# Show the welcome message and identify the Pod handling the request.
@app.get("/")
def homepage():
    return {
        "message": "Welcome to Big Sale!",
        "pod": socket.gethostname(),
        "ts": time.time()
    }

# Simulate a customer buying a random product during the sale.
@app.get("/buy")
def buy():
    item = random.choice(
        ["Smartphone", "Shoes", "Headphones", "Laptop"]
    )
    user = request.args.get(
        "user", f"user{random.randint(1, 1000)}"
    )

    return {
        "status": "success",
        "item": item,
        "user": user,
        "served_by_pod": socket.gethostname(),
        "time": time.strftime("%H:%M:%S")
    }

# Kubernetes uses this endpoint to check application health.
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "pod": socket.gethostname()
    }
