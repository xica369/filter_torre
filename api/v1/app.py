#!/usr/bin/python3
"""
starts a Flask web application:
web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, jsonify
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

# Cross-Origin Resource Sharing
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.errorhandler(404)
def errot_notfound(message):
    """ handler for 404 errors """
    resp = jsonify({"error": "Not found"})
    resp.status_code = 404
    return resp

if __name__ == '__main__':
    app.run(port=int(getenv("API_PORT")),
            host=getenv("API_HOST"), threaded=True)
