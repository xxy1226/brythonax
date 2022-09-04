from flask import Flask, url_for

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'iaegiygkasydgvuiaysg'

    from . import brythonax
    app.register_blueprint(brythonax.bp)

    return app

if __name__ == '__main__':
    create_app()