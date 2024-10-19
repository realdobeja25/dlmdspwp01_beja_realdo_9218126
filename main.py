##
from DataLoad.load_train import load_train_data
from DataLoad.load_test import load_test_data
from DataLoad.load_ideal import load_ideal_data
from DataBase.data_base_creation import data_base
from Data_Visualization.ProjectHandler import DataVisualizer
from Mapping.Data_Mapping import TestDataMapper
##
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ##
    train_loader = load_train_data("Datasets1/train.csv")
    train_loader.read_file_of_train()
    train_data = train_loader.parse_data_of_train()
    print(train_data)
    ##
    test_loader = load_test_data("Datasets1/test.csv")
    test_loader.read_file_of_test()
    test_data = test_loader.parse_data_of_test()
    print(test_data)
    ##
    ideal_loader = load_ideal_data("Datasets1/ideal.csv")
    ideal_loader.read_file_of_ideal()
    ideal_data = ideal_loader.parse_data_of_ideal()
    print(ideal_data)
    ##
    db_manager = data_base('database_schema.db')
    db_manager.create_tables()
    print("Tables created.")
    ##
    # Initialize and use TestDataMapper
    mapper = TestDataMapper(train_data, ideal_data, test_data)
    mapped_data = mapper.map_test_data()
    print(mapped_data)
    ##
    ##
    # Store mapped_data in the database
    # Store mapped data in the database
    db_manager = data_base('database_schema.db')
    db_manager.create_tables()
    db_manager.store_mapped_data(mapped_data)
    ##
    ##
    visualizer = DataVisualizer(train_data, mapped_data)
    visualizer.visualize_training_data()
    visualizer.visualize_mapped_data()
    ##