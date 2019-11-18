#!/usr/bin/python3
"""filter to language that handles all default RestFul API actions"""

from api.v1.views.validate import __CONECTIONS__
from api.v1.views import app_views
from flask import jsonify, abort, request
import requests

conections = __CONECTIONS__
filter_language = []

@app_views.route("/language/<lang>", methods=['GET'])
def language_filter(lang):
    "filter to language"

    filter_language.clear()
    for conect in conections:
        url = "https://torre.bio/api/bios/{}".format(conect['publicId'])
        resp = requests.get(url).json()
        for language in resp['languages']:
            if language["language"] == lang:
                filter_language.append(conect)
    return jsonify(filter_language), 200
