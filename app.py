from flask import Flask, jsonify, abort, make_response
import os
import craft

app=Flask(__name__)
@app.route("/<key>",methods=["GET"])
def main(key):
        return jsonify(craft.apimode(key))

app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
