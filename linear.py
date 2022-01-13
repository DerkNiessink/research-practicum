import numpy as np


def linear(data, percentage):
    find = percentage * np.max(data[1])

    for item in data:
        point1 = 0
        if item[1] > find:
            point1 = item[1]
            point2 = data[data.index(point1) - 1]
            break

    a = (point1[1] - point2[1]) / (point1[0] - point2[0])
    b = point1[1] - a * point1[0]

    x_list = []
    y_list = []
    for x in np.arange(point1(0), point2(0), 0.1):
        x_list.append(x)
        y_list.append(a * x + b)

    diff_list = [(find - item, item) for item in y_list]

    return np.min(diff_list)[1]
