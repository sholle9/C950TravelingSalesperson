import csv


class Distance:

    def __init__(self, addressId, addressName, weights):
        self._addressId = addressId
        self._addressName = addressName
        self._weights = (weights[0], weights[1], weights[2], weights[3], weights[4], weights[5], weights[6], weights[7], weights[8], weights[9],
                         weights[10], weights[11], weights[12], weights[13], weights[14], weights[15], weights[16], weights[17], weights[18], weights[19],
                         weights[20], weights[21], weights[22], weights[23], weights[24], weights[25], weights[26])

    # Return String for dictionary for distances
    def __str__(self):
        return "%s, %s, %s" % (
            self._addressId, self._addressName, self._weights)

def loadDistanceData(distanceHashTable):
    fileName = 'C:\dev\SKatuzienski_TaskC950\DistanceList.csv'
    i = 0
    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        next(distanceData)  # skip header
        for row in distanceData:
            dID = i = i + 1
            dName = row[0]
            dWeights = (row[1],	row[2],	row[3],	row[4],	row[5],	row[6],	row[7],	row[8],
                        row[9],	row[10], row[11], row[12], row[13],	row[14], row[15], row[16],
                        row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24],
                        row[25], row[26], row[27])
            d = Distance(dID, dName, dWeights)
            distanceHashTable.insert(dID, d)





