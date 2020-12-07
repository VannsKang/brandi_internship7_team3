
class ProductService:
    def __init__(self, product_dao, config):
        self.product_dao = product_dao
        self.config = config

    
    # NOTE soomyung's API get color data
    def get_colors(self, conn):
        
        colors =  self.product_dao.get_colors(conn)
        
        return colors
    
    # NOTE soomyung's API get size data
    def get_sizes(self, conn):
        
        sizes =  self.product_dao.get_sizes(conn)
        
        return sizes
    
    # NOTE soomyung's API get first_categories data
    def get_first_categories(self, conn):
        
        first_categories =  self.product_dao.get_first_categories(conn)
        
        return first_categories

    # NOTE soomyung's API get second_categories data
    def get_second_categories(self, first_category_id, conn):
        
        if "first_category_id" not in first_category_id:
            raise KeyError
        
        second_categories =  self.product_dao.get_second_categories(first_category_id, conn)
        
        return second_categories
    
    # NOTE soomyung's API post new products data
    def add_new_product(self,product_info, conn):
        # print(product_info)
        # NOTE number, product_option_number => custom auto increments
        
        new_product =  self.product_dao.add_new_product(product_info,conn)

        return new_product