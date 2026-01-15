import pandas as pd
import numpy as np
from pathlib import Path

class DataAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None
    
    def load_data(self):
        """Load data from CSV or Excel file"""
        if self.filepath.endswith('.csv'):
            self.df = pd.read_csv(self.filepath)
        elif self.filepath.endswith(('.xls', '.xlsx')):
            self.df = pd.read_excel(self.filepath)
        return self.df
    
    def get_summary(self):
        """Get summary statistics"""
        return self.df.describe()
    
    def clean_data(self):
        """Clean the dataset"""
        self.df = self.df.dropna()
        return self.df
    
    def filter_data(self, column, condition):
        """Filter data based on condition"""
        return self.df[self.df[column] == condition]

if __name__ == '__main__':
    analyzer = DataAnalyzer('data/sample_data.csv')
    df = analyzer.load_data()
    print(analyzer.get_summary())
