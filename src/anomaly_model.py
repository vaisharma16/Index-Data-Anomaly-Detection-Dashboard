# src/anomaly_model.py
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

def detect_anomalies(df, contamination=0.03):
    """
    Detect anomalies using Isolation Forest on price and volume features.
    """
    df = df.copy()
    features = ['Open', 'High', 'Low', 'Close', 'Volume']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])

    model = IsolationForest(contamination=contamination, random_state=42)
    df['anomaly_score'] = model.fit_predict(X_scaled)
    df['anomaly_flag'] = df['anomaly_score'].apply(lambda x: 1 if x == -1 else 0)

    return df[df['anomaly_flag'] == 1][['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

if __name__ == '__main__':
    df = pd.read_csv('data/sample_index_data.csv')
    anomalies = detect_anomalies(df)
    print("\nAnomalies detected:\n", anomalies)
