#!/bin/python3
from celery_module import app
 
if __name__ == '__main__':
    app.debug=True
    app.run(debug=True)
