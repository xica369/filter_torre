#!/usr/bin/python3
"""look to person that handles all default RestFul API actions"""


from api.v1.views import app_views
from flask import jsonify, abort, request
import requests


@app_views.route("/person/<publicId>", methods=['GET'])
def person_filter(publicId):
    "basic information about the person"
    education = []
    strengths = []
    languages = []
    location = []

    url = "https://torre.bio/api/bios/{}".format(publicId)
    resp = requests.get(url).json()

    "save education"
    for edu in resp["education"]:
        education.append(edu["name"])

    "save strenths"
    for stren in resp["strengths"]:
        strengths.append(stren["name"])

    "save languages"
    for lang in resp["languages"]:
        languages.append(lang["language"])

    "save location"
    if resp.get("person").get("location"):
        location.append(resp.get("person").get("location").get("name"))

    person = {
        "name": resp.get("person").get("name"),
        "profesionalHeadline": resp.get("person").get("profesionalHeadline"),
        "summaryOfBio": resp.get("person").get("summaryOfBio"),
        "education": education,
        "strengths": strengths,
        "languages": languages,
        "location": location
    }
    return jsonify(person), 200
