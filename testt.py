
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def get_hash(self,key):
        h = 0
        for i in key:
            h+=ord(i)
        return h%self.max

    def insert(self,key,val):
        index = self.get_hash(key)
        node = self.arr[index]
        if node is None:
            self.arr[index] = Node(key,val)
        