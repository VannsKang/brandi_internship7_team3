import flask_excel as excel

from app import create_app

if __name__ == '__main__':
    app = create_app()
    excel.init_excel(app)
    app.run(host='0.0.0.0', port=5000)
