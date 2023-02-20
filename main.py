# This is my header that i will fill in with information like
# Name
# Class
# Date
# Description:
import datetime

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
    for i in range(len(distances) + 1):
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
        # skip address info in file
        if i == 0:
            continue

        # meaningful comment here
        if minDistance > float(distances[addressId][i]) and float(distances[addressId][i]) != 0:
            minDistance = float(distances[addressId][i])
            addressIdOfShortestDistance = i

    return addressIdOfShortestDistance


def deliverTruck(truck, deliveryStartTime):
    totalDistance: float = 0.0
    now = datetime.datetime.now()
    startingTime = now.replace(hour=8, minute=0, second=0, microsecond=0) + datetime.timedelta(
        minutes=deliveryStartTime)
    timeDelta = datetime.timedelta(minutes=0)
    timeStringFormat = '%H:%M'
    startingAddressName = 'HUB'

    # if truck 3, then update package 9 with new address
    if (startingTime + timeDelta).time() >  datetime.time(hour= 10, minute=20, second=0, microsecond= 0):
        for i in range(len(truck.loadedPackages)):
            if truck.loadedPackages[i] == 9:
                updatePackageNine = packages.search(9)
                updatePackageNine.address = "410 S State St(84111)"

    while truck.hasMorePackages():
        shortestDistance = float(100)


        # find package to deliver
        for i in range(len(truck.loadedPackages)):

            # get package number from truck list
            packageID = int(truck.loadedPackages[i])

            # associated int with the packageID from the packages hash table
            package = packages.search(packageID)

            # find addressName associated with package address from the distanceArray
            addressName = package.address

            # check to see if I'm the nearest package
            if shortestDistance > getDistancesBetweenAddresses(startingAddressName,addressName) and getDistancesBetweenAddresses(startingAddressName, addressName) != 0.0:
                shortestDistance = getDistancesBetweenAddresses(startingAddressName, addressName)
                packageIdToDeliver = packageID

        totalDistance = float(totalDistance + shortestDistance)

        # after we find the nearest package. deliver package which updates the package status and the time
        # remove package(s) from truck
        packageToUpdate = packages.search(packageIdToDeliver)

        # Initalized Array for the other packages with same address as the packageIdToDeliver
        packagesToDeliver = []

        # Grouping packages with same address
        for i in range(len(truck.loadedPackages)):
            # get package number from truck list
            packageID = int(truck.loadedPackages[i])

            # associated int with the packageID from the packages hash table
            package = packages.search(packageID)

            if packageToUpdate.address == package.address:
                packagesToDeliver.append(packageID)

        # Time delivered is calculated by the distances traveled by the truck times 18 mph
        minutesToTravel = shortestDistance / (18 / 60)
        timeDelta = timeDelta + datetime.timedelta(minutes=minutesToTravel)

        # Updating statuses based on time
        for i in range(len(packagesToDeliver)):
            packageToUpdate = packages.search(packagesToDeliver[i])

            # update time delivered
            packageToUpdate.timeDelivered = startingTime + timeDelta

            # check to see if we have delivered the package on time
            if packageToUpdate.deadline != "EOD":
                parsedPackageToUpdateDeadlineTime = datetime.datetime.strptime(packageToUpdate.deadline, timeStringFormat).time()
                if packageToUpdate.timeDelivered.time() > parsedPackageToUpdateDeadlineTime:
                    packageToUpdate.status = "Delivered Late"
                else:
                    packageToUpdate.status = "Delivered On Time"
            else:
                packageToUpdate.status = "Delivered On Time"

            # find position in loaded truck array to delete because the array may have changed sizes if delivering
            # multiple packages to the same address
            for k in range(len(truck.loadedPackages)):
                if packageToUpdate.id == truck.loadedPackages[k]:
                    positionInArray = k
                    break

            startingAddressName = packageToUpdate.address

            # deliver package
            truck.loadedPackages.pop(positionInArray)

        truck.distanceTraveled += shortestDistance

        # time to go back and get the other packages
        print(truck)
        print(packagesToDeliver)

    if truck.id == 1:
        truck.distanceTraveled += getDistancesBetweenAddresses(packageToUpdate.address, "HUB")

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
#
truck1 = Truck(1, [4, 13, 14, 15, 16, 17, 19, 20, 21, 26, 34, 39, 40])
truck2 = Truck(2, [1, 3, 6, 7, 8, 10, 18, 25, 29, 30, 31, 32, 36, 37, 38])
truck3 = Truck(3, [2, 5, 9, 11, 12, 22, 23, 24, 27, 28, 33, 35])

deliverTruck(truck1, 0)
deliverTruck(truck2, 65)
deliverTruck(truck3, 150)
# Fetch data from Hash Table
for i in range(len(packages.table)):
    print("Package: {}".format(packages.search(i + 1)))  # 1 to 40 is sent to packages.search()

print(truck1, truck2, truck3)
print(truck1.distanceTraveled + truck2.distanceTraveled + truck3.distanceTraveled)
