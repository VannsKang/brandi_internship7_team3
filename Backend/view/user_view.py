from flask                   import request, jsonify
from flask_request_validator import Param, JSON, Pattern, validate_params
from connection              import get_connection
from service.user_service    import UserService, SellerService
from utils.exceptions        import ApiError


class UserView:

    def create_endpoints(app, service):
        user_service = service.user_service

        @app.route('/sign-up', methods=['POST'])
        @validate_params(
            Param('user_id', JSON, str, rules=[Pattern(r'[a-zA-Z0-9]')]),
            Param('password1', JSON, str),
            Param('password2', JSON, str),
            Param('seller_attribute_id', JSON, int),
            Param('owner_number', JSON, str),
            Param('name', JSON, str, rules=[Pattern(r'[ㄱ-힣a-zA-Z0-9]')]),
            Param('eng_name', JSON, str, rules=[Pattern(r'[a-zA-Z0-9]')]),
            Param('cs_number', JSON, str, rules=[Pattern(r'\d{2,3}-\d{3,4}-\d{4}')])
        )
        # 회원가입
        def sign_up(*args):
            conn = None
            user_data = {
                'user_id': args[0],
                'password1': args[1],
                'password2': args[2],
                'seller_attribute_id': args[3],
                'owner_number': args[4],
                'name': args[5],
                'eng_name': args[6],
                'cs_number': args[7]
            }
            try:
                conn = get_connection()
                sign_up_result = user_service.sign_up_account(user_data, conn)
                if sign_up_result:
                    conn.commit()
                    return jsonify({'message': 'SUCCESS'}), 201
            except ApiError as e:
                conn.rollback()
                return jsonify({'message': format(e.message)}), e.status_code
            except Exception as e:
                conn.rollback()
                return jsonify({'message': format(e)}), 500
            finally:
                conn.close()

        @app.route('/sign-in', methods=['POST'])
        @validate_params(
            Param('user_id', JSON, str, rules=[Pattern(r'[a-zA-Z0-9]')]),
            Param('password', JSON, str,
                  rules=[Pattern(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,20}$')])
        )
        # 로그인
        def sign_in(*args):
            conn = None
            user_data = {
                'user_id': args[0],
                'password': args[1]
            }
            try:
                conn = get_connection()
                sign_in_seller = user_service.sign_in_seller(user_data, conn)
                if sign_in_seller:
                    return sign_in_seller
            except ApiError as e:
                return jsonify({'message': format(e.message)}), e.status_code
            except Exception as e:
                return jsonify({'message': 'error {}'.format(e)}), 500
            finally:
                conn.close()


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

                updated_seller = seller_service.update_seller_status(account_info, conn)

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
