
##
import unittest
from DataLoad.load_train import load_train_data
from DataLoad.load_test import load_test_data
from DataLoad.load_ideal import load_ideal_data
import Datasets1


class TestDataLoading(unittest.TestCase):
    def setUp(self):
        # Initialize test file paths
        self.train_file = "train.csv"
        self.test_file = "test.csv"
        self.ideal_file = "ideal.csv"

    def test_load_train_data(self):
        # Test loading and parsing of training data
        train_loader = load_train_data(self.train_file)
        train_loader.read_file_of_train()
        train_data = train_loader.parse_data_of_train()

        # Assert that data is loaded and parsed correctly
        self.assertIsNotNone(train_data)
        self.assertIsInstance(train_data, list)
        self.assertGreater(len(train_data), 0)
        # Add more specific assertions based on the structure and content of your training data

    def test_load_test_data(self):
        # Test loading and parsing of test data
        test_loader = load_test_data(self.test_file)
        test_loader.read_file_of_test()
        test_data = test_loader.parse_data_of_test()

        # Assert that data is loaded and parsed correctly
        self.assertIsNotNone(test_data)
        self.assertIsInstance(test_data, list)
        self.assertGreater(len(test_data), 0)
        # Add more specific assertions based on the structure and content of your test data

    def test_load_ideal_data(self):
        # Test loading and parsing of ideal data
        ideal_loader = load_ideal_data(self.ideal_file)
        ideal_loader.read_file_of_ideal()
        ideal_data = ideal_loader.parse_data_of_ideal()

        # Assert that data is loaded and parsed correctly
        self.assertIsNotNone(ideal_data)
        self.assertIsInstance(ideal_data, list)
        self.assertGreater(len(ideal_data), 0)
        # Add more specific assertions based on the structure and content of your ideal data


if __name__ == '__main__':
    unittest.main()
##