#!/usr/bin/env python

from utils import dataset
from utils import helpers

TRAIN_DATASET = 'data/train.csv'
TEST_DATA = 'data/test.csv'



if __name__ == '__main__':
    # Y_train is array of 0/1 values based on "Prediction" feature (s -> 1, b -> 0)
    # we're ignoring "Id" feature

    Y_train, X_train, indexes = dataset.load_csv_data(TRAIN_DATASET)

    w = helpers.ridge(Y_train, X_train ,1)
    print(len(w), w)

    loss = helpers.compute_loss(Y_train, X_train, w)
    print("loss: ", loss)

    Y_test, X_test, indexes = dataset.load_csv_data(TEST_DATA)
    Y_test = X_test.dot(w)
    print(Y_test[:10])

    Y_test = [1 if e >= 0.0 else -1 for e in Y_test]
    print(Y_test[:10])

    dataset.create_csv_submission(indexes, Y_test, "dot.csv")
    # X_train, Y_train = load_train_dataset(TRAIN_DATASET) NxD
    # X_train, Y_train = clean_dataset("METHOD_NAME", X_train, Y_train)
    # w = logistic_regression(X_train, Y_train)
    # TESTING TIME using w
