from utils.exceptions import NotExistError


class ProductService:
    def __init__(self, product_dao, config):
        self.product_dao = product_dao
        self.config = config

    def get_products(self, filter_data, conn):
        if filter_data.get('start_date') and filter_data.get('end_date'):
            if filter_data.get('end_date') < filter_data.get('start_date'):
                filter_data['start_date'] = filter_data.get('end_date')
            filter_data['start_date'] += ' 00:00:00'
            filter_data['end_date'] += ' 23:59:59'
        if filter_data.get('start_date') is None:
            filter_data['start_date'] = '2016-05-24 00:00:00'
        if filter_data.get('end_date') is None:
            filter_data['end_date'] = '2050-12-31 23:59:59'
        # if filter_data.get('seller_attribute_id') is None:
        #     filter_data['seller_attribute_id'] = (1, 2, 3, 4, 5, 6, 7)
        get_products_result = self.product_dao.get_products(filter_data, conn)
        print(get_products_result)
        if get_products_result is None:
            raise NotExistError('일치하는 정보가 없습니다.', 400)
        else:
            # product_list = get_products_result['product_list']
            # product_count = get_products_result['product_count']
            # return {'product_list': product_list, 'product_count': product_count}
            return get_products_result
