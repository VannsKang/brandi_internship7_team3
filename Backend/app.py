from flask      import Flask, jsonify, request  #jsonify -> 딕셔너리를 json으로 변환
from sqlalchemy import create_engine, text       #create_engine -> 데이터베이스 연결, text -> 실행 sql 만들기
from flask_cors import CORS


# app = Flask(__name__)       #import한 flask 클래스를 객체화한 후 app 변수에 저장
# app.users = {}      #새로 가입한 사용자를 저장할 딕셔너리를 users 라는 변수에 저장
# app.id_count = 1    #회원가입하는 사용자의 id 값을 저장하는 변수이다. id는 1부터 시작하며 새로운 사용자가 생성될 때마다 하나씩 증가한다.

def create_app(test_config = None):
    app = Flask(__name__)
    CORS(app)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)
    database = create_engine(app.config['DB_URL'], encoding = "utf-8", max_overflow = 0)    #데이터베이스와 연결
    app.database = database

    @app.route('/sign-up', methods = ['POST'])
    def sign_up():
        new_account = request.json  # 요청을 통해 전송된 json 데이터를 파이썬 딕셔너리로 변환
        new_user_id = app.database.execute(text("""
            INSERT INTO accounts (
                user_id,
                class_id
            ) VALUES (
                :user_id,
                :class_id
            )
        """), new_account)  # 요청으로 전송된 정보에 id 값을 더해준다.
        # app.users[app.id_count] = new_account  # 회원가입하는 사용자의 정보를 딕셔너리에 저장한다. key는 사용자 아이디이고, value는 회원정보이다.
        # app.id_count = app.id_count + 1  # id 값에 1을 더해준다.
        return jsonify({'message' : 'SUCCESS'}), 201
    return app