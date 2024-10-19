import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from sklearn.linear_model import LinearRegression

class DataVisualizer:
    """Class for visualizing training and mapped test data."""
    def __init__(self, train_data, mapped_data):
        """Initialize the DataVisualizer object.
        Args:
        train_data (list): Training data to be visualized.
        mapped_data (list): Mapped test data to be visualized.
        """
        self.train_data = train_data
        self.mapped_data = mapped_data

    def visualize_training_data(self):
        """Visualize the training data."""
        plt.switch_backend('TkAgg')  # Switch to a supported backend
        plt.figure(figsize=(8, 6))
        plt.title("Training Data")
        plt.xlabel('X')
        plt.ylabel('Y')
        x_values = [row[0] for row in self.train_data]
        y_values = [row[1:] for row in self.train_data]
        for i in range(len(y_values[0])):
            plt.scatter(x_values, [y[i] for y in y_values], label=f'Y{i+1}', color="blue", s=8)
        plt.legend()
        plt.show()

    def visualize_mapped_data(self):
        """Visualize the mapped test data."""
        plt.switch_backend('TkAgg')  # Switch to a supported backend
        plt.figure(figsize=(8, 6))
        plt.title("Mapped Test Data")
        plt.xlabel('X_test')
        plt.ylabel('Y_test')
        x_values = [data[0][0] for data in self.mapped_data]
        selected_functions = []
        deviations = []
        for x, model, _ in self.mapped_data:
            if isinstance(model, LinearRegression):
                selected_functions.append(model.coef_[0])
                deviations.append(model.intercept_)
            else:
                selected_functions.append(model)
                deviations.append(0)  # Placeholder for non-linear models
        plt.scatter(x_values, selected_functions, label="Selected_Function", color="blue", s=8)
        plt.scatter(x_values, deviations, label="Deviation", color="red", s=8)
        plt.legend()
        plt.show()