from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is my API!"

@app.route("/api/data")
def get_data():
    return jsonify({
        "name": "Your Name",
        "message": "Welcome to my API",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)
