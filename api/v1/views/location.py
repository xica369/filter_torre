#!/usr/bin/python3
"""filter to location that handles all default RestFul API actions"""

from api.v1.views.validate import __CONNECTIONS__
from api.v1.views import app_views
from flask import jsonify, abort, request
import requests
import sys

conections = __CONNECTIONS__
filter_location = []

@app_views.route("/location/<location>", methods=['GET'])
def location_filter(location):
    "filter to location"

    for conect in conections:
        url = "https://torre.bio/api/bios/{}".format(conect['publicId'])
        resp = requests.get(url).json()

        if resp.get('person').get('location'):
            if location.lower() in resp['person']['location']['name'].lower():
                filter_location.append(conect)

    conections.clear()
    conections.extend(filter_location)
    return jsonify(filter_location), 200
