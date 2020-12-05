import datetime

from flask                   import request, jsonify, Response
from flask_request_validator import Param, JSON, Pattern, validate_params
from connection              import get_connection
from utils.exceptions        import ApiError
from io                      import StringIO


class UserView:

    def create_endpoints(app, service):
        user_service = service.user_service

        @app.route('/sign-up', methods=['POST'])
        @validate_params(
            Param('user_id', JSON, str, rules=[Pattern(r'[a-zA-Z0-9]')]),
            Param('password', JSON, str),
            Param('confirm_password', JSON, str),
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
                'password': args[1],
                'confirm_password': args[2],
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
                return jsonify({'message': 'error {}'.format(e)}), 400
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
                return jsonify({'message': 'error {}'.format(e)}), 400
            finally:
                conn.close()

        # 마스터가 셀러 리스트를 보는 페이지
        @app.route("/master/seller_list", methods=['POST'])
        # decorator master
        def seller_info_list():
            conn = None

            try:
                conn = get_connection()
                filter_data = request.get_json()

                data = user_service.get_seller_list(filter_data, conn)

            except KeyError:
                return jsonify({'message': '셀러 정보 조회에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                return jsonify({'message': '셀러 정보 조회에 비어있는 값 전송'}), 400

            except Exception as e:
                return jsonify({'message': 'error {}'.format(e)}), 400

            else:
                return jsonify(data), 200

            finally:
                conn.close()

        # 셀러 상태
        @app.route("/seller_status", methods=['GET', 'PUT'])
        def seller_status_list():
            conn = None

            try:
                conn = get_connection()

                if request.method == 'GET':
                    seller_status = user_service.get_seller_status(conn)
                    return jsonify(seller_status), 200

                if request.method == 'PUT':
                    account_info = request.get_json()
                    user_service.update_seller_status(account_info, conn)
                    return jsonify({'message': 'SUCCESS'}), 200

            except KeyError:
                return jsonify({'message': '셀러 상태 조회에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                return jsonify({'message': '셀러 상태 조회에 비어있는 값 전송'}), 400

            except Exception as e:
                return jsonify({'message': 'error {}'.format(e)}), 400

            finally:
                conn.close()

        # 셀러 속성
        @app.route("/seller_attributes", methods=['GET'])
        def seller_attributes_list():
            conn = None

            try:
                conn = get_connection()
                seller_attributes = user_service.get_seller_attributes(conn)

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

        @app.route("/seller_info/download", methods=['POST'])
        def seller_info_list_download():
            conn = None
            output_stream = None

            try:
                conn = get_connection()
                filter_data = request.get_json()
                seller_info = user_service.get_seller_list(filter_data, conn)

                created_excel = user_service.create_excel_seller_info(seller_info)

                output_stream = StringIO()
                # output_stream.write(u'\ufeff')
                created_excel.to_csv(output_stream)

                now_date = datetime.datetime.now().strftime("%Y%m%d")[2:]

                response = Response(
                    output_stream.getvalue(),
                    content_type="text/csv; charset=utf-8",
                )
                response.headers["Content-Disposition"] = "attachment; filename=seller_list_{now_date}.csv" \
                    .format(now_date=now_date)

            except Exception as e:
                return jsonify({'message': 'error {}'.format(e)}), 400

            else:
                output_stream.close()
                return response, 200

            finally:
                conn.close()
                output_stream.close()

        # 셀러 정보 조회/수정
        @app.route("/sellers/<int:seller_id>", methods=['GET', 'PUT'])
        def seller_detail(seller_id):
            conn = None
            seller = None

            try:
                conn = get_connection()

                if request.method == 'GET':
                    seller = user_service.get_seller_info({'id': seller_id}, conn)

                if request.method == 'PUT':
                    account_info = request.get_json()
                    conn.commit()
                    seller = user_service.update_seller_info(account_info, conn)

            except KeyError:
                return jsonify({'message': '셀러 속성 조회에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                return jsonify({'message': '셀러 속성 조회에 비어있는 값 전송'}), 400

            except Exception as e:
                return jsonify({'message': 'error {}'.format(e)}), 400

            else:
                return jsonify(seller), 200

            finally:
                conn.close()

        @app.route("/upload/image", methods=['POST'])
        def seller_image_upload():
            conn = None

            try:
                conn = get_connection()
                seller_image = request.files
                user_service.upload_seller_image(seller_image, conn)

            except KeyError:
                return jsonify({'message': '이미지 업로드에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                return jsonify({'message': '업로드 할 파일이 없습니다.'}), 400

            except Exception as e:
                return jsonify({'message': 'error {}'.format(e)}), 400

            else:
                return jsonify({'message': 'SUCCESS'}), 200

            finally:
                conn.close()
