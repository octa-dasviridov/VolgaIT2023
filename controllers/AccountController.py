# -*- coding: utf-8 -*-
# Created by Danil Sviridov
# Contact by da_sviridov@octateam.ru


from flask import Blueprint
from flasgger import swag_from


swag_path = 'controllersDescription/AccountController'
account = Blueprint('AccountController', __name__)


@account.route('/Me', methods=['GET'])
@swag_from(f'{swag_path}/me_d.yml')
def me():
    return 'v'


@account.route('/SignIn', methods=['POST'])
@swag_from(f'{swag_path}/signin_d.yml')
def signin():
    return 'v'


@account.route('/SignUp', methods=['POST'])
@swag_from(f'{swag_path}/signup_d.yml')
def signup():
    return 'v'


@account.route('/SignOut', methods=['POST'])
@swag_from(f'{swag_path}/signout_d.yml')
def signout():
    return 'v'


@account.route('/Update', methods=['PUT'])
@swag_from(f'{swag_path}/update_d.yml')
def update():
    return 'v'
