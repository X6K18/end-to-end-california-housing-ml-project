from flask import Blueprint, request, render_template
from app.services.prediction_service import model_manager

predictions_bp = Blueprint("predictions", __name__)

@predictions_bp.route("/", methods=["GET", "POST"])
def predictions():
    prediction_text = None
    selected_model = request.args.get("model", "best_xgboost")
    all_predictions = None
    
    # Lấy danh sách models để hiển thị dropdown
    model_comparison = model_manager.get_model_comparison()
    
    if request.method == "POST":
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
        
        # Lấy model được chọn từ form
        selected_model = request.form.get("model", "best_xgboost")
        
        # Dự đoán với model được chọn
        price, model_name = model_manager.predict(data, selected_model)
        prediction_text = f"${price:,.2f}"
        
        # Dự đoán với tất cả models để so sánh
        all_predictions = model_manager.predict_all(data)
    
    return render_template(
        "predictions.html", 
        active_page="predictions", 
        prediction_text=prediction_text,
        selected_model=selected_model,
        models=model_comparison,
        all_predictions=all_predictions
    )