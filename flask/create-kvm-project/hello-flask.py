#!/bin/python 

from flask import Flask 

app = Flask(__name__) 

@app.route("/")
def hello():
    return "hello,world"

@app.route("/hello")
def hello_persion():
    return "hello, Margin"


app.run(host='0.0.0.0',port=8085,debug=True)
