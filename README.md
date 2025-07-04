# Network Security ML Pipeline

## Project Description

This project implements an end-to-end machine learning pipeline for network security analysis. The goal is to automate the process of detecting network threats or anomalies using machine learning models. The pipeline is designed to handle all stages of the ML workflow, from data ingestion to model deployment, ensuring reproducibility, scalability, and ease of use.

## Key Features

- **Data Ingestion:**  
  Automatically loads and splits raw network security data for further processing.

- **Data Validation:**  
  Validates the schema, checks for required columns, and ensures data quality before training.

- **Data Transformation:**  
  Handles missing values, feature engineering, and scaling using robust preprocessing techniques (e.g., KNNImputer).

- **Model Training & Selection:**  
  Trains multiple classification models (Random Forest, Decision Tree, Gradient Boosting, Logistic Regression, AdaBoost), performs hyperparameter tuning, and selects the best model based on evaluation metrics.

- **Experiment Tracking:**  
  Integrates with MLflow (via DagsHub) to log metrics, parameters, and artifacts for each experiment run.

- **Model Deployment:**  
  Provides a FastAPI-based web interface for making predictions on new data files, supporting easy integration and real-time inference.

## Implementation Overview

1. **Data Ingestion:**  
   - Loads data from a source (e.g., MongoDB or CSV).
   - Splits data into training and testing sets.
   - Saves processed data for downstream tasks.

2. **Data Validation:**  
   - Checks for schema consistency and required columns.
   - Validates the presence of numerical features.
   - Logs validation results and data drift reports.

3. **Data Transformation:**  
   - Applies preprocessing (imputation, scaling, encoding).
   - Saves transformation objects for reproducibility.

4. **Model Training:**  
   - Trains and tunes several ML models.
   - Evaluates models using metrics like accuracy, precision, recall, and F1-score.
   - Logs the best model and its metrics to MLflow.

5. **Model Deployment:**  
   - Exposes a `/predict` endpoint via FastAPI for batch predictions.
   - Accepts file uploads and returns predictions in a user-friendly format.

6. **Experiment Tracking:**  
   - Uses MLflow (with DagsHub backend) for tracking experiments, metrics, and artifacts.

## How to Run

1. **Clone the repository and install dependencies.**
2. **Start the FastAPI server:**
   ```bash
   uvicorn app:app --reload
   ```
3. **Access the API documentation at:**  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

4. **Train the pipeline and make predictions using the provided endpoints.**

---

**This pipeline enables automated, reliable, and scalable network security analysis using machine learning.**

---
