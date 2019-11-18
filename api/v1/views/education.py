#!/usr/bin/python3
"""filter to education that handles all default RestFul API actions"""

from api.v1.views.validate import __CONECTIONS__
from api.v1.views import app_views
from flask import jsonify, abort, request
import requests

conections = __CONECTIONS__
filter_education = []

@app_views.route("/education/<edu>", methods=['GET'])
def education_filter(edu):
    "filter to education"

    filter_education.clear()
    for conect in conections:
        url = "https://torre.bio/api/bios/{}".format(conect['publicId'])
        resp = requests.get(url).json()
        for education in resp['education']:
            if edu.lower() in education["name"].lower():
                filter_education.append(conect)
    return jsonify(filter_education), 200
