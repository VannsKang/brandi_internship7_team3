class SellerService:
    def __init__(self, user_dao, config):
        self.seller_dao = user_dao
        self.config   = config

    def get_seller_list(self, filter_data, conn):
        seller_list = self.seller_dao.get_seller_list(filter_data, conn)

        columns = [
            {
                'title': '번호',
                'dataIndex': 'id'
            },
            {
                'title': '셀러아이디',
                'dataIndex': 'seller_id'
            },
            {
                'title': '영문이름',
                'dataIndex': 'eng_name'
            },
            {
                'title': '한글이름',
                'dataIndex': 'kor_name',
            },
            {
                'title': '담당자이름',
                'dataIndex': 'owner_name'
            },
            {
                'title': '셀러상태',
                'dataIndex': 'seller_status'
            },
            {
                'title': '담당자연락처',
                'dataIndex': 'phone_number'
            },
            {
                'title': '담당자이메일',
                'dataIndex': 'email'
            },
            {
                'title': '셀러속성',
                'dataIndex': 'seller_attribute'
            },
            {
                'title': '등록일시',
                'dataIndex': 'created_at'
            },
            {
                'title': 'Actions',
                'dataIndex': 'seller_actions'
            }
        ]

        data = {
            'columns' : columns,
            'seller_count' :  self.seller_dao.get_seller_count(filter_data, conn)['count'],
            'data': [{
                'id'               : seller['id'],
                'seller_id'        : seller['seller_id'],
                'eng_name'         : seller['eng_name'],
                'kor_name'         : seller['kor_name'],
                'seller_status'    : seller['seller_status'],
                'seller_attribute' : seller['seller_attribute'],
                'owner_name'       : seller['owner_name'],
                'phone_number'     : seller['phone_number'],
                'email'            : seller['email'],
                'created_at'       : seller['created_at'].strftime('%Y-%m-%d %H:%M:%S'),
                'seller_actions'   : [{
                    'id'  : seller_action_id,
                    'name': seller_action
                } for seller_action_id, seller_action
                    in zip(seller['seller_action_id'].split(','), seller['seller_action'].split(','))]
                if seller['seller_action_id'] else None
            } for seller in seller_list]
        }

        return data

    def get_seller_status(self, conn):
        seller_status = self.seller_dao.get_seller_status(conn)

        return seller_status

    def get_seller_attributes(self, conn):
        seller_attributes = self.seller_dao.get_seller_attributes(conn)

        return seller_attributes

    def update_seller_status(self, account_info, conn):

        if 'id' not in account_info:
            raise KeyError

        if 'seller_action_id' not in account_info:
            raise KeyError

        if len(account_info) != 2:
            raise KeyError

        # 액션에 따른 상태 이전
        if account_info['seller_action_id'] == 1:
            account_info['seller_status_id'] = 2

        if account_info['seller_action_id'] == 2:
            account_info['is_deleted'] = 1

        if account_info['seller_action_id'] == 3:
            account_info['seller_status_id'] = 5

        if account_info['seller_action_id'] == 4:
            account_info['seller_status_id'] = 2

        if account_info['seller_action_id'] == 5:
            account_info['seller_status_id'] = 4

        if account_info['seller_action_id'] == 6:
            account_info['seller_status_id'] = 2

        if account_info['seller_action_id'] == 7:
            account_info['seller_status_id'] = 3

        if 'seller_status_id' not in account_info:
            raise Exception("유효하지 않은 액션 값 전송")

        seller_status = self.seller_dao.update_seller_status(account_info, conn)

        return seller_status
