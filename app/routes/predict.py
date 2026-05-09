from flask import Blueprint, request, jsonify, render_template
from app.services.prediction_service import predict_house_price

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict_api", methods=["POST"])
def predict_api():

    data = request.json["data"]

    prediction = predict_house_price(data)

    return jsonify({
        "prediction": prediction
    })


@predict_bp.route("/predict", methods=["POST"])
def predict():

    data = {
        "MedInc": float(request.form["MedInc"]),
        "HouseAge": float(request.form["HouseAge"]),
        "AveRooms": float(request.form["AveRooms"]),
        "AveBedrms": float(request.form["AveBedrms"]),
        "Population": float(request.form["Population"]),
        "AveOccup": float(request.form["AveOccup"]),
        "Latitude": float(request.form["Latitude"]),
        "Longitude": float(request.form["Longitude"])
    }

    prediction = predict_house_price(data)

    return render_template(
        "home.html",
        prediction_text=f"Predicted House Price: ${prediction:,.2f}"
        
    )