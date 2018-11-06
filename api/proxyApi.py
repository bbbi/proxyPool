# -*- coding: utf-8 -*-
import sys

from flask import Flask, request, url_for, redirect, render_template, jsonify

from dbs.redisClient import RedisRefreshClient,RedisInitClient
from settings import API_HOST, API_PORT

app = Flask(__name__,
            # static_folder="api/static"
            )

sys.path.append('..')
db = RedisRefreshClient()
init_db = RedisInitClient()


@app.route(r'/', methods=['GET'])
def index():
    http_count = db.count('http')
    https_count = db.count('https')
    init_count = init_db.count()
    context = {
        'http_count': http_count,
        'https_count': https_count,
        'init_count':init_count
    }

    return render_template('index.html', **context)


@app.route(r'/get', methods=['GET'])
def get():
    scheme = request.args.get('scheme', '')
    if scheme == 'http':
        item = db.random(scheme)
        return jsonify(item)
    elif scheme == 'https':
        item = db.random(scheme)
        return jsonify(item)
    else:
        url = url_for('index')

        return redirect(url)


@app.route(r'/count', methods=['GET'])
def count():
    scheme = request.args.get('scheme', '')
    if scheme == 'http':
        count = db.count(scheme)
        return str(count)
    elif scheme == 'https':
        count = db.count(scheme)
        return str(count)
    elif scheme == 'init_':
        count = init_db.count()
    else:
        url = url_for('index')

        return redirect(url)


def api_run():
    app.run(host=API_HOST, port=API_PORT)


if __name__ == '__main__':
    api_run()
