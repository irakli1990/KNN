import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt

PATH_DATASET_EXEL = 'data/dataset.xlsx'
PATH_DATASET_CSV = 'data/dataset.csv'


def load_csv(path):
    read_file = pd.read_excel(path, 1)
    read_file.to_csv(PATH_DATASET_CSV, index=None, header=True)
    df = pd.DataFrame(pd.read_csv(PATH_DATASET_CSV))
    return df


def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)


def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


if __name__ == '__main__':
    dataframe = load_csv(PATH_DATASET_EXEL)
    print(dataframe.columns.values)
    print(dataframe.values)
    dataset = dataframe.iloc[:, [0, 1, 2, 3]].values
    print(euclidean_distance(dataset[0], dataset[1]))
    neighbors = get_neighbors(dataset, dataset[0], 5)

    for neighbor in neighbors:
        print(neighbor)
    plt.show()
