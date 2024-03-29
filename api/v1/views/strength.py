#!/usr/bin/python3
"""filter to strength that handles all default RestFul API actions"""

from api.v1.views.validate import __CONNECTIONS__
from api.v1.views import app_views
from flask import jsonify, abort, request
import requests
import sys

conections = __CONNECTIONS__
filter_strength = []

@app_views.route("/strength/<strength>", methods=['GET'])
def strength_filter(strength):
    "filter to education"

    for conect in conections:
        url = "https://torre.bio/api/bios/{}".format(conect['publicId'])
        resp = requests.get(url).json()
        for stren in resp['strengths']:
            if strength.lower() in stren["name"].lower():
                filter_strength.append(conect)
                break
    conections.clear()
    conections.extend(filter_strength)
    return jsonify(filter_strength), 200
