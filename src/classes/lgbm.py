from classes.predictor import Predictor
from lightgbm import LGBMRegressor

class Lgbm_reg(Predictor):

    def __init__(self):
        self.model = LGBMRegressor( objective='regression', num_leaves=1200, learning_rate=0.17, n_estimators=10, max_depth=5)