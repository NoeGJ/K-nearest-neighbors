from kNearestNeighbor import kNearestNeighbor


class HandsOn4:
    def __init__(self):
        k = 5
        # height in cms
        self.height = [158, 158, 158, 160, 160, 163, 163, 160, 163, 165, 165, 165, 168, 168, 168, 170, 170, 170]
        # weight in kgs
        self.weight = [58, 59, 63, 59, 60, 60, 61, 64, 64, 61, 62, 65, 62, 63, 66, 63, 64, 68]
        # T shirt size [M, L]
        self.tShirtSize = ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']
        # new data
        self.newData = [161, 61]

        knn = kNearestNeighbor( k )
        heightStand = knn.standardization(self.height, self.newData[0])
        weightStand = knn.standardization(self.weight, self.newData[1])

        #print(heightStand)
        #print(weightStand)

        newDataStand = [heightStand.pop(), weightStand.pop()]
        #print(newDataStand)

        xy = [[i, j] for i, j in zip(heightStand, weightStand)]
        #print(xy)
        distances = knn.computedDistances(xy, newDataStand)
        #print(distances)

        cat = knn.findKNearestNeighbor(self.tShirtSize, distances)
        print("Los valores", self.newData, "corresponden a", cat)


if __name__ == "__main__":
    HandsOn4()