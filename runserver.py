#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
import os


app = Flask(__name__)

app.config['SERVER_NAME'] = os.environ.get('SERVER_NAME')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
