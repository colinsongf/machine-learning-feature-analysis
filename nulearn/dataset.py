__author__ = 'jiachiliu'


import numpy as np

class CsvReader:
    """
    CsvReader will read data from csv file
    """

    def __init__(self, path):
        self.path = path

    def read(self, delimiter, converter):
        f = open(self.path)
        lines = f.readlines()
        return self.parse_lines(lines, delimiter, converter)

    @staticmethod
    def parse_lines(lines, delimiter, converter):
        data = []
        for line in lines:
            if line.strip():
                row = [s.strip() for s in line.strip().split(delimiter) if s.strip()]
                data.append(row)

        return np.array(data, converter)

def load_spambase():
    reader = CsvReader('data/spambase.data')
    data = reader.read(',', float)
    total_col = data.shape[1]
    return data[:, :total_col - 1], data[:, total_col - 1]


def load_polluted_spambase():
    reader = CsvReader('data/spam_polluted/train_feature.txt')
    train = reader.read(' ', float)

    reader = CsvReader('data/spam_polluted/train_label.txt')
    train_target = reader.read(' ', float).flatten()

    reader = CsvReader('data/spam_polluted/test_feature.txt')
    test = reader.read(' ', float)

    reader = CsvReader('data/spam_polluted/test_label.txt')
    test_target = reader.read(' ', float).flatten()

    return train, train_target, test, test_target


def load_20p_missing_spambase():
    reader = CsvReader('data/20_percent_missing_train.txt')
    train = reader.read(',', float)

    reader = CsvReader('data/20_percent_missing_test.txt')
    test = reader.read(',', float)

    total_col = train.shape[1]
    return train[:, :total_col - 1], train[:, total_col - 1], test[:, :total_col - 1], test[:, total_col - 1]