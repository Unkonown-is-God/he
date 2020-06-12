from flask import Flask, jsonify, abort, make_response
import os
from unmo import Unmo


app=Flask(__name__)
@app.route("/")
def main():
        return jsonify("hello")

app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))