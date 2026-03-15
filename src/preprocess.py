import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    df['Hour'] = df['Timestamp'].dt.hour
    df['Month'] = df['Timestamp'].dt.month

    df.drop('Timestamp', axis=1, inplace=True)

    df['Holiday'] = df['Holiday'].map({'Yes':1,'No':0})

    return df
