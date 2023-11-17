from flask import Flask

app = Flask(__name__)

@app.route("/first")
def main():
    return "This is the first API, but we're using something else!"
