from flask import Blueprint, render_template

mlflow_bp = Blueprint("mlflow", __name__)

@mlflow_bp.route("/")
def mlflow():
    return render_template("mlflow.html", active_page="mlflow")