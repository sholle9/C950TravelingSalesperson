import random

class Truck:

    def __init__(self, id, packages):
        self.id = id
        self.loadedPackages = packages

    def __str__(self):
        return " %s, %s" % (
            self.id, self.loadedPackages)

    def hasMorePackages(self):
        return len(self.loadedPackages) > 0
