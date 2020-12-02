import pymysql
import datetime
from utils.exceptions import InsertFailError


class UserDao:
    # 회원가입 정보 저장
    def sign_up_account(self, user_data, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sign_up_sql = """
            INSERT INTO accounts (
                user_id,
                class_id
            ) VALUES (
                %(user_id)s, 
                2    
            )
            """
            sign_up_result = cursor.execute(sign_up_sql, user_data)
            if not sign_up_result:
                raise InsertFailError('회원가입 실패', 400)
            account_id = cursor.lastrowid

            user_data['account_id'] = account_id

            insert_seller_info = """
                INSERT INTO seller_info (
                    account_id,
                    seller_attribute_id,
                    modifier_id,
                    password,
                    owner_number,
                    name,
                    eng_name,
                    cs_number
                ) VALUES (
                    %(account_id)s,
                    %(seller_attribute_id)s,
                    (select class_id from accounts where account_id = %(account_id)s),
                    %(password1)s,
                    %(owner_number)s,
                    %(name)s,
                    %(eng_name)s,
                    %(cs_number)s
                )
                """
            seller_info_result = cursor.execute(insert_seller_info, user_data)
            if not seller_info_result:
                raise InsertFailError('회원가입 실패', 400)
            return seller_info_result

    # 사용자 정보 존재 여부 조회
    def get_user(self, user_data, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT
                    * 
                FROM
                    accounts 
                WHERE
                    user_id=%(user_id)s
                """
            cursor.execute(sql, user_data)
            get_user_result = cursor.fetchone()
            return get_user_result

    # 셀러 정보 조회
    def get_seller_info(self, user_data, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT
                    accounts.user_id,
                    seller_info.password
                FROM
                    accounts
                INNER JOIN
                    seller_info ON accounts.account_id = seller_info.account_id
                WHERE
                    accounts.user_id=%(user_id)s
                """
            cursor.execute(sql, user_data)
            get_seller_info_result = cursor.fetchone()
            return get_seller_info_result

    # noinspection PyMethodMayBeStatic
    def get_seller_list(self, filter_data, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
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
                    sa.seller_action AS seller_action,
                    sa.seller_action_id AS seller_action_id
                FROM seller_info AS s
                INNER JOIN accounts AS ac ON s.account_id = ac.account_id
                INNER JOIN seller_status AS ss ON s.seller_status_id = ss.seller_status_id
                INNER JOIN seller_attributes AS sat ON s.seller_attribute_id = sat.seller_attribute_id
                LEFT JOIN (SELECT 
                            GROUP_CONCAT(sa.name) AS seller_action, 
                            GROUP_CONCAT(sa.seller_action_id) AS seller_action_id, 
                            ssa.status_id
                        FROM seller_status_actions AS ssa
                        INNER JOIN seller_actions AS sa ON ssa.action_id = sa.seller_action_id
                        GROUP BY ssa.status_id) sa ON s.seller_status_id = sa.status_id
                
                WHERE end_date='9999-12-31' AND is_deleted=0
            """

            if 'id' in filter_data and filter_data['id']:
                query += ' AND ac.account_id = %(id)s'

            if 'seller_id' in filter_data and filter_data['seller_id']:
                query += ' AND ac.user_id = %(seller_id)s'

            if 'eng_name' in filter_data and filter_data['eng_name']:
                query += ' AND s.eng_name = %(eng_name)s'

            if 'kor_name' in filter_data and filter_data['kor_name']:
                query += ' AND s.name = %(kor_name)s'

            if 'owner_name' in filter_data and filter_data['owner_name']:
                query += ' AND s.owner_name = %(owner_name)s'

            if 'seller_status_id' in filter_data and filter_data['seller_status_id']:
                query += ' AND ss.seller_status_id = %(seller_status_id)s'

            if 'phone_number' in filter_data and filter_data['phone_number']:
                query += ' AND s.owner_number = %(phone_number)s'

            if 'email' in filter_data and filter_data['email']:
                query += ' AND s.owner_email = %(email)s'

            if 'seller_attribute_id' in filter_data and filter_data['seller_attribute_id']:
                query += ' AND sat.seller_attribute_id = %(seller_attribute_id)s'

            if 'start_time' in filter_data \
                    and 'end_time' in filter_data \
                    and filter_data['start_time'] \
                    and filter_data['end_time']:
                end_time = datetime.datetime.strptime(filter_data['end_time'], '%Y-%m-%d')
                filter_data['end_time'] = (end_time + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
                query += ' AND (ac.created_at >= %(start_time)s AND ac.created_at < %(end_time)s)'

            elif 'start_time' in filter_data and filter_data['start_time']:
                query += ' AND ac.created_at >= %(start_time)s'

            elif 'end_time' in filter_data and filter_data['end_time']:
                end_time = datetime.datetime.strptime(filter_data['end_time'], '%Y-%m-%d')
                filter_data['end_time'] = (end_time + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
                query += ' AND ac.created_at < %(end_time)s'

            if 'sort_type' in filter_data and filter_data['sort_type']:
                if '-id' == filter_data['sort_type']:
                    query += ' ORDER BY -ac.account_id'
                elif 'id' == filter_data['sort_type']:
                    query += ' ORDER BY ac.account_id'
            else:
                query += ' ORDER BY -ac.account_id'

            if 'offset' in filter_data and 'limit' in filter_data:
                filter_data['offset'] = int(filter_data['offset'])
                filter_data['limit'] = int(filter_data['limit'])
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
    
                WHERE end_date='9999-12-31' AND is_deleted=0
            """

            if 'id' in filter_data and filter_data['id']:
                query += ' AND ac.account_id = %(id)s'

            if 'seller_id' in filter_data and filter_data['seller_id']:
                query += ' AND ac.user_id = %(seller_id)s'

            if 'eng_name' in filter_data and filter_data['eng_name']:
                query += ' AND s.eng_name = %(eng_name)s'

            if 'kor_name' in filter_data and filter_data['kor_name']:
                query += ' AND s.name = %(kor_name)s'

            if 'owner_name' in filter_data and filter_data['owner_name']:
                query += ' AND s.owner_name = %(owner_name)s'

            if 'seller_status_id' in filter_data and filter_data['seller_status_id']:
                query += ' AND ss.seller_status_id = %(seller_status_id)s'

            if 'phone_number' in filter_data and filter_data['phone_number']:
                query += ' AND s.owner_number = %(phone_number)s'

            if 'email' in filter_data and filter_data['email']:
                query += ' AND s.owner_email = %(email)s'

            if 'seller_attribute_id' in filter_data and filter_data['seller_attribute_id']:
                query += ' AND sat.seller_attribute_id = %(seller_attribute_id)s'

            if 'start_time' in filter_data \
                    and 'end_time' in filter_data \
                    and filter_data['start_time'] \
                    and filter_data['end_time']:
                end_time = datetime.datetime.strptime(filter_data['end_time'], '%Y-%m-%d')
                filter_data['end_time'] = (end_time + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
                query += ' AND (ac.created_at >= %(start_time)s AND ac.created_at < %(end_time)s)'

            elif 'start_time' in filter_data and filter_data['start_time']:
                query += ' AND ac.created_at >= %(start_time)s'

            elif 'end_time' in filter_data and filter_data['end_time']:
                end_time = datetime.datetime.strptime(filter_data['end_time'], '%Y-%m-%d')
                filter_data['end_time'] = (end_time + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
                query += ' AND ac.created_at < %(end_time)s'

            if 'sort_type' in filter_data and filter_data['sort_type']:
                if '-id' == filter_data['sort_type']:
                    query += ' ORDER BY -ac.account_id'
                elif 'id' == filter_data['sort_type']:
                    query += ' ORDER BY ac.account_id'
            else:
                query += ' ORDER BY -ac.account_id'

            seller_count = cursor.execute(query, filter_data)

            if not seller_count:
                raise Exception("seller Data 없음")

            return cursor.fetchone()

    # noinspection PyMethodMayBeStatic
    def get_seller_status(self, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT 
                    seller_status_id,
                    name
                FROM seller_status
            """

            seller_status = cursor.execute(query)

            if not seller_status:
                raise Exception("seller status Data 없음")

            return cursor.fetchall()

    # noinspection PyMethodMayBeStatic
    def get_seller_attributes(self, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT 
                    seller_attribute_id,
                    name
                FROM seller_attributes
            """

            seller_attributes = cursor.execute(query)

            if not seller_attributes:
                raise Exception("seller attributes Data 없음")

            return cursor.fetchall()

    # noinspection PyMethodMayBeStatic
    def get_seller_action_to_status(self, account_info, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT 
                    sas.status_id AS seller_status_id
                FROM seller_action_to_status AS sas
                RIGHT JOIN seller_actions AS sa ON sas.action_id = sa.seller_action_id
                WHERE sa.seller_action_id = %(seller_action_id)s
            """

            seller_status = cursor.execute(query, account_info)

            if not seller_status:
                raise Exception("유효하지 않은 액션 값 전송")
            return cursor.fetchone()

    # noinspection PyMethodMayBeStatic
    def get_now_time(self, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT now() AS now
            """)

            return cursor.fetchone()

    # noinspection PyMethodMayBeStatic
    def get_seller(self, seller_info, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT
                    seller_info_id AS seller_info_id,
                    account_id AS id,
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
                FROM seller_info
                WHERE end_date = '9999-12-31'
                AND account_id = %(id)s
            """

            seller_info = cursor.execute(query, seller_info)

            if not seller_info:
                raise Exception("seller Data 없음")

            return cursor.fetchone()

    # noinspection PyMethodMayBeStatic
    def insert_seller_info(self, seller_info, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
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
                )
                VALUES (    
                    %(id)s,
                    %(seller_status_id)s,
                    %(seller_attribute_id)s,
                    %(modifier_id)s,
                    %(is_deleted)s,
                    %(password)s,
                    %(now)s,
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

            insert_seller_info_check = cursor.execute(query, seller_info)

            if not insert_seller_info_check:
                raise Exception('셀러 상태 정보 갱신 실패')

            return insert_seller_info_check

    # noinspection PyMethodMayBeStatic
    def update_seller_info(self, seller_info, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                UPDATE seller_info
                SET end_date = %(now)s
                WHERE seller_info_id = %(seller_info_id)s            
            """

            update_seller_info = cursor.execute(query, seller_info)

            if not update_seller_info:
                raise Exception('이전 셀러 정보 이력 업데이트 실패')

            return update_seller_info
