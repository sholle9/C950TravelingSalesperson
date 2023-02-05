# This is my header that i will fill in with information like
# Name
# Class
# Date
# Description:

from Objects.HashTable import ChainingHashTable
from Objects.Package import loadPackageData, Package
from Objects.Distance import loadDistanceData, Distance

# Create Hash Tables
packages = ChainingHashTable(40)
trucks = ChainingHashTable()
distances = ChainingHashTable(27)
addresses = ChainingHashTable()

# Initalize tables with Columns
#packages = Package
#trucks = Truck
#distances = Distance

# Load Data into Objects
# Load: packages, trucks, distance
loadPackageData(packages)
loadDistanceData(distances)

#loadTrucks(distances, packages, trucks)



# Fetch data from Hash Table
for i in range (len(packages.table)):
    print("Package: {}".format(packages.search(i+1))) # 1 to 40 is sent to packages.search()

for k in range(len(distances.table)):
    print("Distance: {}".format(distances.search(k+1)))  # 1 to 40 is sent to packages.search()


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
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
