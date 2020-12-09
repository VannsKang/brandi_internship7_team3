import pymysql
from flask import g
from utils.exceptions import InsertFailError


class ProductDao:
    # 상품 리스트 표출
    def get_products(self, filter_data, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            # if g.user_id:
                sql = """
                    SELECT
                        pi.start_date  AS created_at,     
                        img.image_url  AS thumbnail, 
                        pi.name        AS name,
                        p.product_code AS code,
                        pi.number      AS number,
                        sa.name        AS seller_attribute,
                        si.name        AS seller_name,
                        pi.price       AS price,
                        pi.discount    AS discount,
                        pi.sell_info   AS sell_info,
                        pi.show_info   AS show_info,
                        pi.sale_info   AS sale_info
                                                             
                    FROM product_info AS pi
                    
                    #상품 코드
                    LEFT JOIN products AS p
                    ON p.product_id = pi.product_id
                    
                    #셀러 이름  
                    LEFT JOIN seller_info AS si
                    ON si.seller_info_id = pi.seller_id
                    
                    #셀러 속성
                    LEFT JOIN seller_attributes AS sa
                    ON sa.seller_attribute_id = si.seller_attribute_id
                    
                    #상품 대표이미지
                    LEFT JOIN product_images AS img
                    ON img.product_info_id = pi.product_id
                    
                    WHERE
                    #삭제 여부 확인
                    pi.is_deleted = 0
                    AND si.is_deleted = 0
                    #AND img.is_deleted = 0
                    
                    #최신 정보로 제한
                    AND pi.end_date = '9999-12-31 00:00:00'
                    AND si.end_date = '9999-12-31 00:00:00'
                    #AND img.end_date = '9999-12-31 00:00:00'
                    
                    #사진 이미지 제한
                    #AND img.image_order_id = 1
                    """

                # 조회기간 시작
                if filter_data.get('start_date', None):
                    sql += " AND pi.start_date > %(start_date)s"

                # 조회기간 종료
                if filter_data.get('end_date', None):
                    sql += " AND pi.start_date < %(end_date)s"

                # 셀러명
                if filter_data.get('seller_name', None):
                    sql += " AND si.name = %(seller_name)s"

                # 상품명
                if filter_data.get('product_name', None):
                    sql += " AND pi.name = %(product_name)s"

                # 상품번호
                if filter_data.get('product_number', None):
                    sql += " AND pi.number = %(product_number)s"

                # 상품코드
                if filter_data.get('product_code', None):
                    sql += " AND p.code = %(product_code)s"

                # 셀러 속성
                if filter_data.get('seller_attribute_id', None):
                    sql += " AND sa.seller_attribute_id in %(seller_attribute_id)s"

                # 판매여부
                if filter_data.get('sell_info', None) is not None:
                    sql += " AND pi.sell_info = %(sell_info)s"

                # 진열여부
                if filter_data.get('show_info', None) is not None:
                    sql += " AND pi.show_info = %(show_info)s"

                # 할인여부
                if filter_data.get('sale_info', None) is not None:
                    sql += " AND pi.sale_info = %(sale_info)s"

                sql += " ORDER BY pi.start_date DESC"

                # 페이지네이션
                if filter_data.get('limit', None) and filter_data.get('offset', None):
                    filter_data['limit'] = int(filter_data['limit'])
                    filter_data['offset'] = int(filter_data['offset'])
                    sql += " LIMIT %(offset)s, %(limit)s"

                cursor.execute(sql, filter_data)
                product_list = cursor.fetchall()

                # 상품 개수 가져오기
                sql = """
                    SELECT COUNT(*) AS product_count
    
                    FROM product_info AS pi
                    
                    #상품 코드
                    LEFT JOIN products AS p
                    ON p.product_id = pi.product_id
                    
                    #셀러 이름  
                    LEFT JOIN seller_info AS si
                    ON si.seller_info_id = pi.seller_id
                    
                    #셀러 속성
                    LEFT JOIN seller_attributes AS sa
                    ON sa.seller_attribute_id = si.seller_attribute_id
                    
                    #상품 대표이미지
                    LEFT JOIN product_images AS img
                    ON img.product_info_id = pi.product_id
                    
                    WHERE
                    #삭제 여부 확인
                    pi.is_deleted = 0
                    AND si.is_deleted = 0
                    #AND img.is_deleted = 0
                    
                    #최신 정보로 제한
                    AND pi.end_date = '9999-12-31 00:00:00'
                    AND si.end_date = '9999-12-31 00:00:00'
                    #AND img.end_date = '9999-12-31 00:00:00'
                    
                    #사진 이미지 제한
                    #AND img.image_order_id = 1
                    """

                # 조회기간 시작
                if filter_data.get('start_date', None):
                    sql += " AND pi.start_date > %(start_date)s"

                # 조회기간 종료
                if filter_data.get('end_date', None):
                    sql += " AND pi.start_date < %(end_date)s"

                # 셀러명
                if filter_data.get('seller_name', None):
                    sql += " AND si.name = %(seller_name)s"

                # 상품명
                if filter_data.get('product_name', None):
                    sql += " AND pi.name = %(product_name)s"

                # 상품번호
                if filter_data.get('product_number', None):
                    sql += " AND pi.number = %(product_number)s"

                # 상품코드
                if filter_data.get('product_code', None):
                    sql += " AND p.code = %(product_code)s"

                # 셀러 속성
                if filter_data.get('seller_attribute_id', None):
                    sql += " AND sa.seller_attribute_id in %(seller_attribute_id)s"

                # 판매여부
                if filter_data.get('sell_info', None) is not None:
                    sql += " AND pi.sell_info = %(sell_info)s"

                # 진열여부
                if filter_data.get('show_info', None) is not None:
                    sql += " AND pi.show_info = %(show_info)s"

                # 할인여부
                if filter_data.get('sale_info', None) is not None:
                    sql += " AND pi.sale_info = %(sale_info)s"

                cursor.execute(sql, filter_data)
                product_count = cursor.fetchone()

                return {'product_list': product_list, 'product_count': product_count}

    def get_colors(self, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT * FROM colors
            """

            # NOTE show every color in the list
            colors = cursor.execute(query)

            if not colors:
                raise Exception("검색 결과 없음")

            return cursor.fetchall()

    def get_sizes(self, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT * FROM sizes
            """

            # NOTE show every size in the list
            sizes = cursor.execute(query)

            if not sizes:
                raise Exception("검색 결과 없음")

            return cursor.fetchall()

    def get_first_categories(self, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT * FROM first_categories
            """

            # NOTE show every first categories in the list
            first_categories = cursor.execute(query)

            if not first_categories:
                raise Exception("검색 결과 없음")

            return cursor.fetchall()

    def get_second_categories(self, first_category_id, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            print(first_category_id)
            query = """
                SELECT
                    s.first_category_id AS first_category_id,
                    s.second_category_id,
                    s.name
                FROM second_categories AS s
                WHERE first_category_id = %(first_category_id)s
            """

            # NOTE show every second categories in the list
            second_categories = cursor.execute(query, first_category_id)

            if not second_categories:
                raise Exception("검색 결과 없음")

            return cursor.fetchall()

    def add_new_product(self, product_info, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            products_query = """
                INSERT INTO products(
                    creater_id
                )
                VALUES (
                    %(creater_id)s
                )
                """
            option_info_data = product_info['option_info']
            product_info["option_info"] = None
            products_query_result = cursor.execute(products_query, product_info)
            if not products_query_result:
                raise InsertFailError('생성 실패', 400)
            product = cursor.lastrowid
            # NOTE productid auto increment => productid /creatorID => modifier ID same data
            product_info['product_id'] = product
            product_info['modifier_id'] = product_info['creater_id']

            search_most_updated = """
                SELECT product_option_number FROM product_options
                ORDER BY product_option_number DESC
                LIMIT 1; 
            """
            search_most_updated_result = cursor.execute(search_most_updated, product_info)
            search_most_updated = cursor.fetchone()
            # NOTE expected  {product_option_number: 2334556568}
            new_product_query = """
                INSERT INTO product_info(
                    product_id,
                    seller_id,
                    modifier_id,
                    second_category_id,
                    name,
                    number,
                    detail,
                    price,
                    description,
                    min_quantity,
                    max_quantity
                )
                VALUES (
                    %(product_id)s,
                    %(seller_id)s,
                    %(modifier_id)s,
                    %(second_category_id)s,
                    %(name)s,
                    %(number)s,
                    %(detail)s,
                    %(price)s,
                    %(description)s,
                    %(min_quantity)s,
                    %(max_quantity)s
                );
                """

            new_number = search_most_updated['product_option_number'] + 1
            product_info['number'] = new_number
            product_info_query = cursor.execute(new_product_query, product_info)

            new_product_option_query = """
                INSERT INTO product_options (
                    product_id,
                    modifier_id,
                    color_id,
                    size_id,
                    product_option_number,
                    quantity
                )
                VALUES (
                    %(product_id)s,
                    %(modifier_id)s,
                    %(color_id)s,
                    %(size_id)s,
                    %(product_option_number)s,
                    %(quantity)s
                );
            """

            for option in option_info_data:
                new_number += 1
                product_info['product_option_number'] = new_number
                product_info = dict(product_info, **option)
                print(product_info)
                product_option_info_query = cursor.execute(new_product_option_query, product_info)
                print(1)
                if not product_option_info_query:
                    raise InsertFailError('생성 실패', 400)

            return True
