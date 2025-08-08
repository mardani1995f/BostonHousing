import pandas as pd


def load_data():

    # Lets load the dataset and sample some
    column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
                    'MEDV']
    data = pd.read_csv('dataset/housing.csv', header=None, delimiter=r"\s+", names=column_names)

    return data