# -*- coding: utf-8 -*-
# Created by Danil Sviridov
# Contact by da_sviridov@octateam.ru


import controllers

from config import mode
from flask import Flask
from flasgger import Swagger
from flask_cors import CORS


app = Flask(__name__)
app.config.from_pyfile('config.py')
swagger = Swagger(app)
CORS(app)

app.register_blueprint(controllers.AccountController.account, url_prefix='/api/AccountController')
app.register_blueprint(controllers.AdminAccountController.admin_account, url_prefix='/api/AdminAccountController')
app.register_blueprint(controllers.TransportController.transport, url_prefix='/api/TransportController')
app.register_blueprint(controllers.AdminTransportController.admin_transport, url_prefix='/api/AdminTransportController')
app.register_blueprint(controllers.RentController.rent, url_prefix='/api/RentController')
app.register_blueprint(controllers.AdminRentController.admin_rent, url_prefix='/api/AdminRentController')
if mode:
    print('abab')
    app.register_blueprint(controllers.PaymentController.payment, url_prefix='/api/PaymentController')


if __name__ == '__main__':
    app.run(debug=mode)
