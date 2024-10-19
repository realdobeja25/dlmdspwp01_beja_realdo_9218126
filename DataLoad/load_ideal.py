import csv
##
class load_ideal_data:
    """Class for loading and parsing ideal data from a CSV file.
        Args:
            file_path (str): Path to the CSV file containing ideal data.
        """
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_file_of_ideal(self):
        """Read the CSV file containing ideal data."""
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self.data.append(row)

    def parse_data_of_ideal(self):
        """Parse the ideal data read from the CSV file.

        Returns:
        list: Parsed ideal data.
        """
        ideal_data = []
        for row in self.data:
            x_values = float(row[0])
            y_values = [float(val) for val in row[1:]]
            ideal_data.append((x_values, y_values))
        return ideal_data
##