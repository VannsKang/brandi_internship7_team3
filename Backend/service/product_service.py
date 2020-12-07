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
        get_products_result = self.product_dao.get_products(filter_data, conn)
        if get_products_result is None:
            raise NotExistError('일치하는 정보가 없습니다.', 400)
        else:
            return get_products_result

    # NOTE soomyung's API get color data
    def get_colors(self, conn):

        colors = self.product_dao.get_colors(conn)

        return colors

    # NOTE soomyung's API get size data
    def get_sizes(self, conn):

        sizes = self.product_dao.get_sizes(conn)

        return sizes

    # NOTE soomyung's API get first_categories data
    def get_first_categories(self, conn):

        first_categories = self.product_dao.get_first_categories(conn)

        return first_categories

    # NOTE soomyung's API get second_categories data
    def get_second_categories(self, first_category_id, conn):

        if "first_category_id" not in first_category_id:
            raise KeyError

        second_categories = self.product_dao.get_second_categories(first_category_id, conn)

        return second_categories

    # NOTE soomyung's API post new products data
    def add_new_product(self, product_info, conn):
        # print(product_info)
        # NOTE number, product_option_number => custom auto increments

        new_product = self.product_dao.add_new_product(product_info, conn)

        return new_product
