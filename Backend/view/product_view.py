from flask                   import request, jsonify, Response
from flask_request_validator import Param, JSON, Pattern, validate_params
from connection              import get_connection
from utils.exceptions        import ApiError



class ProductView:

    def create_endpoints(app, service):
        product_service = service.product_service

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
                return jsonify({'message': '상품 등록에 유효하지 않은 키 값 전송'}), 404
            except TypeError:
<<<<<<< Updated upstream
                return jsonify({'message': '셀러 속성 조회에 비어있는 값 전송'}), 400
            except Exception as e:
                return jsonify({'message': 'error {}'.format(e)}), 500
=======
                return jsonify({'message': '상품 등록을 위한 값에 비어있는 값 전송'}), 400
>>>>>>> Stashed changes
            except ApiError as e:
                conn.rollback()
                return jsonify({'message': format(e.message)}), e.status_code
            
            else:
                conn.commit()
                return jsonify({'message': '생성 성공'}), 201
                # return jsonify(new_product), 200
            
            finally:
                conn.close()
