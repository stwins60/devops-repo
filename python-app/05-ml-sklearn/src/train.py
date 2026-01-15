from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

class ModelTrainer:
    def __init__(self, model_type='random_forest'):
        self.model = None
        self.model_type = model_type
        
    def load_data(self, filepath):
        """Load training data"""
        return pd.read_csv(filepath)
    
    def train(self, X, y):
        """Train the model"""
        if self.model_type == 'random_forest':
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        
        self.model.fit(X, y)
        return self.model
    
    def save_model(self, filepath):
        """Save trained model"""
        joblib.dump(self.model, filepath)
    
    def evaluate(self, X_test, y_test):
        """Evaluate model"""
        score = self.model.score(X_test, y_test)
        return score

if __name__ == '__main__':
    trainer = ModelTrainer()
    print("Model trainer initialized")
