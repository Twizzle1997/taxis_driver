import numpy as np

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