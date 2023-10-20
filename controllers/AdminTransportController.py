# -*- coding: utf-8 -*-
# Created by Danil Sviridov
# Contact by da_sviridov@octateam.ru


from flask import Blueprint
from flasgger import swag_from


swag_path = 'controllersDescription/AdminTransportController'
admin_transport = Blueprint('AdminTransportController', __name__)