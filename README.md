# 📘 Network Security ML Pipeline Documentation

## 🧾 Project Overview

This project implements a **machine learning pipeline** to detect **phishing attacks** and other **network security threats**. It is designed to be end-to-end, handling data ingestion, validation, transformation, model training, evaluation, experiment tracking, and deployment.

---

## 🚀 Key Features

* **Data Ingestion**: Load and split raw data from CSV or MongoDB
* **Data Validation**: Validate schema, types, and presence of critical columns
* **Data Transformation**: Impute missing values, scale features
* **Model Training**: Train and tune multiple classification models
* **Experiment Tracking**: Use MLflow (via DagsHub) to track experiments
* **Model Deployment**: FastAPI-based web app for prediction

---

## 🧰 Tech Stack

### 🖥 Backend (API & ML)

| Component           | Technology                                    |
| ------------------- | --------------------------------------------- |
| Language            | Python 3.9+                                   |
| Web Framework       | FastAPI                                       |
| ML Libraries        | scikit-learn, pandas, numpy, imbalanced-learn |
| Experiment Tracking | MLflow (via DagsHub)                          |
| API Testing & Docs  | Swagger UI (FastAPI)                          |

### 🌐 Frontend (Optional Enhancement)

| Component    | Technology                         |
| ------------ | ---------------------------------- |
| UI Framework | React / Vue (optional)             |
| Styling      | TailwindCSS / Bootstrap (optional) |
| API Calls    | Axios / Fetch API (optional)       |

### 🗄 Database

| Component      | Technology       |
| -------------- | ---------------- |
| Raw Data Store | MongoDB / CSV    |
| Logging Store  | MLflow + DagsHub |

---

## 🧩 Pipeline Steps (Detailed)

### 1. 📥 Data Ingestion

* Load raw data from CSV or MongoDB
* Verify availability of required columns (e.g., IP, port, payload, etc.)
* Split data into training and testing sets (default: 80/20)
* Save the split data as `train.csv` and `test.csv`

### 2. 🧪 Data Validation

* Validate schema (expected vs actual columns)
* Check for:

  * Missing values
  * Non-numeric entries in numeric columns
  * Categorical encoding needs
* Generate data drift reports using tools like EvidentlyAI (optional)

### 3. 🔧 Data Transformation

* Impute missing values using `KNNImputer`
* Normalize features with `StandardScaler` or `RobustScaler`
* Save transformation pipeline using `joblib`

### 4. 🧠 Model Training

* Models used:

  * Random Forest
  * Decision Tree
  * Logistic Regression
  * Gradient Boosting
  * AdaBoost
* Perform grid search / random search for hyperparameter tuning
* Metrics used:

  * Accuracy
  * Precision
  * Recall
  * F1 Score
* Save best model as `model.pkl`
* Log parameters, metrics, and artifacts to MLflow

### 5. 🧪 Experiment Tracking

* Integrate MLflow with DagsHub
* Track:

  * Parameters
  * Metrics
  * Model versioning
  * Preprocessing artifacts
* Run via: `mlflow ui` or view on DagsHub

### 6. 🚀 Model Deployment

* FastAPI-based server with `/predict` endpoint
* Accepts: CSV file upload with rows of network feature data
* Returns: CSV with prediction column (`is_phishing: 0/1`)
* Access via: `http://127.0.0.1:8000/docs`

---

## 🛠 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-repo/network-security-ml-pipeline.git
cd network-security-ml-pipeline
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Model

```bash
python train_pipeline.py
```

### 4. Start the API Server

```bash
uvicorn app:app --reload
```

### 5. Access API Docs

Visit: `http://127.0.0.1:8000/docs`

Upload a file to `/predict` endpoint and download predictions.

---

## 📦 Folder Structure

```
network-security-ml-pipeline/
├── data/
│   ├── raw.csv
│   ├── train.csv
│   └── test.csv
├── models/
│   ├── model.pkl
│   └── transformer.pkl
├── notebooks/
│   └── EDA.ipynb
├── app.py               # FastAPI app
├── train_pipeline.py    # Main training script
├── utils/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── data_transformation.py
│   └── model_trainer.py
└── requirements.txt
```

---

## 📈 Future Enhancements

* Add SHAP/LIME explainability
* Integrate with Kafka for streaming logs
* Enable real-time alerting dashboard
* Deploy to AWS/GCP for scaling

---

## 📞 Contact

Maintainer: `Your Name`
Email: `your.email@example.com`
GitHub: `https://github.com/your-repo`

---

> "This project empowers cybersecurity through automation, data, and machine learning — because threats never sleep."
