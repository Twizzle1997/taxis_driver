from classes.predictor import Predictor
from sklearn.ensemble import RandomForestRegressor

class rfr_reg(Predictor):

    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, max_depth=5)
                                