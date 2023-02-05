import csv

class Distance:

    def __init__(self, distanceId, address1Id, address1Name, address2Id, address2Name, weight):
        self._distanceId = distanceId
        self._address1 = (address1Id, address1Name)
        self._address2 = (address2Id, address2Name)
        self._weight = weight

#Return String for dictionary for distances
    def __str__(self,distanceId, address1, address2, weight):
        return "%s, %s,%s, %s" % (
            self._distanceId, self._address1 , self._address2 , self._weight)

# # iterate through rows in csv file and assign values to dictionaries
#     for i, row in enumerate(csv_reader):
#         address1['id'] = i
#         address1['name'] = row[0]
#         address2['id'] = i
#         address2['name'] = row[1]
#
# def loadDistanceData(distanceHashTable):
#     fileName = 'C:\dev\SKatuzienski_TaskC950\DistanceList.csv'
#     i = 0
#     with open(fileName) as distances:
#         distanceData = csv.reader(distances, delimiter=',')
#         next(distanceData)  # skip header
#         for row in distanceData:
#             for column in row
#
#
#             d = Distance()
#             packageHashTable.insert(dID, d)
#
