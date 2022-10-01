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
    def insert(self, item):
        # get the node list where this item will go.
        node = hash(item) % len(self.table)
        node_list = self.table[node]

        # insert the item to the end of the node list.
        node_list.append(item)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the node list where this key would be.
        node = hash(key) % len(self.table)
        node_list = self.table[node]

        # search for the key in the node list
        if key in node_list:
            # find the item's index and return the item that is in the node list.
            item_index = node_list.index(key)
            return node_list[item_index]
        else:
            # the key is not found.
            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the node list where this item will be removed from.
        node = hash(key) % len(self.table)
        node_list = self.table[node]

        # remove the item from the node list if it is present.
        if key in node_list:
            node_list.remove(key)