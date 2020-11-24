from flask      import request, jsonify
from connection import get_connection


class SellerView:
    def create_endpoints(app, services):
        seller_service = services.user_service

        # 마스터가 셀러 리스트를 보는 페이지
        @app.route("/master/seller_list", methods=['GET'])
        def master_seller_list():
            conn = None
            data = None

            try:
                conn = get_connection()
                filter_data = dict(request.args)

                if request.method == 'GET':
                    data = seller_service.get_seller_list(filter_data, conn)

            except KeyError:
                conn.rollback()
                return jsonify({'message' : 'KEY ERROR'}), 400

            except TypeError:
                conn.rollback()
                return jsonify({'message' : 'TYPE ERROR'}), 400

            except Exception as e:
                conn.rollback()
                return jsonify({'message' : 'error {}'.format(e)}), 400

            else:
                conn.commit()
                return jsonify(data), 200

            finally:
                conn.close()

        # 셀러 속성
        @app.route("/seller_attributes", methods=['GET'])
        def seller_attributes_list():
            conn = None
            seller_attributes = None

            try:
                conn = get_connection()

                if request.method == 'GET':
                    seller_attributes = seller_service.get_seller_attributes(conn)

            except KeyError:
                conn.rollback()
                return jsonify({'message': 'KEY ERROR'}), 400

            except TypeError:
                conn.rollback()
                return jsonify({'message': 'TYPE ERROR'}), 400

            except Exception as e:
                conn.rollback()
                return jsonify({'message': 'error {}'.format(e)}), 400

            else:
                conn.commit()
                return jsonify(seller_attributes), 200

            finally:
                conn.close()
