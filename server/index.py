import json
import logging
import configparser

from flask import Flask
from flask import request
from flask import jsonify

from model import graph

app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
fh = logging.FileHandler('main.log', encoding = 'utf-8')
ch = logging.StreamHandler()
fh.setLevel(logging.DEBUG)
ch.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
app.logger.addHandler(fh)
app.logger.addHandler(ch)

config = configparser.ConfigParser()
config.read('./config.ini', 'utf-8')

host = config['server']['host']
port = config['server']['port']

@app.before_request
def log_info():
    app.logger.info(
        'remote_addr: %s, path: %s, method: %s, args: %s, form: %s' % 
        (
            request.remote_addr, request.path, request.method, 
            json.dumps(request.args, ensure_ascii = False), json.dumps(request.form, ensure_ascii = False)
        )
    )

@app.after_request
def cross_origin(response):
    response.headers['Access-Control-Allow-Origin' ] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST'
    return response

@app.route('/graph', methods = ['GET'], endpoint = 'graph')
def get_graph():
    query = request.args.get('query')
    nodes, edges = graph.get_triple(query)
    return jsonify([nodes, edges])

app.run(host = host, port = port, debug = True)