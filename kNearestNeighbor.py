from collections import Counter
import discreteMaths

class kNearestNeighbor(discreteMaths.DiscreteMaths):
    def __init__(self, k = 2):
        #super().__init__(array1, array2)
        self.k = k

    def standardization(self, array, newData):
        vmean = self.mean(array)
        vstanddev = self.standardDeviation(array)

        newList =[(array[i] - vmean) / vstanddev for i in range(len(array))]
        newList.append( (newData - vmean) / vstanddev )
        return newList

    def computedDistances(self, xy, new):
        return [ self.euclidean(new[0], new[1], i, j) for i, j in xy ]

    def findKNearestNeighbor(self, categories, distances):
        listNeighbor = [[i, j] for i, j in zip(categories, distances)]
        #print(listNeighbor)

        sortedList = sorted(listNeighbor, key=lambda x: x[1])
        del sortedList[self.k:]
        #print(sortedList)
        count = Counter()

        for i in sortedList:
            count[i[0]] += 1

        category = max(count, key=count.get)

        return category
