
from flask import Flask

app = Flask(__name__)

# This route responds when someone opens the home page.
@app.route("/")
def home():
    return "Hello from Flask on Kubernetes!"

if __name__ == "__main__":
    # Listen on all interfaces so Kubernetes can reach the app.
    app.run(host="0.0.0.0", port=15000)
