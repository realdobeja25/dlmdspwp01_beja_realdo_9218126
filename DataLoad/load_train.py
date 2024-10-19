##
import csv

class load_train_data:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_file_of_train(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                self.data.append(row)

    def parse_data_of_train(self):
        train_data = []
        for idx, row in enumerate(self.data):
            x_value = float(row[0])
            y_values = [float(val) for val in row[1:]]
            train_data.append([x_value] + y_values)
            # Debugging: Print the length of each row
            print(f"Row {idx + 1}: Length = {len([x_value] + y_values)}")
        return train_data
##