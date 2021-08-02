from flask import Flask

import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('./config.ini', 'utf-8')

host = config['server']['host']
port = config['server']['port']

@app.route('/')
def hello():
    return 'Hello World'

app.run(host = host, port = port, debug = True)