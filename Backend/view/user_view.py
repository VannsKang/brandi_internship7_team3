import datetime

from flask      import request, jsonify, Response
from connection import get_connection
from openpyxl   import Workbook


class SellerView:
    # noinspection PyMethodMayBeStatic
    def create_endpoints(app, services):
        seller_service = services.user_service

        # 마스터가 셀러 리스트를 보는 페이지
        @app.route("/master/seller_list", methods=['POST'])
        # decorator master
        def seller_info_list():
            conn = None

            try:
                conn = get_connection()
                filter_data = request.get_json()

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
                print(account_info)
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

        @app.route("/seller_info/download", methods=['POST'])
        def seller_info_list_download():
            conn = None
            work_book = None

            try:
                conn = get_connection()
                filter_data = request.get_json()
                # filter_data = dict(request.args)
                data = seller_service.get_seller_list(filter_data, conn)

                work_book = Workbook()
                excel_write = work_book.active

                columns = (
                    '번호',
                     '셀러번호',
                     '관리자계정ID',
                     '셀러영문명',
                     '셀러한글명',
                     '담당자명',
                     '담당자연락처',
                     '담당자이메일',
                     '셀러속성',
                     '셀러등록일',
                     '승인여부',
                )

                excel_write.append(columns)

                seller_list = [
                    {
                        index + 1,
                        seller['id'],
                        seller['seller_id'],
                        seller['eng_name'],
                        seller['kor_name'],
                        seller['seller_attribute'],
                        seller['owner_name'],
                        seller['phone_number'],
                        seller['email'],
                        seller['created_at'],
                        seller['seller_status']
                    } for index, seller in enumerate(data['data'])]

                [excel_write.append(row) for row in seller_list]

                now_date = datetime.datetime.now().strftime("%Y%m%d")[2:]

                response = Response(
                    work_book,
                    content_type="text/csv; charset=utf-8"
                )
                response.headers["Content-Disposition"] = "attachment; filename=seller_list_{now_date}"\
                    .format(now_date=now_date)

            except Exception as e:
                return jsonify({'message': 'error {}'.format(e)}), 400

            else:
                return response, 200

            finally:
                conn.close()
                work_book.close()

        # 셀러 정보 조회/수정
        @app.route("/seller_my_page/<int:seller_id>", methods=['POST', 'PUT'])
        def seller_detail():
            conn = None
            seller = None

            try:
                conn = get_connection()

                if request.method == 'POST':
                    seller = seller_service.get_seller_attributes(conn)

                if request.method == 'PUT':
                    seller = seller_service.update_seller(conn)

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
