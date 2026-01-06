from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    # Run the app on localhost port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
