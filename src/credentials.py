import os

class Credentials:
    DATA_PATH = ".." + os.sep + "data" + os.sep
    DATA_TRAIN = DATA_PATH + "train.csv"
    DATA_TEST = DATA_PATH + "test.csv"
    CURATED_PATH = ".." + os.sep + "curated" + os.sep
    CURATED_TRAIN = CURATED_PATH + "train" + os.sep
    CURATED_TEST = CURATED_PATH + "test" + os.sep