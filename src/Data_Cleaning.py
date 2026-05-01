import pandas as pd
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
)
logger = logging.getLogger('data-cleaning')

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from {file_path}: {e}")
        raise e
def remove_outliers(df, cols):
    df_clean = df.copy()
    for col in cols:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1  
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df_clean = df_clean[(df_clean[col] >= lower) & (df_clean[col] <= upper)]
    return df_clean

def clean_data(data):
    try:
        data.dropna(inplace=True)
        data['price'] = data['price'].replace(r'[^\d]','',regex = True).astype(float)
        data['Area'] = data['Area'].replace(r'[^\d]','',regex = True).astype(float)
        numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
        data = remove_outliers(data, numeric_columns)
        data.to_csv('data/Cleaned_Data.csv', index = False)
        logger.info("Data cleaning completed successfully")
        return data
    except Exception as e:
        logger.error(f"Error during data cleaning: {e}")
        raise e
if __name__ == "__main__":
    data_file_path = Path('data/Apartments.csv')
    data = load_data(data_file_path)
    clean_data(data)

