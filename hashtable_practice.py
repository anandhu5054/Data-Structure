class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self,key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.Max

    def __getitem__(self,key):
        index = self.get_hash(key)
        for i in self.arr[index]:
            if i[0] == key:
                return i[1]

    def __setitem__(self,key,val):
        index = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[index]):
            if len(element)==2 and element[0] == key:
                self.arr[index][idx] = (key,val)
                found = True
        
        if not found:
            self.arr[index].append((key,val))

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457

