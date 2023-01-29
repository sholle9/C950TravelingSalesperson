# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all nodes with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty node list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item):  # does both insert and update 
        # get the node list where this item will go.
        node = hash(key) % len(self.table)-1
        node_list = self.table[node]

        # update key if it is already in the node
        for kv in node_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the node list.
        key_value = [key, item]
        node_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the node list where this key would be.
        node = hash(key) % len(self.table)-1
        node_list = self.table[node]

        # search for the key in the bucket list
        for kv in node_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        node = hash(key) % len(self.table)-1
        node_list = self.table[node]

        # remove the item from the bucket list if it is present.
        for kv in node_list:
            # print (key_value)
            if kv[0] == key:
                node_list.remove([kv[0], kv[1]])

