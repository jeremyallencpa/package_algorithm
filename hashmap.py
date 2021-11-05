# Class for hashmap. Set initial size to 40 as there are 40 packages that need to be delivered.
class HashMap:
    def __init__(self, size=40):
        self.map = []
        for i in range(size):
            self.map.append([])

    # Function to create a hash key. Time complexity = O(1)
    def create_hash_key(self, key):
        return int(key) % len(self.map)

    # Function to insert a package into the hash table. Time complexity = O(1)
    def insert(self, key, value):
        kh = self.create_hash_key(key)
        kv = [key, value]

        if self.map[kh] == None:
            self.map[kh] = list([kv])
            return True
        else:
            for pair in self.map[kh]:
                if pair[0] == key:
                    pair[1] = kv
                    return True
            self.map[kh].append(kv)
            return True

    # Function to update package in the hash table. Time complexity = O(n)
    def update(self, key, value):
        kh = self.create_hash_key(key)
        if self.map[kh] != None:
            for pair in self.map[kh]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('Error updating key : ' + key)

    # Function to get a value from the hash table. Time complexity = O(n)
    def get_hash_value(self, key):
        kh = self.create_hash_key(key)
        if self.map[kh] != None:
            for pair in self.map[kh]:
                if pair[0] == key:
                    return pair[1]