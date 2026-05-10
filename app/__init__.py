from flask import Flask
from app.routes.dashboard import dashboard_bp
from app.routes.analytics import analytics_bp
from app.routes.predictions import predictions_bp
from app.routes.model_metrics import model_metrics_bp
from app.routes.mlflow import mlflow_bp
from app.routes.settings import settings_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.config")

    app.register_blueprint(dashboard_bp, url_prefix="/")
    app.register_blueprint(analytics_bp, url_prefix="/analytics")
    app.register_blueprint(predictions_bp, url_prefix="/predictions")
    app.register_blueprint(model_metrics_bp, url_prefix="/model-metrics")
    app.register_blueprint(mlflow_bp, url_prefix="/mlflow")
    app.register_blueprint(settings_bp, url_prefix="/settings")

    return app