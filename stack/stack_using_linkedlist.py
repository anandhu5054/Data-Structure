class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
    
    def isempty(self):
        return self.head == None

    def push(self,data):
        if self.isempty():
            self.head = Node(data,None)
        else:
            self.head = Node(data,self.head)

    def pop(self):
        if self.isempty():
            print("This stack is empty")
        else:
            popped = self.head
            self.head = self.head.next
            print(popped.data)
            
    def display(self):
        if self.isempty():
            print("This stack is empty")
        else:
            itr = self.head
            stack_display = ''
            while itr:
                stack_display = str(itr.data) + '-->'
                itr = itr.next
            print(stack_display)


















