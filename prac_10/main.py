from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"  # Use return, not print


if __name__ == '__main__':
    app.run(debug=True)  # Include parentheses to run the app
