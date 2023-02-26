"""
    Description: Create a hashtable using Chaining
    Big O Runtime Complexity: O(n)
    Big O Space Complexity: O(n)
"""
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all nodes with an empty list.
    """
        Description: Initalize Chaining Hash Table with a given size
        Big O Runtime Complexity: O(n)
        Big O Space Complexity: O(n)
    """
    def __init__(self, initialCapacity=10):
        # initialize the hash table with empty node list entries.
        self.table = []
        for i in range(initialCapacity):
            self.table.append([])

    """
        Description: Inserts a new item into the hash table.
        Big O Runtime Complexity: O(n)
        Big O Space Complexity: O(n)
    """
    def insert(self, key, item):  # does both insert and update 
        # get the node list where this item will go.
        node = hash(key) % len(self.table)-1
        nodeList = self.table[node]

        # update key if it is already in the node
        for kv in nodeList:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the node list.
        key_value = [key, item]
        nodeList.append(key_value)
        return True

    """
        Description: Searches for an item with matching key in the hash table.
        Big O Runtime Complexity: O(n)
        Big O Space Complexity: O(n)
    """
    def search(self, key):
        # get the node list where this key would be.
        node = hash(key) % len(self.table)-1
        nodeList = self.table[node]

        # search for the key in the bucket list
        for kv in nodeList:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    """
        Description: Removes an item with matching key from the hash table.
        Big O Runtime Complexity: O(n)
        Big O Space Complexity: O(n)
    """
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        node = hash(key) % len(self.table)-1
        nodeList = self.table[node]

        # remove the item from the bucket list if it is present.
        for kv in nodeList:
            # print (key_value)
            if kv[0] == key:
                nodeList.remove([kv[0], kv[1]])

