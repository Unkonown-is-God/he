from flask import Flask, jsonify, abort, make_response
import os
app=Flask(__name__)
@app.route("/")
def index():
        return "Hello World! ハローワールド!"
app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 5000)))

