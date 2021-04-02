from credentials import Credentials as cr
import numpy as np
import pandas as pd
import os
import csv
from sklearn.ensemble import IsolationForest

class Functions:
    
    def split_datas_keys(self, file, dirname):
        
        '''
        Break raw data into many files
        '''

        os.makedirs(cr.CURATED_PATH + dirname + os.sep, exist_ok=True)

        csv.field_size_limit(10000000)
        with open(file, encoding='utf-8') as file_stream:
            file_stream_reader = csv.DictReader(file_stream, delimiter=',')
            open_files_references = {}

            for row in file_stream_reader:
                name_of_file = row['key'][:4]
                # Open a new file and write the header
                if name_of_file not in open_files_references:
                    output_file = open(cr.CURATED_PATH + dirname + os.sep + '{}.csv'.format(name_of_file), 'w', encoding='utf-8')
                    dictionary_writer = csv.DictWriter(output_file, fieldnames=file_stream_reader.fieldnames)
                    dictionary_writer.writeheader()
                    open_files_references[name_of_file] = output_file, dictionary_writer
                # Always write the row
                open_files_references[name_of_file][1].writerow(row)
            # Close all the files
            for output_file, _ in open_files_references.values():
                output_file.close()


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