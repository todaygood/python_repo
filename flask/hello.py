#!/usr/bin/python 

from flask import Flask 

app = Flask(__name__) 

@app.route("/")

def hello():
    return "hello,world"

@app.route("/hello")

def hello_persion():
    return "hello, Margin"

