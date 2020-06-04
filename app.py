from flask import Flask, jsonify, abort, make_response
app=Flask(__name__)
@app.route("/")
def index():
        return "Hello World! ハローワールド!"
app.run(port=3000)
