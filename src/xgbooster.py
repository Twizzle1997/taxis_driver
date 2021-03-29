import xgboost as xgb
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

class Xgb_reg():

    def __init__(self):
        self.model = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 10)
    
    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)


    def predict(self, data_test):
        data_test["predicted_fare_amount"] = self.model.predict(data_test)
    
    def get_accuracy(self, xtrain, ytrain):

        score = self.model.score(xtrain, ytrain)  
        print("Training score: ", score)
        # y_pred = self.model.predict(x_test)
        # return print(self.model.score(y_pred, y_test))

        # kfold = KFold(n_splits=10, random_state=7)
        # results = cross_val_score(xg_reg, X_train, y_train, cv=kfold)
        # y_test_pred = xg_reg.predict(X_test)

        # mse = mean_squared_error(y_test_pred, y_test)
    


        # y_pred = self.model.predict(x_test)
        # predictions = [round(value) for value in y_pred]

        # accuracy = accuracy_score(y_test, predictions, multioutput='variance_weighted')
        # print("Accuracy: %.2f%%" % (accuracy * 100.0))