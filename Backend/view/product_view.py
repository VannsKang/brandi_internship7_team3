from flask                   import request, jsonify, Response
from flask_request_validator import Param, GET, JSON, Pattern, validate_params
from connection              import get_connection
from utils.exceptions        import ApiError
from utils.validate          import login_validate


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
            try:
                conn = get_connection()
                get_product_list_result = product_service.get_products(filter_data, conn)
                if get_product_list_result:
                    return jsonify({'message': 'SUCCESS',
                                    'product_list': get_product_list_result['product_list'],
                                    'product_count': get_product_list_result['product_count']}), 200
                else:
                    return jsonify({'message': 'SUCCESS',
                                    'product_list': [],
                                    'product_count': 0}), 200
            except Exception as e:
                return jsonify({'message': format(e)}), 500
            finally:
                conn.close()

        # NOTE soomyung API search color result
        @app.route("/products/colors", methods=["GET"])
        def get_colors():
            conn = get_connection()
            try:
                colors = product_service.get_colors(conn)

            except KeyError:
                return jsonify({'message'}), 404
            else:
                return jsonify(colors), 200
            finally:
                conn.close()

        # NOTE soomyung API search sizes result    
        @app.route("/products/sizes", methods=["GET"])
        def get_sizes():
            conn = get_connection()
            try:
                sizes = product_service.get_sizes(conn)

            except KeyError:
                return jsonify({'message'}), 404
            else:
                return jsonify(sizes), 200
            finally:
                conn.close()

        # NOTE soomyung API get first categories     
        @app.route("/products/first_categories", methods=["GET"])
        def get_first_categories():
            conn = get_connection()
            try:
                first_categories = product_service.get_first_categories(conn)

            except KeyError:
                return jsonify({'message'}), 404
            else:
                return jsonify(first_categories), 200
            finally:
                conn.close()

        # NOTE soomyung API get second categories     
        @app.route("/products/second_categories", methods=["GET"])
        def get_second_categories():
            conn = get_connection()
            try:
                first_category_id = dict(request.args)
                second_categories = product_service.get_second_categories(first_category_id, conn)

            except KeyError:
                return jsonify({'message'}), 404
            else:
                return jsonify(second_categories), 200
            finally:
                conn.close()

        # NOTE soomyung API post new product
        @app.route("/products/new", methods=["POST"])
        def add_new_product():

            conn = get_connection()

            try:
                product_info = request.get_json()
                new_product = product_service.add_new_product(product_info, conn)

            except KeyError:
                conn.rollback()
                return jsonify({'message': '상품 정보에 유효하지 않은 키 값 전송'}), 404
            except TypeError:
                return jsonify({'message': '셀러 속성 조회에 비어있는 값 전송'}), 400
            except Exception as e:
                return jsonify({'message': 'error {}'.format(e)}), 500
            except ApiError as e:
                conn.rollback()
                return jsonify({'message': format(e.message)}), e.status_code

            else:
                conn.commit()
                return jsonify({'message': '생성 성공'}), 201
                # return jsonify(new_product), 200
            finally:
                conn.close()
