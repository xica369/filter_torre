#!/usr/bin/python3
""" Initialize Blueprint """

from flask import Blueprint


app_views = Blueprint("mold", __name__, url_prefix='/api/v1')


from api.v1.views.index import *
from api.v1.views.validate import *
from api.v1.views.language import *
from api.v1.views.education import *
from api.v1.views.strength import *
from api.v1.views.location import *
from api.v1.views.person import *
from api.v1.views.clear import *
