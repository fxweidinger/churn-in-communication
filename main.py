import pandas
import numpy as np

pandas.set_option('display.max_columns', None)

dataset = pandas.read_csv("../churn-in-communication/WA_Fn-UseC_-Telco-Customer-Churn.csv")


def data_dump(dataframe, message):
    print(f'{message}:\n')
    print('Number of rows: ', dataframe.shape[0])
    print("\nNumber of features:", dataframe.shape[1])
    print("\nData Features:")
    print(dataframe.columns.tolist())
    print("\nMissing values:", dataframe.isnull().sum().values.sum())
    print("\nUnique values:")
    print(dataframe.nunique())


data_dump(dataset, "Ueberblick über Datensatz")
