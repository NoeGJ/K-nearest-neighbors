import math

class DiscreteMath:

    def euclidean(self, xNewValue, yNewValue, x, y):
        return math.sqrt((((xNewValue - x)**2) + ((yNewValue - y)**2)))

    def mean(self, array):
        return sum(array) / len(array)

    def standardDeviation(self, array):
        vmean = self.mean(array)
        vlen = len(array)

        aux = [abs((array[i] - vmean))**2  for i in range(vlen)]
        return math.sqrt((sum(aux)) / (vlen - 1))
