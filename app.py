from flask import Flask

app = Flask(__name__)

@app.route("/second")
def main():
    return "This is the second API!"
