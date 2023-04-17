class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None 
    
    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty")

        else:
            n= self.head
            while n is not None:
                print(n.data,"-->", end=" ")
                n= n.ref

    def add_begin(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = self.head
        else:
            new_node.ref = self.head
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self,data,x):
        n= self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == x :
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("LL is empty")
        elif self.head is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self,value):
        if self.head is None:
            print("LL is empty")
            return
        if value== self.head.data:
            self.head = self.head.ref
            return

        n= self.head
        while n.ref is not None:
            if n.ref.data == value:
                break
            n = n.ref
        if n.ref is None:
            print("node is not present")
        else:
            n.ref = n.ref.ref

    def update(self,value,new_value):
        n =self.head
        while n.ref is not None:
            if n.data == value:
                n.data = new_value
                return
            n = n.ref
        print("sorry no matching value found")


        



LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_end(90)
LL1.add_begin(77)
LL1.add_before(45,90)
LL1.add_after(99,90)
# LL1.delete_begin()
# LL1.delete_end()
LL1.delete_by_value(45)
LL1.add_end(123)
LL1.print_LL()


