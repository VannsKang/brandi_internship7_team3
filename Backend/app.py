import config

from flask      import Flask, jsonify
from flask_cors import CORS

from model.user_dao          import UserDao
from model.product_dao       import ProductDao
from service.user_service    import UserService
from service.product_service import ProductService
from view.user_view          import UserView
from view.product_view       import ProductView
from utils.exceptions        import ApiError


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
    user_dao = UserDao()
    product_dao = ProductDao()

    # Business Layer
    services = Services
    services.user_service = UserService(user_dao, config)
    services.product_service = ProductService(product_dao, config)

    # Endpoint
    UserView.create_endpoints(app, services)
    ProductView.create_endpoints(app, services)

    @app.errorhandler(Exception)
    def handle_error(error):
        if type(error) is ApiError:
            return jsonify({'message': 'error {}'.format(error.message)}), error.status_code
        return jsonify({'message': 'error {}'.format(error)}), 400
    return app
