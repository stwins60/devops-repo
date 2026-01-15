import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, dataframe):
        self.df = dataframe
        sns.set_style('whitegrid')
    
    def plot_histogram(self, column, output_path='output/histogram.png'):
        """Create histogram"""
        plt.figure(figsize=(10, 6))
        self.df[column].hist(bins=30)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.savefig(output_path)
        plt.close()
    
    def plot_scatter(self, x_col, y_col, output_path='output/scatter.png'):
        """Create scatter plot"""
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df[x_col], self.df[y_col])
        plt.title(f'{x_col} vs {y_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.savefig(output_path)
        plt.close()
