#!/bin/python 

from flask import Flask 

app = Flask(__name__) 

#global tasks
tasks=[1,2]


@app.route("/")
def hello():
    print(tasks)
    tasks.append(8)
    tasks[0]=3

    print(tasks)
    return "hello,world  "+str(tasks)

@app.route("/hello")
def hello_persion():
    print(tasks) 
    tasks.append(4)
    tasks.append(6)

    return "hello, Margin   "+str(tasks)

app.debug=True
app.run(host='0.0.0.0',port=8085,debug=True)
