class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range(self.Max)]

    def get_hash(self,key):
        h=0
        for i in key:
            h+= ord(i)
        return h % self.Max

    def __setitem__(self,key,val):
        index = self.get_hash(key)
        self.arr[index] = val
    
    def __getitem__(self,key):
        index = self.get_hash(key)
        return self.arr[index]

t = HashTable()

t['Anandhu'] = '007'
t['Nandhu'] = '123'
print(t.arr)
x = t['Anandhu']
print(x)


