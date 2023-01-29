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

    def __str__(self, id, address, city, state, zip, deadline, weight, status):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self._id, self._address, self._city, self._state, self._deadline, self._weight, self._status)

    # def id(self):
    #     return self._id
    #
    # def address(self):
    #     return self._address
    #
    # def city(self):
    #     return self._city
    #
    # def state(self):
    #     return self._state
    #
    # def zip(self):
    #     return self._zip
    #
    # def deadline(self):
    #     return self._deadline
    #
    # def weight(self):
    #     return self._weight
    #
    # def status(self):
    #     return self._status


def loadPackageData(fileName):
    with open(fileName) as packages:
        myHash = ChainingHashTable()
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
            myHash.insert(pID, p)

        print(myHash.table)
