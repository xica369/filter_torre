#!/usr/bin/python3
"""velidate user name and save publicId to conections
that handles all default RestFull API actions"""

from api.v1.views import app_views
from flask import jsonify, abort, request
import requests
import sys

this = sys.modules[__name__]

__CONNECTIONS__ = []

@app_views.route("/validate/<username>", methods=['GET'])
def validate_username(username):
    "validate the user name and save the publicId to conections"
    __CONNECTIONS__.clear()
    print(id(__CONNECTIONS__))
    url = 'https://bio.torre.co/api/people/{}/connections'.format(username)
    res = requests.get(url).json()

    if type(res) is dict and res.get('message') == "Person not found!":
        return jsonify({'message': "Person not found!"}), 400
    else:
        bio_url = 'https://bio.torre.co/api/bios/{}'.format(username)
        bio_res = requests.get(bio_url).json()
        for conect in res:
            info_conect = {
                "name": conect['person']['name'],
                "publicId": conect['person']['publicId']
            }
            __CONNECTIONS__.append(info_conect)
        print(id(__CONNECTIONS__))
        info = {
            "username": bio_res['person']['name'],
            "conections": __CONNECTIONS__
            }
        return jsonify(info), 200
