from sklearn.metrics import mean_squared_error, explained_variance_score, max_error, mean_absolute_error

class Predictor():

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)


    def predict(self, data_test):
        data_test["predicted_fare_amount"] = self.model.predict(data_test)
    

    def get_metrics(self, x_test, y_test):

        y_pred = self.model.predict(x_test)

        print("Mean squared error: ", mean_squared_error(y_test, y_pred),
        "\nVariance regression score function: ", explained_variance_score(y_test, y_pred, multioutput='uniform_average'),
        "\nMaximum residual error: ", max_error(y_test, y_pred), 
        "\nMean absolute error regression loss: ", mean_absolute_error(y_test, y_pred, multioutput='uniform_average'))
        
        
