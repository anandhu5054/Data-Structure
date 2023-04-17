class BST:
    def __init__(self,key):
        self.key = key
        self.rChild = None
        self.lChild = None

    def insert(self,data):
        if self.key == None:
            self.key = data
            return
        
        if self.key == data:
            return
        
        if self.key>data:
            if self.lChild:
                self.lChild.insert(data)
            else:
                self.lChild = BST(data)
        if self.key<data:
            if self.rChild:
                self.rChild.insert(data)
            else:
                self.rChild = BST(data)

root = BST(15)
root.insert(10)

# root.lChild = BST(10)
print(root.key)
# print(root.lChild)
print(root.lChild.key)
print(root.lChild.lChild)
