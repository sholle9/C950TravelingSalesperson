"""
Description: The truck class that holds the Id of itself, an array of packages to deliver
, and the total distance travelled
Big O Runtime Complexity: 1
Big O Space Complexity: 1
 """
class Truck:
    """
        Description: Constructor for Truck
        Big O Runtime Complexity: 1
        Big O Space Complexity: 1
    """
    def __init__(self, id, packages):
        self.id = id
        self.loadedPackages = packages
        self.distanceTraveled = 0.0

    """
        Description: Override for print of Truck
        Big O Runtime Complexity: 1
        Big O Space Complexity: 1
    """
    def __str__(self):
        return " %s, %s, %s" % (
            self.id, self.loadedPackages, self.distanceTraveled)

    """
        Description: Determines if the truck still has packages to deliver
        Big O Runtime Complexity: 1
        Big O Space Complexity: 1
    """
    def hasMorePackages(self):
        return len(self.loadedPackages) > 0
