from flask import Blueprint, render_template

model_metrics_bp = Blueprint("model_metrics", __name__)

@model_metrics_bp.route("/")
def model_metrics():
    return render_template("model_metrics.html", active_page="model_metrics")