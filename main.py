"""
Name: Stephanie Katuzienski
Class: C950
Date: 2/20/23
Description:    Deliver trucks using the greedy algorithm.
                Also provide the status of all packages at a given point in time.
"""
import datetime

from Objects.HashTable import ChainingHashTable
from Objects.Package import loadPackageData, Package
from Objects.Distance import loadDistanceData, Distance

from Objects.Truck import Truck

# Create Hash Tables
packages = ChainingHashTable(40)
trucks = []
distances = []
addresses = []




"""
Description: get the address Id associated with a given Address
Big O Runtime Complexity: n
Big O Space Complexity: n
 """
def getIndexForAddress(addressToFind):
    # Loop through the distanceArray comparing element 0
    for i in range(len(distances) + 1):
        if distances[i][0] == addressToFind:
            return i
    pass


"""
Description: Find the distance between two addresses
Big O Runtime Complexity: 1
Big O Space Complexity: 1
 """
def getDistancesBetweenAddresses(startAddress, endAddress):
    startingIndex = getIndexForAddress(startAddress)
    endIndex = getIndexForAddress(endAddress) + 1
    return float(distances[startingIndex][endIndex])


"""
Description:    Deliver truck takes the truck, a delivery start time, and a status time as parameters
                It looks through the packages in the trucks and uses a greedy algorithm to determine which package
                to deliver next. It also looks to see if Status time is passed. if so, it will provide the status of all
Big O Runtime Complexity: n^3
Big O Space Complexity: n^3
 """
def deliverTruck(truck, deliveryStartTime, statusTime):
    totalDistance: float = 0.0
    now = datetime.datetime.now()
    startingTime = now.replace(hour=8, minute=0, second=0, microsecond=0) + datetime.timedelta(
        minutes=deliveryStartTime)
    timeDelta = datetime.timedelta(minutes=0)
    startingAddressName = 'HUB'

    # check to see if we have to provide status update
    if statusTime != None and (startingTime + timeDelta).time() >= statusTime:
        return

    # set all packages on truck to in Route
    for i in range(len(truck.loadedPackages)):
        packageToUpdate = packages.search(truck.loadedPackages[i])
        packageToUpdate.status = "In Route"

    # if truck 3, then update package 9 with new address
    if (startingTime + timeDelta).time() >= datetime.time(hour=10, minute=20, second=0, microsecond= 0):
        for i in range(len(truck.loadedPackages)):
            if truck.loadedPackages[i] == 9:
                updatePackageNine = packages.search(9)
                updatePackageNine.address = "410 S State St(84111)"

    # big loop
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

            # update Delivery Status
            packageToUpdate.status = "Delivered"

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

        # check to see if we have to provide status update
        if statusTime != None and (startingTime + timeDelta) != 0.0 and (startingTime + timeDelta).time() >= statusTime:
            for i in range(len(packages.table)):
                packageToFix = packages.search((i + 1))
                if packageToFix.timeDelivered != 0:
                    if packageToFix.timeDelivered.time() >= statusTime:
                        packageToFix.status = "In Route"
                        packageToFix.timeDelivered = 0

            return


    if truck.id == 1:
        # time to go back and get the other packages
        truck.distanceTraveled += getDistancesBetweenAddresses(packageToUpdate.address, "HUB")

    return totalDistance

"""
Description:    Menu for user to operate program
Big O Runtime Complexity: n
Big O Space Complexity: n
 """
def menu():
    print("Option: 1 Deliver Truck")
    print("Option: 2 Check Status of Packages")
    print("Option 0: Exit")

    option = int(input("Choose option: "))

    # Load Data into Objects
    # Load: packages, trucks, distance
    loadDistanceData(distances)
    loadPackageData(packages)
    while True:
        if option == 1:

            # Load trucks with packages
            truck1 = Truck(1, [4, 13, 14, 15, 16, 17, 19, 20, 21, 26, 34, 39, 40])
            truck2 = Truck(2, [1, 3, 6, 7, 8, 10, 18, 25, 29, 30, 31, 32, 36, 37, 38])
            truck3 = Truck(3, [2, 5, 9, 11, 12, 22, 23, 24, 27, 28, 33, 35])

            # Deliver trucks
            deliverTruck(truck1, 0, None)
            deliverTruck(truck2, 65, None)
            deliverTruck(truck3, 150, None)

            # Output
            print("\nDelivering Packages")
            print("\nPackages Delivered")
            for i in range(len(packages.table)):
                print("Package: {}".format(packages.search(i + 1)))  # 1 to 40 is sent to packages.search()

            print(f"Truck 1 Distance: {truck1.distanceTraveled}\nTruck 2 Distance: "
                  f"{truck2.distanceTraveled}\nTruck 3 Distance: {truck3.distanceTraveled}")
            print(f"Total Distance {truck1.distanceTraveled + truck2.distanceTraveled + truck3.distanceTraveled}")
            print()
            menu()

        elif option == 2:
            print("Enter Time to Check the Status of Packages: ")
            hour = int(input("Hour: "))
            minutes = int(input("Minutes: "))

            # Load and deliver packages in trucks. then check times that they were delivered, print status
            # Load trucks with packages
            truck1 = Truck(1, [4, 13, 14, 15, 16, 17, 19, 20, 21, 26, 34, 39, 40])
            truck2 = Truck(2, [1, 3, 6, 7, 8, 10, 18, 25, 29, 30, 31, 32, 36, 37, 38])
            truck3 = Truck(3, [2, 5, 9, 11, 12, 22, 23, 24, 27, 28, 33, 35])

            # Deliver trucks
            deliverTruck(truck1, 0, datetime.time(hour= hour, minute = minutes))
            deliverTruck(truck2, 65, datetime.time(hour = hour, minute = minutes))
            deliverTruck(truck3, 150, datetime.time(hour = hour, minute = minutes))

            for i in range(len(packages.table)):
                print("Package: {}".format(packages.search(i + 1)))
            print()
            menu()
        elif option == 0:
            break
        else:
            print("Try again")
            print()
            menu()

menu()

