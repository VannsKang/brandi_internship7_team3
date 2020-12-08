import datetime

from flask                   import request, jsonify, Response, g
from flask_request_validator import Param, JSON, Pattern, validate_params
from connection              import get_connection
from utils.exceptions        import ApiError
from utils.validate          import login_validate
from io                      import StringIO
from urllib.parse            import quote


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
                return jsonify({'message': format(e)}), 400
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
                return jsonify({'message': format(e)}), 400
            finally:
                conn.close()

        # 마스터가 셀러 리스트를 보는 페이지
        @app.route("/master/seller_list", methods=['POST'])
        @login_validate
        def seller_info_list():
            conn = None

            try:
                conn = get_connection()
                filter_data = request.get_json()
                data = user_service.get_seller_list(g.user_id, filter_data, conn)

            except KeyError:
                return jsonify({'message': '셀러 정보 조회에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                return jsonify({'message': '셀러 정보 조회에 비어있는 값 전송'}), 400

            except ApiError as e:
                return jsonify({'message': format(e.message)}), e.status_code

            except Exception as e:
                return jsonify({'message': format(e)}), 400

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
                seller_status = user_service.get_seller_status(conn)

            except KeyError:
                return jsonify({'message': '셀러 상태 조회에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                return jsonify({'message': '셀러 상태 조회에 비어있는 값 전송'}), 400

            except ApiError as e:
                return jsonify({'message': format(e.message)}), e.status_code

            except Exception as e:
                return jsonify({'message': format(e)}), 400

            else:
                return jsonify(seller_status), 200

            finally:
                conn.close()

        # 셀러 상태
        @app.route("/update/seller_status", methods=['PUT'])
        @login_validate
        def update_seller_status():
            conn = None

            try:
                conn = get_connection()

                account_info = request.get_json()
                user_service.update_seller_status(account_info, conn)

            except KeyError:
                conn.rollback()
                return jsonify({'message': '셀러 상태 조회에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                conn.rollback()
                return jsonify({'message': '셀러 상태 조회에 비어있는 값 전송'}), 400

            except ApiError as e:
                conn.rollback()
                return jsonify({'message': format(e.message)}), e.status_code

            except Exception as e:
                conn.rollback()
                return jsonify({'message': format(e)}), 400

            else:
                conn.commit()
                return jsonify({'message': 'SUCCESS'}), 200

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

            except ApiError as e:
                return jsonify({'message': format(e.message)}), e.status_code

            except Exception as e:
                return jsonify({'message': format(e)}), 400

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
                created_excel.to_csv(output_stream)

                now_date = datetime.datetime.now().strftime("%Y%m%d")[2:]

                file_name = f"seller_list_{now_date}.csv".format(now_date=now_date)
                file_name = file_name.encode("utf-8")
                url_encoded_file_name = quote(file_name)

                response = Response(
                    output_stream.getvalue(),
                    content_type="text/csv; charset=utf-8",
                    mimetype='text/csv',
                    status=200
                )

                response.headers[
                    "Content-Disposition"
                ] = f"attachment; filename={url_encoded_file_name}; filename*=utf-8''{url_encoded_file_name}"\
                    .format(url_encoded_file_name=url_encoded_file_name)

            except ApiError as e:
                return jsonify({'message': format(e.message)}), e.status_code

            except Exception as e:
                return jsonify({'message': format(e)}), 400

            else:
                output_stream.close()
                return response

            finally:
                conn.close()
                output_stream.close()

        # 셀러 정보 조회/수정
        @app.route("/sellers/<int:seller_id>", methods=['GET', 'PUT'])
        @login_validate
        def seller_detail(seller_id):
            conn = None

            try:
                conn = get_connection()

                if request.method == 'GET':
                    seller = user_service.get_seller_info({'id': seller_id}, conn)
                    return jsonify(seller), 200

                if request.method == 'PUT':
                    seller_images = dict(request.files)
                    seller_info = dict(request.form)
                    seller_info['id'] = seller_id

                    user_service.update_seller_info(seller_info, seller_images, conn)
                    conn.commit()
                    return jsonify({'message': 'SUCCESS'}), 200

            except KeyError:
                conn.rollback()
                return jsonify({'message': '셀러 속성 조회에 유효하지 않은 키 값 전송'}), 400

            except TypeError:
                conn.rollback()
                return jsonify({'message': '셀러 속성 조회에 비어있는 값 전송'}), 400

            except ApiError as e:
                return jsonify({'message': format(e.message)}), e.status_code

            except Exception as e:
                return jsonify({'message': format(e)}), 400

            finally:
                conn.close()

        # NOTE soomyung API search seller result    
        @app.route("/sellers/search", methods=["GET"])
        def get_sellers(): 
            conn = get_connection()
            try:
                filter_data = dict(request.args) 
                filtered_sellers = user_service.get_filtered_sellers(filter_data, conn)
                """request.args looks like
                {
                    user_id: blarblar
                }
                """
            except KeyError:
                return jsonify({'meassa'}), 400
            else:
                return jsonify(filtered_sellers), 200
