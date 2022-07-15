from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return 'hello world'


@app.route("/home")
def health():
    return 'home page'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
