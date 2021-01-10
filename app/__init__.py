# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.timer_controller import api as timer_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='TVMAZE',
          version='1.0',
          description='API for TVMAZE'
          )
api.add_namespace(timer_ns, path='/timers')