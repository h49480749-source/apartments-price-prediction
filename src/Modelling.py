from sklearn.model_selection import train_test_split, cross_validate, KFold , cross_val_predict
from sklearn.linear_model import Ridge
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.preprocessing import PolynomialFeatures, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
import mlflow
import joblib
from pathlib import Path
import logging
import dagshub
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
)
logger = logging.getLogger('Model-Building')

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from {file_path}: {e}")
        raise e

def modelling(data):
    try:
        X = data.drop(columns=['price','Posted_by'])
        y = data['price']
        preprocessor = ColumnTransformer([
            ("cat", OneHotEncoder(handle_unknown="ignore"),make_column_selector(dtype_include=object)),
            ("num", "passthrough", make_column_selector(dtype_include=["int64", "float64"]))
        ])
        dagshub.init(repo_owner='h49480749', repo_name='apartments-price-prediction', mlflow=True)
        mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
        mlflow.set_experiment("Apartments Price Prediction")
        splits = 3
        kf = KFold(shuffle=True, random_state=42, n_splits=splits)
        model = Pipeline([
            ("preprocessor", preprocessor),
            ("poly", PolynomialFeatures(degree=2)),
            ("lr", Ridge(alpha=9))
        ])
        with mlflow.start_run(run_name='Ridge Regression'):
            
            y_pred = cross_val_predict(model,X,y, cv=kf)
            score = r2_score(y,y_pred)
            model.fit(X,y)
            mlflow.log_param("Cross_validation_splits", splits)
            mlflow.log_param("alpha", 9.0)
            mlflow.log_metric('r2_score', score)
            mlflow.sklearn.log_model(sk_model=model, artifact_path="Ridge_regression_model")        
            model.fit(X,y)
        joblib.dump(model, 'models/model.pkl')
        logger.info("Model building and saving completed successfully")
    except Exception as e:
        logger.error(f"Error during model building: {e}")
        raise e

if __name__ == "__main__":
    data_file_path = Path('data/Cleaned_Data.csv')
    data = load_data(data_file_path)
    modelling(data)