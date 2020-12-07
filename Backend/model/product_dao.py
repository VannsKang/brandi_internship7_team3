import pymysql
import simplejson


class ProductDao:
    # 상품 리스트 표출
    def get_products(self, filter_data, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
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
                
                #최신 정보로 제한
                AND pi.end_date = '9999-12-31 00:00:00'
                AND si.end_date = '9999-12-31 00:00:00'
                
                #사진 이미지 순서 제한
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
                if filter_data.get('sale_info') == 1:
                    sql += " AND pi.sale_info = 1"
                else:
                    sql += " AND pi.sale_info = 0"

            sql += " ORDER BY pi.start_date DESC"

            # 페이지네이션 끝
            if filter_data.get('limit', None):
                # filter_data['limit'] = int(filter_data['limit'])
                sql += " LIMIT %(limit)s"

            # 페이지네이션 시작
            if filter_data.get('offset', None):
                # filter_data['offset'] = int(filter_data['offset'])
                sql += " OFFSET %(offset)s"
            print(filter_data)
            cursor.execute(sql, filter_data)
            product_list = cursor.fetchall()
            print(product_list)

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
                
                #최신 정보로 제한
                AND pi.end_date = '9999-12-31 00:00:00'
                AND si.end_date = '9999-12-31 00:00:00'
                
                #사진 이미지 순서 제한
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
                if filter_data['sale_info'] == 1:
                    sql += " AND pi.sale_info = 1"
                else:
                    sql += " AND pi.sale_info = 0"

            cursor.execute(sql, filter_data)
            product_count = cursor.fetchone()

            return {'product_list': product_list, 'product_count': product_count}
