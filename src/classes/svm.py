from classes.predictor import Predictor
from sklearn.svm import SVR

class Svm_reg(Predictor):

    def __init__(self):
        self.model = SVR(C=0.3)