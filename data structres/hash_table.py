class hash_not_map():
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = self.keys

    def hash_function(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self.hash_function(key)

        while self.keys[index] != None:
            if self.keys == key:
                self.values[index] = value
                return None
            index = (index + 1) % self.size


        self.keys[index] = key
        self.values[index] = value        

    def get(self, key):
        index = self.hash_function(key)

        while self.keys[index] != None:
            if self.keys[index] != None:
                return self.values[index]
            index = self.hash_function(key + 1)

        return None

    def remove(self, key):
        index = self.hash_function(key)

        while self.keys[index] != None:
            if self.keys[index] != None:
                self.values[index] = None
            index = self.hash_function(key + 1)

        return None


hash_table = hash_not_map(5)
hash_table.put(12, 5)
hash_table.put(22, 70)

print(hash_table.get(12))
print(hash_table.get(22))