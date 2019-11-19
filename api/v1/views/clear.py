#!/usr/bin/python3
"""clear the list CONNECTIONS"""

from api.v1.views.validate import __CONNECTIONS__
from api.v1.views import app_views
from flask import jsonify, abort, request
import requests
import sys


@app_views.route("/clear", methods=['GET'])
def location_clear():
    "clear the list CONNECTIONS"

    __CONNECTIONS__.clear()
    return jsonify({"message": "clean list"}), 200
