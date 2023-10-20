# -*- coding: utf-8 -*-
# Created by Danil Sviridov
# Contact by da_sviridov@octateam.ru


from flask import Blueprint
from flasgger import swag_from


swag_path = 'controllersDescription/TransportController'
transport = Blueprint('TransportController', __name__)