import pandas as pd
def get_dataframe_dtypes(file_path):
    df = pd.read_csv(file_path)
    return df.dtypes

def get_dataframe_shape(f1le_path):
    df = pd.read_csv(file_path)
    return df.shape
