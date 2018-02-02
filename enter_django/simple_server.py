#!/usr/bin/env python

from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']

app=make_server('127.0.0.1',8000,simple_app)
app.serve_forever()
