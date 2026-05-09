# Linear Regression - California Housing Dataset

Dự án này thực hiện bài toán dự đoán giá nhà tại California bằng thuật toán Linear Regression sử dụng thư viện Scikit-learn.

## Nội dung thực hiện

### 1. Data Preprocessing
- Load California Housing Dataset
- Tạo DataFrame bằng Pandas
- Kiểm tra:
  - Missing values
  - Duplicate values
  - Thống kê mô tả dữ liệu

### 2. Exploratory Data Analysis (EDA)
Thực hiện trực quan hóa dữ liệu bằng:
- Correlation Heatmap
- Pairplot
- Scatter Plot
- Histogram
- Regression Plot

Phân tích mối quan hệ giữa:
- Median Income và House Price
- Average Rooms và House Price
- House Age và House Price
- Latitude / Longitude và House Price

### 3. Feature Engineering & Scaling
- Chia dữ liệu Train/Test
- Chuẩn hóa dữ liệu bằng `StandardScaler`

### 4. Model Training
Sử dụng mô hình:

```python
LinearRegression()
```

Huấn luyện mô hình trên tập train và thực hiện dự đoán trên tập test.

### 5. Model Evaluation

Các độ đo đã thực hiện trong notebook:

| Metric | Ý nghĩa |
|---|---|
| MAE (Mean Absolute Error) | Sai số tuyệt đối trung bình |
| MSE (Mean Squared Error) | Sai số bình phương trung bình |
| RMSE (Root Mean Squared Error) | Căn bậc hai của MSE |
| R² Score | Đánh giá mức độ phù hợp của mô hình |
| Adjusted R² | Đánh giá mô hình có xét số lượng features |

### 6. Residual Analysis
Thực hiện:
- Residual Distribution Plot
- Residual vs Predicted Plot
- Actual vs Predicted Scatter Plot

Mục tiêu:
- Kiểm tra phân phối lỗi
- Đánh giá chất lượng dự đoán
- Kiểm tra hiện tượng heteroscedasticity

### 7. Model Persistence
Lưu mô hình bằng:

```python
pickle
```

File model:
```bash
models/regmodel.pkl
```

## Công nghệ sử dụng

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Dataset

Dataset sử dụng:
```python
fetch_california_housing()
```

Features:
- MedInc
- HouseAge
- AveRooms
- AveBedrms
- Population
- AveOccup
- Latitude
- Longitude

Target:
- Price

## Kết quả đạt được

- Xây dựng thành công mô hình dự đoán giá nhà.
- Thực hiện đầy đủ quy trình Machine Learning:
  - Data preprocessing
  - Data visualization
  - Model training
  - Model evaluation
  - Residual analysis
  - Model saving

## File Notebook

```bash
linear_regression.ipynb
```