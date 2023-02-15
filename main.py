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

# loadTrucks(distances, packages, trucks)
# def loadTrucks(distances, packages, trucks):
#     packageIdToInsert = random.randint(0, len(packages.table) - 1)
#     trucks.insert(0,packages.table[packageIdToInsert][0][0])
#     while True:
#         #look up closest package by distance to current package
#         distances[]
#
#         #add to array
#         #once we hit 8 packages, break

def getIndexForAddress(addressToFind):
    # Loop through the distanceArray comparing element 0
    for i in range(len(distances)+1):
        if distances[i][0] == addressToFind:
            return i
    pass

def getDistancesBetweenAddresses(startAddress, endAddress):
    startingIndex = getIndexForAddress(startAddress)
    endIndex = getIndexForAddress(endAddress) + 1
    return distances[startingIndex][endIndex]

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

print(getShortestDistanceFromAddress(26))

def deliverTruck(truck):

    while truck.hasMorePackages():
        shortestDistance = 100
        startingAddressId = 0
        packageIdToDeliver = 0

        #if len(truck.loadedPackages == 1):
            #deliver the last package
            #deliverPackage(truck.loadedPackages[0])

        for packageID in range(len(truck.loadedPackages)):
            # check to see if I'm the nearest package
            # get package
            package = packages.search(packageID)

            # find addressId associated with package address
            addressId = getIndexForAddress(package.address)

            # package with the address closest to this one
            if shortestDistance > getDistancesBetweenAddresses(startingAddressId, addressId):
                startingAddressId = addressId
                packageIdToDeliver = packageID

        # after we find nearest package. deliver package
        #deliverPackage(packageIdToDeliver)
        # remove package from truck
        #removeFromTruck(truck, packageId)





    pass
        # update nearest package as delivered
        # Don't forget to remove the packageID from truck._loadedPackages - infinite loop

truck1 = Truck(1, [5, 7, 15])
deliverTruck(truck1)

# deliverTruck(truck1)
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

# Fetch data from Hash Table
# for i in range(len(packages.table)):
#     print("Package: {}".format(packages.search(i + 1)))  # 1 to 40 is sent to packages.search()
# for k in range(len(distances)):
#     print("Distance: {}".format(distances[k]))  # 1 to 40 is sent to packages.search()
#
# for j in range(len(addresses)):
#     print("Address: {}".format(addresses[j]))  # 1 to 40 is sent to packages.search()


print(getIndexForAddress('6351 South 900 East(84121)'))
print(getDistancesBetweenAddresses('6351 South 900 East(84121)', 'HUB'))
print(distances[26][1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
