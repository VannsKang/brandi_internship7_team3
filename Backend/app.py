import config
import pymysql

from flask      import Flask, jsonify
from flask_cors import CORS

from model      import user_dao
from service    import user_service
from view       import user_view


class Services:
    pass


def create_app(test_config=None):
    app = Flask(__name__)
    app.debug = True

    CORS(app, resources={r'*': {'origins': '*'}})

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    # Persistence Layer
    seller_dao = user_dao.SellerDao()

    # Business Layer
    services = Services
    services.user_service = user_service.SellerService(seller_dao, config)

    # Endpoint
    user_view.SellerView.create_endpoints(app, services)

    @app.errorhandler(Exception)
    def handle_error(error):
        return jsonify(error.error_response)

    return app
