from flask import Blueprint, render_template
from app.services.prediction_service import model_manager

model_metrics_bp = Blueprint("model_metrics", __name__)

@model_metrics_bp.route("/")
def model_metrics():
    """Hiển thị trang so sánh các models"""
    models = model_manager.get_model_comparison()
    return render_template("model_comparison.html", active_page="model_metrics", models=models)