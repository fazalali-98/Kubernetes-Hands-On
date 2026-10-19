
from flask import Flask, jsonify

app = Flask(__name__)

# Return basic information about the REST API.
@app.route("/about", methods=["GET"])
def about():
    return jsonify({
        "name": "Simple REST API",
        "version": "1.0",
        "description": "This is a simple REST API built with Flask."
    })

if __name__ == "__main__":
    # Listen on all interfaces so Docker can forward requests to the app.
    app.run(host="0.0.0.0", port=5001)
