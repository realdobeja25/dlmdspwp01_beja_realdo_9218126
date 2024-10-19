##
import json
import numpy as np
from sqlalchemy import create_engine, Column, Integer, Float, MetaData, Table, Text

class data_base:
    """Class for managing database operations."""
    def __init__(self, db_name):
        """Initialize the data_base object.

        Args:
        db_name (str): Name of the database file.
        """
        self.db_name = db_name
        self.engine = create_engine(f'sqlite:///{self.db_name}')
        self.metadata = MetaData()
        self.table_of_mapped_data = None  # Initialize as None




    def create_tables(self):
        """Create tables in the database."""
        table_of_train_data = Table(
            'train_data', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('X', Float),
            Column('Y1', Float),
            Column('Y2', Float),
            Column('Y3', Float),
            Column('Y4', Float)
        )

        table_of_ideal_data = Table(
            'ideal_functions', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('X', Float),
            *[Column(f'Y{i}', Float) for i in range(1, 51)])

        self.table_of_mapped_data = Table(
            'mapped_data', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('X_test', Float),
            Column('Y_test', Float),
            Column('Selected_Function', Text),
            Column('Deviation', Float)
        )

        self.metadata.create_all(self.engine)

    def data_load(self, data, table_name):
        """Load data into a specified table in the database.
        Args:
        data (DataFrame): Data to be loaded into the table.
        table_name (str): Name of the table.
        """
        data.to_sql(table_name, con=self.engine, if_exists='append', index=False)

    def store_mapped_data(self, mapped_data):
        """Store mapped data in the database.
        Args:
        mapped_data (list): Mapped data to be stored.
        """

        conn = self.engine.connect()
        for data_point in mapped_data:
            x_test, selected_function, deviation = data_point
            # Extract the first element from the tuple for X_test
            x_test = x_test[0]
            y_test = None  # Placeholder for y_test since it's not provided in the mapped data

            # Extract coefficients from selected_function (assuming it's a scikit-learn LinearRegression object)
            coefficients = selected_function.coef_

            # Convert coefficients to a string representation
            coefficients_str = ','.join(map(str, coefficients))

            conn.execute(self.table_of_mapped_data.insert().values(
                X_test=x_test,
                Y_test=y_test,
                Selected_Function=coefficients_str,
                Deviation=deviation
            ))
        conn.close()

##