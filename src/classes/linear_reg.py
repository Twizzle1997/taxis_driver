from classes.predictor import Predictor
from sklearn.linear_model import LinearRegression

class linear_reg(Predictor):

    def __init__(self):
        self.model = LinearRegression()
                                