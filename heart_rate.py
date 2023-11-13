from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
heart_rate = {
    "heart_id": "01234",
    "date": "November 13, 2023",
    "heart_rate": "43",
}

@app.route("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
