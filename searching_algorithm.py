def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f'target at {i}')
            break
    else:
        print(f'target not found')
        
# linear_search([8,9,4,5],8)

def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left <= right:
        m=(left+right) // 2
        if target == arr[m]:
            return m
        elif target > arr[m]:
            left=m+1
        elif target < arr[m]:
            right=m-1
    return -1

# print(binary_search([-1,0,3,5,9,12],9))

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def printLL(self):
        if self.head:
            return
        n=self.head
        while n is not None:
            print(n.data,end=' >> ')
            n=n.next
    def insertLL(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return 
        n=self.head
        while n.next:
            n=n.next
        n.next=new
    def linear_search(self,target):
        curr=self.head
        position=0
        while curr:
            if curr.data==target:
                return position
            curr=curr.next
            position+=1
        return 'element not found'


# ll=LinkedList()
# ll.insertLL(10)
# ll.insertLL(20)
# ll.insertLL(30)
# print(ll.linear_search(20))
# ll.printLL()

class LinkedList:
    def __init__(self):
        self.head=None
    def printLL(self):
        if not self.head:
            return
        n=self.head
        while n is not None:
                print(n.data,end=' >> ')
                n=n.next
    def insertLL(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return
        n=self.head
        while n.next:
            n=n.next
        n.next=new
    def insert_end(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def linear_search(self,target):
        curr=self.head
        index=0
        while curr:
            if curr.data==target:
                return index
            curr=curr.next
            index+=1
        return 'element not found'


aa=LinkedList()
aa.insertLL(10)
aa.insertLL(20)
aa.insert_end(30)
print(aa.linear_search(20))
aa.printLL()

