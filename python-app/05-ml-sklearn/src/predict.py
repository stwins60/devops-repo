import joblib
import pandas as pd

class Predictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
    
    def predict(self, X):
        """Make predictions"""
        return self.model.predict(X)
    
    def predict_proba(self, X):
        """Get prediction probabilities"""
        return self.model.predict_proba(X)

if __name__ == '__main__':
    print("Predictor ready")
