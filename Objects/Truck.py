class Truck:

    def __init__(self, id, packages):
        self.id = id
        self.loadedPackages = packages
        self.distanceTraveled = 0.0

    def __str__(self):
        return " %s, %s, %s" % (
            self.id, self.loadedPackages, self.distanceTraveled)

    def hasMorePackages(self):
        return len(self.loadedPackages) > 0
