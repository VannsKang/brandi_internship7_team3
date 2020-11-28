import pymysql


class SellerDao:
    # noinspection PyMethodMayBeStatic
    def get_seller_list(self, filter_data, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:

            filter_data['offset'] = int(filter_data['offset'])
            filter_data['limit'] = int(filter_data['limit'])

            query = """
                SELECT 
                    ac.account_id    AS id,
                    ac.user_id       AS seller_id,
                    s.eng_name       AS eng_name,
                    s.name           AS kor_name,
                    ss.name          AS seller_status,
                    sat.name         AS seller_attribute,
                    s.owner_name     AS owner_name,
                    s.owner_number   AS phone_number,
                    s.owner_email    AS email,
                    ac.created_at    AS created_at,
                    sa.seller_action AS seller_action
                FROM seller_info AS s
                INNER JOIN accounts AS ac ON s.account_id = ac.account_id
                INNER JOIN seller_status AS ss ON s.seller_status_id = ss.seller_status_id
                INNER JOIN seller_attributes AS sat ON s.seller_attribute_id = sat.seller_attribute_id
                LEFT JOIN (SELECT GROUP_CONCAT(sa.name) AS seller_action, ssa.status_id
                            FROM seller_status_actions AS ssa
                            INNER JOIN seller_actions AS sa ON ssa.action_id = sa.seller_action_id
                            GROUP BY ssa.status_id) sa ON s.seller_status_id = sa.status_id
                
                WHERE end_date='9999-12-31 AND is_deleted=0'
            """

            if 'id' in filter_data:
                query += ' AND ac.account_id = %(id)s'

            if 'seller_id' in filter_data:
                query += ' AND ac.user_id = %(seller_id)s'

            if 'eng_name' in filter_data:
                query += ' AND s.eng_name = %(eng_name)s'

            if 'kor_name' in filter_data:
                query += ' AND s.name = %(kor_name)s'

            if 'owner_name' in filter_data:
                query += ' AND s.owner_name = %(owner_name)s'

            if 'status' in filter_data:
                query += ' AND ss.seller_status_id = %(status)s'

            if 'owner_number' in filter_data:
                query += ' AND s.owner_number = %(owner_number)s'

            if 'owner_email' in filter_data:
                query += ' AND s.owner_email = %(owner_email)s'

            if 'attribute' in filter_data:
                query += ' AND sat.seller_attribute_id = %(attribute)s'

            if 'start_time' in filter_data and 'end_time' in filter_data:
                query += ' AND (ac.created_at BETWEEN %(start_time)s AND %(end_time)s)'
            elif 'start_time' in filter_data:
                query += ' AND ac.created_at >= %(start_time)s'
            elif 'end_time' in filter_data:
                query += ' AND ac.created_at <= %(end_time)s'

            query += ' LIMIT %(offset)s, %(limit)s'

            sellers = cursor.execute(query, filter_data)

            if not sellers:
                raise Exception("seller Data 없음")

            return cursor.fetchall()

    # noinspection PyMethodMayBeStatic
    def get_seller_count(self, filter_data, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT 
                    COUNT(*) AS count
                FROM seller_info AS s
                INNER JOIN accounts AS ac ON s.account_id = ac.account_id
                INNER JOIN seller_status AS ss ON s.seller_status_id = ss.seller_status_id
                INNER JOIN seller_attributes AS sat ON s.seller_attribute_id = sat.seller_attribute_id
                LEFT JOIN (SELECT GROUP_CONCAT(sa.name) AS seller_action, ssa.status_id
                            FROM seller_status_actions AS ssa
                            INNER JOIN seller_actions AS sa ON ssa.action_id = sa.seller_action_id
                            GROUP BY ssa.status_id) sa ON s.seller_status_id = sa.status_id
    
                WHERE end_date='9999-12-31 AND is_deleted=0'
            """

            if 'attribute' in filter_data:
                query += ' AND sat.seller_attribute_id = %(attribute)s'

            if 'status' in filter_data:
                query += ' AND ss.seller_status_id = %(status)s'

            seller_count = cursor.execute(query, filter_data)

            if not seller_count:
                raise Exception("seller Data 없음")

            return cursor.fetchone()

    # noinspection PyMethodMayBeStatic
    def get_seller_attributes(self, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT *
                FROM seller_attributes
            """

            seller_attributes = cursor.execute(query)

            if not seller_attributes:
                raise Exception("seller attributes Data 없음")

            return cursor.fetchall()

    # noinspection PyMethodMayBeStatic
    def update_seller_status(self, account_info, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:

            # 현재 시간 가져오기
            cursor.execute("""
                SELECT now()
            """)

            # 현재 시간 저장
            now = cursor.fetchone()
            account_info['now'] = now['now()']

            previous_seller_info_query = """
                SELECT
                    account_id,
                    seller_status_id,
                    seller_attribute_id,
                    modifier_id,
                    is_deleted,
                    password,
                    name,
                    eng_name,
                    cs_number,
                    owner_name,
                    owner_number,
                    owner_email,
                    seller_profile,
                    seller_background,
                    seller_intro,
                    seller_detail,
                    zipcode,
                    first_address,
                    last_address,
                    open_time,
                    close_time,
                    delivery,
                    refund
                FROM seller_info
                WHERE end_date = '9999-12-31'
                AND account_id = %(account_id)s
            """

            # 가장 최근 셀러 정보 확인
            previous_seller_info_check = cursor.execute(previous_seller_info_query, account_info)

            # 해당 셀러 정보가 없을 시 에러처리
            if not previous_seller_info_check:
                raise Exception("seller Data 없음")

            # 가장 최근 셀러 정보 가져옴
            previous_seller_info = cursor.fetchone()

            insert_seller_info_query = """
                INSERT INTO seller_info (
                    account_id,
                    seller_status_id,
                    seller_attribute_id,
                    modifier_id,
                    is_deleted,
                    password,
                    start_date,
                    name,
                    eng_name,
                    cs_number,
                    owner_name,
                    owner_number,
                    owner_email,
                    seller_profile,
                    seller_background,
                    seller_intro,
                    seller_detail,
                    zipcode,
                    first_address,
                    last_address,
                    open_time,
                    close_time,
                    delivery,
                    refund
                VALUES (    
                    %(account_id)s,
                    %(seller_status_id)s,
                    %(seller_attribute_id)s,
                    %(modifier_id)s,
                    %(is_deleted)s,
                    %(password)s,
                    %(now)s
                    %(name)s,
                    %(eng_name)s,
                    %(cs_number)s,
                    %(owner_name)s,
                    %(owner_number)s,
                    %(owner_email)s,
                    %(seller_profile)s,
                    %(seller_background)s,
                    %(seller_intro)s,
                    %(seller_detail)s,
                    %(zipcode)s,
                    %(first_address)s,
                    %(last_address)s,
                    %(open_time)s,
                    %(close_time)s,
                    %(delivery)s,
                    %(refund)s
                )
             """

            # 수정할 셀러 정보를 갱신
            account_info = dict(previous_seller_info, **account_info)

            # 수정 내용이 적용된 셀러 정보를 생성
            cursor.execute(insert_seller_info_query, account_info)

            update_previous_seller_info = """
                UPDATE seller_info
                SET end_date = %(now)s
                WHERE seller_info_id = %(previous_seller_info_id)s
            """

            # 이전 셀러 정보의 end_date 를 현재 시간으로 수정
            cursor.execute(update_previous_seller_info, previous_seller_info)

            return cursor.fetchone()
