from flask import Flask

def create_app():

    app = Flask(__name__)

    from app.routes.home import home_bp
    from app.routes.predict import predict_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(predict_bp)

    return app