import os
import joblib
import numpy as np
from typing import Dict, Tuple, List

# ====================================
# Base Directory
# ====================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# ====================================
# Model Configuration
# ====================================

class ModelManager:
    """Quản lý nhiều models với scaling strategy riêng"""
    
    MODELS_CONFIG = {
        "linear_regression": {
            "name": "Linear Regression",
            "path": os.path.join(BASE_DIR, "models", "linear_regression_model", "linear_regression.pkl"),
            "scaler_path": os.path.join(BASE_DIR, "models", "linear_regression_model", "scaler.pkl"),
            "need_scaling": True,
            "metrics": {"r2": 0.5958, "rmse": 0.7294, "mae": 0.5272}
        },
        "random_forest": {
            "name": "Random Forest",
            "path": os.path.join(BASE_DIR, "models", "random_forest_model", "random_forest.pkl"),
            "scaler_path": None,
            "need_scaling": False,
            "metrics": {"r2": 0.8061, "rmse": 0.5045, "mae": 0.3370}
        },
        "xgboost": {
            "name": "XGBoost",
            "path": os.path.join(BASE_DIR, "models", "xgboost_model", "xgboost_model.pkl"),
            "scaler_path": None,
            "need_scaling": False,
            "metrics": {"r2": 0.8445, "rmse": 0.4518, "mae": 0.30}
        },
        "best_xgboost": {
            "name": "Best XGBoost",
            "path": os.path.join(BASE_DIR, "models", "best_xgboost", "best_xgboost_02.pkl"),
            "scaler_path": None,
            "need_scaling": False,
            "metrics": {"r2": 0.85, "rmse": 0.45, "mae": 0.29}
        }
    }
    
    def __init__(self):
        self.models = {}
        self.scalers = {}
        self.load_all_models()
    
    def load_all_models(self):
        """Load tất cả models vào bộ nhớ"""
        for model_key, config in self.MODELS_CONFIG.items():
            try:
                if os.path.exists(config["path"]):
                    self.models[model_key] = joblib.load(config["path"])
                    print(f"✅ Loaded {config['name']}")
                    
                    if config["need_scaling"] and config["scaler_path"]:
                        if os.path.exists(config["scaler_path"]):
                            self.scalers[model_key] = joblib.load(config["scaler_path"])
                else:
                    print(f"⚠️ Model not found: {config['path']}")
            except Exception as e:
                print(f"❌ Error loading {config['name']}: {e}")
    
    def prepare_features(self, data: Dict, model_key: str) -> np.ndarray:
        """Chuẩn bị features theo yêu cầu của model"""
        features = np.array([
            data["MedInc"],
            data["HouseAge"],
            data["AveRooms"],
            data["AveBedrms"],
            data["Population"],
            data["AveOccup"],
            data["Latitude"],
            data["Longitude"]
        ]).reshape(1, -1)
        
        # Chỉ scale nếu model cần
        if self.MODELS_CONFIG[model_key]["need_scaling"] and model_key in self.scalers:
            features = self.scalers[model_key].transform(features)
        
        return features
    
    def predict(self, data: Dict, model_key: str = "best_xgboost") -> Tuple[float, str]:
        """Dự đoán với model được chọn"""
        if model_key not in self.models:
            raise ValueError(f"Model {model_key} not found. Available: {list(self.models.keys())}")
        
        features = self.prepare_features(data, model_key)
        prediction = self.models[model_key].predict(features)[0]
        
        return round(float(prediction), 4), self.MODELS_CONFIG[model_key]["name"]
    
    def predict_all(self, data: Dict) -> List[Dict]:
        """Dự đoán với tất cả models"""
        results = []
        for model_key in self.models.keys():
            try:
                pred, name = self.predict(data, model_key)
                results.append({
                    "model_key": model_key,
                    "model_name": name,
                    "prediction": pred,
                    "metrics": self.MODELS_CONFIG[model_key]["metrics"],
                    "need_scaling": self.MODELS_CONFIG[model_key]["need_scaling"]
                })
            except Exception as e:
                results.append({
                    "model_key": model_key,
                    "model_name": self.MODELS_CONFIG[model_key]["name"],
                    "prediction": None,
                    "error": str(e),
                    "need_scaling": self.MODELS_CONFIG[model_key]["need_scaling"]
                })
        return sorted(results, key=lambda x: x.get("prediction", 0), reverse=True)
    
    def get_model_comparison(self) -> Dict:
        """Lấy thông tin so sánh các models"""
        comparison = {}
        for model_key, config in self.MODELS_CONFIG.items():
            if model_key in self.models:
                comparison[model_key] = {
                    "name": config["name"],
                    "metrics": config["metrics"],
                    "need_scaling": config["need_scaling"]
                }
        return comparison

# ====================================
# Khởi tạo global model manager
# ====================================

model_manager = ModelManager()

# ====================================
# Backward compatible functions
# ====================================

def predict_house_price(data: dict, model_key: str = "best_xgboost") -> float:
    """Hàm cũ để tương thích ngược"""
    prediction, _ = model_manager.predict(data, model_key)
    return prediction

def predict_with_all_models(data: dict) -> List[Dict]:
    """Dự đoán với tất cả models"""
    return model_manager.predict_all(data)