import csv

from Objects.HashTable import ChainingHashTable


class Package:

    def __init__(self, id, address, city, state, zip, deadline, weight, status):
        self._id = id
        self._address = address
        self._city = city
        self._state = state
        self._zip = zip
        self._deadline = deadline
        self._weight = weight
        self._status = status

    def __str__(self):
        return " %s, %s, %s, %s, %s, %s, %s, %s" % (
            self._id, self._address, self._city, self._state, self._zip, self._deadline, self._weight, self._status)


def loadPackageData(packageHashTable):
    fileName = 'C:\dev\SKatuzienski_TaskC950\PackageList.csv'
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)  # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = str(package[1])
            pCity = str(package[2])
            pState = str(package[3])
            pZip = int(package[4])
            pDeadline = str(package[5])
            pWeight = int(package[6])
            pStatus = 'TBD'

            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pStatus)
            packageHashTable.insert(pID, p)

