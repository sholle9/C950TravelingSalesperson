import csv
from array import array


class Distance:
    # Created a tuple for the weights.
    # First int represents the addressID of the destination and the second float is the distance between the two points.
    def __init__(self, addressId, addressName, weights):
        self._addressId = addressId
        self._addressName = addressName
        self._weights = []

    # Return String for dictionary for distances
    def __str__(self):
        return "%s, %s, %s" % (
            self.addressId, self.addressName, self.weights)

    def getAddressId(self):
        return self._addressId


def loadDistanceData(distanceArray):
    fileName = 'C:\dev\SKatuzienski_TaskC950\DistanceList.csv'
    i = 0

    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        next(distanceData)  # skip header
        for row in distanceData:
            distanceArray.append(row)
