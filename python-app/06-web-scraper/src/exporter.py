import pandas as pd

def export_to_csv(data, filepath):
    """Export data to CSV"""
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"Data exported to {filepath}")

def export_to_json(data, filepath):
    """Export data to JSON"""
    df = pd.DataFrame(data)
    df.to_json(filepath, orient='records', indent=2)
    print(f"Data exported to {filepath}")
