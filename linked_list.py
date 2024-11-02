class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def printLL(self):
        if self.head is None:
            return
        curr=self.head
        while curr:
            print(curr.data,end=' >> ')
            curr=curr.next
    
    def appendLL(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new
    
    def prepandLL(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    
    def insert_at_position(self,data,position):
        new=Node(data)
        curr=self.head.next
        before=self.head
        for i in range(1,position-1):
            curr=curr.next
        new.data=data
        new.next=curr.next
        curr.next=new
    
    def delete_begin(self):
        curr=self.head
        self.head=curr.next
        curr.next=None
    
    def delete_end(self):
        curr=self.head.next
        before=self.head
        while curr.next:
            curr=curr.next
            before=before.next
        before.next=None
    
    def delete_node(self,target):
        curr=self.head.next
        before=self.head
        while curr:
            if curr.data==target:
                before.next=curr.next
                curr.next=None
                return
            before=curr
            curr=curr.next
    
    def middle_node(self):
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)

    def remove_middle(self):
        slow=fast=self.head
        while fast and fast.next:
            before=slow
            slow=slow.next
            fast=fast.next.next
        before.next=slow.next
    
    def reverseLL(self):
        before=None
        curr=self.head
        while curr:
            temp=curr.next
            curr.next=before
            before=curr
            curr=temp
        self.head=before
        
# ll=LinkedList()
# ll.appendLL(10)
# ll.appendLL(40)
# ll.appendLL(50)
# ll.prepandLL(20)
# ll.insert_at_position(30,2)
# ll.delete_begin()
# ll.delete_end()
# ll.delete_node(30)
# ll.middle_node()
# ll.remove_middle()
# ll.reverseLL()
# ll.printLL()


#-------DOUBLY LINKED LIST----------#

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLL:
    def __init__(self):
        self.head=None
    def appendDD(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new
            new.prev=curr

    def prependDD(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return
        new.next=self.head
        self.head.prev=new
        self.head=new
    def printDD(self):
        if self.head is None:
            return
        curr=self.head
        while curr:
            print(curr.data,end=' <-> ')
            curr=curr.next


dd=DoublyLL()
dd.appendDD(10)
dd.appendDD(20) 
dd.prependDD(30)
dd.printDD()  



#-----------circular------------------#

class NodeC:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def printLL(self):
        if self.head is None:
            print('empty')
        else:
            curr=self.head
            print(curr.data,end=' >> ')
            while curr.next != self.head:
                curr=curr.next
                print(curr.data,end=' >> ')
            print(curr.next.data)
    
    def insert_begin(self,data):
        new=NodeC(data)
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            new.next=self.head
            self.tail.next=new
            self.head=new


cc=CircularLL()
cc.insert_begin(10)
# cc.printLL()



