#!/usr/bin/python3
"""filter to education that handles all default RestFul API actions"""

from api.v1.views.validate import __CONNECTIONS__
from api.v1.views import app_views
from flask import jsonify, abort, request
import requests
import sys

this = sys.modules[__name__]
conections = __CONNECTIONS__
filter_education = []

@app_views.route("/education/<edu>", methods=['GET'])
def education_filter(edu):
    "filter to education"

    for conect in conections:
        url = "https://torre.bio/api/bios/{}".format(conect['publicId'])
        resp = requests.get(url).json()
        for education in resp['education']:
            if edu.lower() in education["name"].lower():
                filter_education.append(conect)
                break

    conections.clear()
    conections.extend(filter_education)
    return jsonify(filter_education), 200
