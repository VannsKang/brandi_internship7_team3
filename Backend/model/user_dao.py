import pymysql


class SellerDao:
    def get_seller_list(self, filter_data, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT 
                ac.account_id    AS id,
                ac.user_id       AS seller_id,
                s.eng_name       AS eng_name,
                s.name           AS kor_name,
                ss.name          AS seller_status,
                sa.name          AS seller_attribute,
                s.owner_number   AS phone_number,
                s.owner_email    AS email,
                ac.created_at    AS created_at
            FROM seller_info AS s
            INNER JOIN accounts AS ac ON s.account_id = ac.account_id
            INNER JOIN seller_status AS ss ON s.seller_status_id = ss.seller_status_id
            INNER JOIN seller_attributes AS sa ON s.seller_attribute_id = sa.seller_attribute_id
                        
            WHERE end_date='9999-12-31'
            LIMIT %(offset)s, %(limit)s
            """

            filter_data['offset'] = int(filter_data['offset'])
            filter_data['limit'] = int(filter_data['limit'])
            seller_list = cursor.execute(query, filter_data)

            if not seller_list:
                raise Exception("seller Data 존재하지 않음")

            return cursor.fetchall()

    def get_seller_count(self, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT COUNT(*) AS count
            FROM seller_info
            WHERE end_date='9999-12-31'
            """

            seller_count = cursor.execute(query)

            if not seller_count:
                raise Exception("seller Data 존재하지 않음")

            return cursor.fetchone()

    def get_seller_attributes(self, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT *
            FROM seller_attributes
            """

            seller_attributes = cursor.execute(query)

            if not seller_attributes:
                raise Exception("seller attributes Data 존재하지 않음")

            return cursor.fetchall()
