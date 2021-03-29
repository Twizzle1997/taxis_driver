import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

class Functions:
    def compute_distance(lat1, lon1, lat2, lon2):
        R = 6372800  # Earth radius in meters

        lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1 
        dlon = lon2 - lon1 
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arcsin(np.sqrt(a)) 
        total_distance = 6372800 * c
        return total_distance/1000

    def isolation_forest(in_file, out_file):
        df = pd.read_csv(in_file)

        model = IsolationForest(n_estimators = 100, max_samples = 'auto', contamination = 'auto', max_features = 1)
        model.fit(df[['passenger_count','distance_km','fare_amount']])

        df['scores'] = model.decision_function(df[['passenger_count','distance_km','fare_amount']])
        df['anomaly'] = model.predict(df[['passenger_count','distance_km','fare_amount']])
        print(df.head(10))

        df.to_csv(out_file)