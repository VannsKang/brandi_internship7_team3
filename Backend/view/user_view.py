from flask      import request, jsonify
from connection import get_connection


class SellerView:
    # noinspection PyMethodMayBeStatic
    def create_endpoints(app, services):
        seller_service = services.user_service

        # 마스터가 셀러 리스트를 보는 페이지
        @app.route("/master/seller_list", methods=['GET'])
        # decorator master
        def seller_list():
            conn = None

            try:
                conn = get_connection()
                filter_data = dict(request.args)

                data = seller_service.get_seller_list(filter_data, conn)

            except KeyError:
                return jsonify({'message' : '셀러 정보 조회에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                return jsonify({'message' : '셀러 정보 조회에 비어있는 값 전송'}), 400

            except Exception as e:
                return jsonify({'message' : 'error {}'.format(e)}), 400

            else:
                return jsonify(data), 200

            finally:
                conn.close()

        # 셀러 상태
        @app.route("/seller_status", methods=['GET'])
        def seller_status_list():
            conn = None

            try:
                conn = get_connection()
                seller_status = seller_service.get_seller_status(conn)

            except KeyError:
                return jsonify({'message': '셀러 상태 조회에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                return jsonify({'message': '셀러 상태 조회에 비어있는 값 전송'}), 400

            except Exception as e:
                return jsonify({'message': 'error {}'.format(e)}), 400

            else:
                return jsonify(seller_status), 200

            finally:
                conn.close()

        # 셀러 속성
        @app.route("/seller_attributes", methods=['GET'])
        def seller_attributes_list():
            conn = None

            try:
                conn = get_connection()
                seller_attributes = seller_service.get_seller_attributes(conn)

            except KeyError:
                return jsonify({'message': '셀러 속성 조회에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                return jsonify({'message': '셀러 속성 조회에 비어있는 값 전송'}), 400

            except Exception as e:
                return jsonify({'message': 'error {}'.format(e)}), 400

            else:
                return jsonify(seller_attributes), 200

            finally:
                conn.close()

        # 액션을 통한 셀러 상태 변경
        @app.route("/seller_status", methods=['PUT'])
        # decorator master
        def update_seller_status():
            conn = None

            try:
                conn = get_connection()
                account_info = request.json

                seller_service.update_seller_status(account_info, conn)

            except KeyError:
                conn.rollback()
                return jsonify({'message': '셀러 상태 변경에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                conn.rollback()
                return jsonify({'message': '셀러 상태 변경에 비어있는 값 전송'}), 400

            except Exception as e:
                conn.rollback()
                return jsonify({'message': 'error {}'.format(e)}), 400

            else:
                conn.commit()
                return jsonify({'message': 'SUCCESS'}), 200

            finally:
                conn.close()
