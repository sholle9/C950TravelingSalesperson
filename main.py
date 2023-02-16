# This is my header that i will fill in with information like
# Name
# Class
# Date
# Description:

from Objects.HashTable import ChainingHashTable
from Objects.Package import loadPackageData, Package
from Objects.Distance import loadDistanceData, Distance
from Objects.Address import loadAddressData, Address
import random

from Objects.Truck import Truck



# Create Hash Tables
packages = ChainingHashTable(40)
trucks = []
distances = []
addresses = []


# Load Data into Objects
# Load: packages, trucks, distance
loadAddressData(addresses)
loadDistanceData(distances)
loadPackageData(packages)

def getIndexForAddress(addressToFind):
    # Loop through the distanceArray comparing element 0
    for i in range(len(distances)+1):
        if distances[i][0] == addressToFind:
            return i
    pass

# getDistancesBetweenAddresses uses two address strings
def getDistancesBetweenAddresses(startAddress, endAddress):
    startingIndex = getIndexForAddress(startAddress)
    endIndex = getIndexForAddress(endAddress) + 1
    return float(distances[startingIndex][endIndex])

def getShortestDistanceFromAddress(addressId):
    minDistance = 100.0
    addressIdOfShortestDistance = 0

    for i in range(len(distances[addressId])):
        #skip address info in file
        if i == 0:
            continue

        #meaningful comment here
        if minDistance > float(distances[addressId][i]) and float(distances[addressId][i]) != 0:
            minDistance = float(distances[addressId][i])
            addressIdOfShortestDistance = i

    return addressIdOfShortestDistance

def deliverTruck(truck):

    totalDistance: float = 0.0
    while truck.hasMorePackages():
        shortestDistance = float(100)
        startingAddressName = 'HUB'

        #if len(truck.loadedPackages == 1):
            #deliver the last package
            #deliverPackage(truck.loadedPackages[0])

        for i in range(len(truck.loadedPackages)):
            # get package number from truck list
            packageID = int(truck.loadedPackages[i])

            # associated int with the packageID from the packages hash table
            package = packages.search(packageID)

            # find addressName associated with package address from the distanceArray
            addressName = package.address

            # check to see if I'm the nearest package
            if shortestDistance > getDistancesBetweenAddresses(startingAddressName, addressName) and getDistancesBetweenAddresses(startingAddressName, addressName) != 0:
                shortestDistance = getDistancesBetweenAddresses(startingAddressName, addressName)
                packageInTruck = i
                packageIdToDeliver = packageID

        totalDistance = float (totalDistance + shortestDistance)

        # after we find the nearest package. deliver package which updates the package status and the time


        # remove package(s) from truck
        packageToUpdate = packages.search(packageIdToDeliver)

        #find other packages with same address
        packagesToDeliver = []
        for i in range(len(truck.loadedPackages)):
            # get package number from truck list
            packageID = int(truck.loadedPackages[i])

            # associated int with the packageID from the packages hash table
            package = packages.search(packageID)
            if packageToUpdate.address == package.address:
                packagesToDeliver.append(packageID)

        for i in range(len(packagesToDeliver)):
            packageToUpdate = packages.search(packagesToDeliver[i])
            # update status to "Delivered"
            packageToUpdate.status = "Delivered"

            # Time delivered is calculated by the distances traveled by the truck times 18 mph
            packageToUpdate.timeDelivered = totalDistance * (18 / 60)
            truck.loadedPackages.pop(packageInTruck)

        print(truck)
        print(packagesToDeliver)
    return totalDistance

def menu():
    print("Option: 1")
    print("Option: 2")
    print("Option: 3")
    print("Option: 4")
    print("Option: 5")
    print("Option 0: Exit")

    menu()
    option = int(input("Choose option: "))

    while option != 0:
        if option == 1:
            # do option 1 stuff
            print("Yay! Option 1")
        elif option == 2:
            # do option 2 stuff
            print("Yay! Option 2")
        elif option == 3:
            # do option 3 stuff
            print("Yay! Option 3")
        elif option == 4:
            # do option 4 stuff
            print("Yay! Option 4")
        elif option == 5:
            # do option 5 stuff
            print("Yay! Option 5")
        else:
            # freakout
            print("Boo! Try again")

        print()
        menu()
        option = int(input("Choose option: "))

    print("See ya!")

# for k in range(len(distances)):
#     print("Distance: {}".format(distances[k]))  # 1 to 40 is sent to packages.search()
#
# for j in range(len(addresses)):
#     print("Address: {}".format(addresses[j]))  # 1 to 40 is sent to packages.search()

truck1 = Truck(1, [7, 29, 1, 11, 31, 32, 12, 20, 21, 4, 40, 14, 15, 16, 34, 23])
truck2 = Truck(2, [27, 35, 18, 13, 39, 36, 3, 8, 9, 30, 6, 5, 37, 38, 25, 26])
truck3 = Truck(3, [19, 2, 33, 28, 17, 24, 10, 22])

print(deliverTruck(truck1) + deliverTruck(truck2) + deliverTruck(truck3))

# Fetch data from Hash Table
for i in range(len(packages.table)):
    print("Package: {}".format(packages.search(i + 1)))  # 1 to 40 is sent to packages.search()