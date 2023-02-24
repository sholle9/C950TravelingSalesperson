import csv

"""
    Description: Distance class that holds the distance between two points
    Big O Runtime Complexity: 1
    Big O Space Complexity: 1
"""
class Distance:
    """
        Description: Constructor for Distance
        Big O Runtime Complexity: 1
        Big O Space Complexity: 1
    """
    def __init__(self, addressId, addressName, weights):
        self._addressId = addressId
        self._addressName = addressName
        self._weights = []

    """
        Description: overload of Print function for this object
        Big O Runtime Complexity: 1
        Big O Space Complexity: 1
    """
    def __str__(self):
        return "%s, %s, %s" % (
            self.addressId, self.addressName, self.weights)

    """
        Description: Returns the AddressId of Distance
        Big O Runtime Complexity: 1
        Big O Space Complexity: 1
    """
    def getAddressId(self):
        return self._addressId

"""
    Description: Load Distance information from csv
    Big O Runtime Complexity: n
    Big O Space Complexity: n
"""
def loadDistanceData(distanceArray):
    fileName = '.\DistanceList.csv'
    i = 0

    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        next(distanceData)  # skip header
        for row in distanceData:
            distanceArray.append(row)
