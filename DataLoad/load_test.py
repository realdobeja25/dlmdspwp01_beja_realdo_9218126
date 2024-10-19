import csv

##
class load_test_data:
    """Class for loading and parsing test data from a CSV file."""
    def __init__(self, file_path):
        """Initialize the load_test_data object.

        Args:
        file_path (str): Path to the CSV file containing test data.
        """
        self.file_path = file_path
        self.data = []

    def read_file_of_test(self):
        """Read the CSV file containing test data."""
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self.data.append(row)

    def parse_data_of_test(self):
        """Parse the test data read from the CSV file.

        Returns:
        list: Parsed test data.
        """
        test_data = []
        for row in self.data:
            x_values, y_values = map(float, row)
            test_data.append((x_values, y_values))
        return test_data
    ##