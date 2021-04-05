# Taxis Driver Project ! 

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
  * [Model classes](#model-classes)
* [Special Thanks](#special-thanks)

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [Python](https://www.python.org/)
* [Jupyter Notebook](https://jupyter.org/)
* [Scikit-Learn](https://scikit-learn.org/stable/)

<!-- GETTING STARTED -->
## Getting Started

Get a local copy up and running following these steps.

### Installation

1. Clone the repository :

    ```sh
    git clone https://github.com/Twizzle1997/taxis_driver
    ```
    
2. If you want to run the notebook, install the requirements : 
    ```sh
    conda env update --name <envname> --file environment.yml
    ```


<!-- USAGE EXAMPLES -->
## Usage

* launch [src/notebook.ipynb](https://github.com/Twizzle1997/taxis_driver/blob/main/src/notebook.ipynb) to see the work and analysis.  

### Model classes
* ```/src/classes/predictor.py``` *[parent class]* machine learning methods.  
* ```/src/classes/gxboost.py``` *[parent : Predictor]* [XGBoost model](https://xgboost.readthedocs.io/en/latest/).   
* ```/src/classes/lgbm.py``` *[parent : Predictor]* [LightGBM model](https://lightgbm.readthedocs.io/en/latest/).  
* ```/src/classes/linear_reg.py``` *[parent : Predictor]* [Linear Regression model](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html).  
* ```/src/classes/randomforest.py``` *[parent : Predictor]* [Random Forest Regressor model](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html).  
* ```/src/classes/svm.py``` *[parent : Predictor]* [Support Vector Regression model](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html) (not used).  

## Special Thanks 
Special thanks to [@David K.](https://github.com/KRDavid) for his precious help. Hug Hug.
