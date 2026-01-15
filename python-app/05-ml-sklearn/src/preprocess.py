from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocess_data(df):
    """Preprocess the data"""
    # Handle missing values
    df = df.fillna(df.mean())
    
    # Scale features
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df
