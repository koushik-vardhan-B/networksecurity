# Network Security ML Pipeline

## Project Description

This project implements an end-to-end machine learning pipeline for **cyber security analysis**, specifically focusing on detecting phishing attacks using network data. The goal is to automate the process of identifying phishing threats or anomalies with machine learning models. The pipeline covers all stages of the ML workflow, from data ingestion to model deployment, ensuring reproducibility, scalability, and ease of use.

## Key Features

- **Data Ingestion:**  
  Automatically loads and splits raw phishing/network security data (e.g., from CSV or MongoDB).

- **Data Validation:**  
  Validates schema, checks for required columns (including numerical features), and ensures data quality before training.

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
   - Loads phishing dataset (network features and labels) from a source (e.g., MongoDB or CSV).
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
   - Accepts phishing/network data files (CSV) and returns predictions in a user-friendly format.

6. **Experiment Tracking:**  
   - Uses MLflow (with DagsHub backend) for tracking experiments, metrics, and artifacts.

## How Inputs and Outputs Work

- **Input:**  
  Upload a CSV file containing network or phishing data (with the same features as used in training) via the `/predict` endpoint in the FastAPI web interface.

- **Output:**  
  The API returns a table (HTML or downloadable CSV) with an additional column indicating the model's prediction for each row (e.g., `phishing` or `legitimate`).  
  The output can be viewed directly in the browser or downloaded for further analysis.

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

**This pipeline enables automated, reliable, and scalable detection of phishing attacks and other network security threats using machine learning.**

---
