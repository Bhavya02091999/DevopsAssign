from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym!"})

@app.route('/plans')
def plans():
    return jsonify({
        "plans": [
            {"name": "Basic", "price": 500},
            {"name": "Standard", "price": 1000},
            {"name": "Premium", "price": 1500}
        ]
    })

@app.route('/trainers')
def trainers():
    return jsonify({
        "trainers": ["Alice", "Bob", "Charlie"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
