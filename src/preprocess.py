import pandas as pd

def load_data(path):

    df = pd.read_csv(path)

    # Convert timestamp to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Extract time features
    df['Hour'] = df['Timestamp'].dt.hour
    df['Month'] = df['Timestamp'].dt.month

    # Drop timestamp
    df.drop('Timestamp', axis=1, inplace=True)

    # Convert categorical columns to numeric
    df['HVACUsage'] = df['HVACUsage'].map({'On':1, 'Off':0})
    df['LightingUsage'] = df['LightingUsage'].map({'On':1, 'Off':0})
    df['Holiday'] = df['Holiday'].map({'Yes':1, 'No':0})

    # Convert DayOfWeek
    df['DayOfWeek'] = df['DayOfWeek'].map({
        'Monday':1,
        'Tuesday':2,
        'Wednesday':3,
        'Thursday':4,
        'Friday':5,
        'Saturday':6,
        'Sunday':7
    })

    return df
