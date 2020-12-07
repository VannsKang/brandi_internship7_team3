import datetime

from flask import request, jsonify, Response
from flask_request_validator import Param, GET, JSON, Pattern, validate_params
from connection import get_connection
from utils.exceptions import ApiError
from utils.validate import login_validate


class ProductView:

    def create_endpoints(app, service):
        product_service = service.product_service

        @app.route('/master/product_list', methods=['GET'])
        # @login_validate
        @validate_params(
            Param('start_date', GET, str, required=False,
                  rules=[Pattern(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))")]),
            Param('end_date', GET, str, required=False,
                  rules=[Pattern(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))")]),
            Param('seller_name', GET, str, required=False),
            Param('product_name', GET, str, required=False),
            Param('product_code', GET, str, required=False),
            Param('product_number', GET, int, required=False),
            Param('seller_attribute_id', GET, list, required=False),
            Param('offset', GET, int),
            Param('limit', GET, int),
            Param('sell_info', GET, bool, required=False),
            Param('show_info', GET, bool, required=False),
            Param('discount_info', GET, bool, required=False)
        )
        def get_product_list(*args):
            conn = None
            filter_data = {
                'start_date': args[0],
                'end_date': args[1],
                'seller_name': args[2],
                'product_name': args[3],
                'product_code': args[4],
                'product_number': args[5],
                'seller_attribute_id': args[6],
                'offset': args[7],
                'limit': args[8],
                'sell_info': args[9],
                'show_info': args[10],
                'discount_info': args[11]
            }
            print(1)
            try:
                conn = get_connection()
                get_product_list_result = product_service.get_products(filter_data, conn)
                if get_product_list_result:
                    conn.commit()
                    return jsonify({'message': 'SUCCESS',
                                    'product_list': get_product_list_result['product_list'],
                                    'product_count': get_product_list_result['product_count']}), 200
                else:
                    return jsonify({'message': 'SUCCESS',
                                    'product_list': [],
                                    'product_count': 0}), 200
            except ApiError as e:
                conn.rollback()
                return jsonify({'message': format(e.message)}), e.status_code
            except Exception as e:
                conn.rollback()
                return jsonify({'message': 'error {}'.format(e)}), 500
            finally:
                conn.close()
