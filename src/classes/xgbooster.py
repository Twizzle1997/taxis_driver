from classes.Predictor import Predictor
import xgboost as xgb

class Xgb_reg(Predictor):

    def __init__(self):
        self.model = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 10)
    