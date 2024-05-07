import math

import dataSet

class DiscreteMaths(dataSet.DataSet):
    def __init__(self, array1, array2):
        super().__init__(array1, array2)

    def euclidean(self, x, y, x1, y1):
        return math.sqrt((((x - x1)**2) + ((y - y1)**2)))

    def mean(self, array):
        return sum(array) / len(array)

    def standardDeviation(self, array):
        vmean = self.mean(array)
        vlen = len(array)

        aux = [math.pow(abs((array[i] - vmean)), 2) for i in range(vlen)]
        return math.sqrt((sum(aux)) / (vlen - 1))
