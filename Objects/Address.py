import csv
from array import array

class Address:

    def __init__(self, id, address):
        self._id = id
        self._address = address

    def __str__(self):
        return " %s, %s" % (
            self._id, self._address)


def loadAddressData(addressArray):
    fileName = 'C:\dev\SKatuzienski_TaskC950\AddressList.csv'

    with open(fileName) as addresses:
        addressData = csv.reader(addresses, delimiter=',')
        next(addressData)  # skip header
        for address in addressData:
            aID = int(address[0])
            aAddress = str(address[1])
            a = (aID, aAddress)
            addressArray.insert(aID, a)