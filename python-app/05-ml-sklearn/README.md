# Machine Learning with Scikit-learn

Machine learning application using scikit-learn for classification and regression.

## Features

- Data preprocessing
- Model training and evaluation
- Multiple ML algorithms
- Model persistence
- Hyperparameter tuning

## Project Structure

```
05-ml-sklearn/
├── src/
│   ├── __init__.py
│   ├── train.py
│   ├── predict.py
│   ├── preprocess.py
│   └── evaluate.py
├── models/
│   └── .gitkeep
├── data/
│   ├── train.csv
│   └── test.csv
├── notebooks/
│   └── experiments.ipynb
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Train model
python src/train.py --data data/train.csv --output models/model.pkl

# Make predictions
python src/predict.py --model models/model.pkl --data data/test.csv
```

## Algorithms Supported

- Linear Regression
- Logistic Regression
- Random Forest
- SVM
- K-Nearest Neighbors
