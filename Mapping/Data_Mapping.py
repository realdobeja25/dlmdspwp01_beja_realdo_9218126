import numpy as np
from sklearn.linear_model import LinearRegression

import numpy as np
from sklearn.linear_model import LinearRegression

class DataException(Exception):
    """Base class for data-related exceptions."""
    pass

class TestDataMapper:
    """
    Class for mapping test data to ideal functions.

    This class takes training data, ideal functions, and test data as input and maps each test data point
    to the most appropriate ideal function based on deviation criteria.

    Attributes:
        train_data (numpy.ndarray): Training data array with shape (n_samples, n_features).
        ideal_functions (list): List of ideal functions represented as models or coefficients.
        test_data (list): List of test data points to be mapped.
        sqrt2 (float): Square root of 2, used for deviation calculation.

    Methods:
        __init__(train_data, ideal_functions, test_data):
            Initializes the TestDataMapper object.

        fit_ideal_functions():
            Fits ideal functions using linear regression.

        calculate_deviation(test_point, model):
            Calculates deviation between test point and ideal function.

        calculate_max_deviation(model):
            Calculates maximum deviation between training data and ideal function.

        map_test_data():
            Maps test data to ideal functions and returns the mapped data.
    """

    def __init__(self, train_data, ideal_functions, test_data):
        """
        Initialize the TestDataMapper object.

        Args:
            train_data (numpy.ndarray): Training data array with shape (n_samples, n_features).
            ideal_functions (list): List of ideal functions represented as models or coefficients.
            test_data (list): List of test data points to be mapped.

        Raises:
            DataException: If input data is not provided as lists or if input data lists are empty.
        """
        if not isinstance(train_data, list) or not isinstance(ideal_functions, list) or not isinstance(test_data, list):
            raise DataException("Input data must be provided as lists.")
        if len(train_data) == 0 or len(ideal_functions) == 0 or len(test_data) == 0:
            raise DataException("Input data lists must not be empty.")
        self.train_data = np.array(train_data)
        self.ideal_functions = ideal_functions
        self.test_data = test_data
        self.sqrt2 = np.sqrt(2)

    def fit_ideal_functions(self):
        """
        Fits ideal functions to the training data using linear regression.

        Returns:
        - models (list): List of linear regression models representing ideal functions.
        """
        models = []
        for y_train in self.train_data[:, 1:].T:
            model = LinearRegression().fit(self.train_data[:, 0].reshape(-1, 1), y_train)
            models.append(model)
        return models

    def calculate_deviation(self, test_point, model):
        """
        Calculates the deviation between a test data point and an ideal function represented by a model.

        Parameters:
        - test_point (tuple): Test data point (x, y).
        - model (LinearRegression): Ideal function represented by a linear regression model.

        Returns:
        - deviation (float): Absolute difference between the predicted value and the actual value of the test point.
        """
        return np.abs(test_point[1] - model.predict(np.array([[test_point[0]]])))

    def calculate_max_deviation(self, model):
        """
        Computes the maximum deviation between the training data and an ideal function represented by a model.

        Parameters:
        - model (LinearRegression): Ideal function represented by a linear regression model.

        Returns:
        - max_deviation (float): Maximum deviation between training data and the ideal function.
        """
        deviations = np.abs(model.predict(self.train_data[:, 0].reshape(-1, 1)) - self.train_data[:, 1])
        return np.max(deviations)

    def map_test_data(self):
        """
        Maps test data points to the most appropriate ideal functions based on deviation criteria.

        Returns:
        - mapped_data (list): List of tuples containing mapped test data points along with selected functions and deviations.
        """
        mapped_data = []
        models = self.fit_ideal_functions()

        for test_point in self.test_data:
            min_deviation = float('inf')
            selected_function = None
            for model in models:
                deviation = self.calculate_deviation(test_point, model)
                max_allowed_deviation = self.calculate_max_deviation(model) * self.sqrt2
                if deviation < min_deviation and deviation <= max_allowed_deviation:
                    min_deviation = deviation
                    selected_function = model

            if selected_function is not None:
                mapped_data.append((test_point, selected_function, min_deviation))
        return mapped_data