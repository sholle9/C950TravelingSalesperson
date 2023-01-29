# This is a sample Python script.
import csv

from Objects.HashTable import ChainingHashTable
from Objects.Package import loadPackageData

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


loadPackageData('C:\dev\SKatuzienski_TaskC950\PackagesList.csv')



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
