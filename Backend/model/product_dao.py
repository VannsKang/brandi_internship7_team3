import pymysql


class ProductDao:
    # 상품 리스트 표출
    def get_products(self, filter_data, conn):
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:

            filter_data['offset'] = int(filter_data['offset'])
            filter_data['limit'] = int(filter_data['limit'])

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
                #상품 아이디
                INNER JOIN products AS p ON p.product_id = pi.product_id
                #셀러 이름
                INNER JOIN seller_info AS si ON si.seller_info_id = pi.seller_id
                #셀러 속성
                INNER JOIN seller_attributes AS sa ON sa.seller_attribute_id = si.seller_attribute_id
                #상품 대표이미지
                INNER JOIN product_images AS img ON img.product_info_id = pi.product_id
                WHERE pi.is_deleted = 0
                AND si.is_deleted = 0
                AND img.is_deleted = 0
                AND pi.end_date = '9999-12-31 00:00:00'
                AND si.end_date = '9999-12-31 00:00:00'
                AND img.e d_date = '9999-12-31 00:00:00'
                AND img.image_order_id = 1
                """