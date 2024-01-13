class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
    
class LL:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        if self.head:
            temp=self.head
            print('outside while it contain head refence ',temp)
            while temp.next:
                print(temp.next,'under while')
                temp=temp.next
                print('inside while',temp)
            temp.next=newnode
            print('under while',temp.next)
        else:
            self.head=newnode   
            print('else it is giving reference',self.head) 
            print(self.head.data)
        
        if not self.head:
            self.head = new_node
            print(1,self.head)
        else:
            current = self.head
            print(2,current)
            while current.next:
                current = current.next
                print(3,current)
            current.next = new_node
            print(4,current)
node=LL()
node.insert(23)
node.insert(45)
node.insert(35)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
        
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=new_node
                temp=temp.next
                
        