from flask import Flask, jsonify, abort, make_response
import os
import craft

app = Flask(__name__)
sum=0
@app.route("/")
def main():
    sum+=1
    print(sum)


app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
