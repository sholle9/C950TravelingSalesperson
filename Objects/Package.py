import csv
"""
    Description: Package class that contains the information about a package
    Big O Runtime Complexity: 1
    Big O Space Complexity: 1
"""
class Package:
    """
        Description: Constructor for Package
        Big O Runtime Complexity: 1
        Big O Space Complexity: 1
    """
    def __init__(self, id, address, city, state, zipCode, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.timeDelivered = 0

    """
        Description: overload of Print function for this object
        Big O Runtime Complexity: 1
        Big O Space Complexity: 1
    """
    def __str__(self):
        return " %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zipCode, self.deadline, self.weight, self.status, self.timeDelivered)

"""
    Description: Load package information from csv
    Big O Runtime Complexity: n
    Big O Space Complexity: n
"""
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
            pZipCode = int(package[4])
            pDeadline = str(package[5])
            pWeight = int(package[6])
            pStatus = 'At the HUB'

            p = Package(pID, pAddress, pCity, pState, pZipCode, pDeadline, pWeight, pStatus)
            packageHashTable.insert(pID, p)
