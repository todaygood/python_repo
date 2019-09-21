#!/usr/bin/python

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)


person('Bob',35,city='Beijing')



from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()



