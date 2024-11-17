class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if not self.stack:
            return 'stack empty'
        else:
            return self.stack.pop()
    def is_empty(self):
        return len(self.stack)==0
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return 'empty stack'
    def display(self):
        if self.is_empty():
            print('stack is empty')
        else:
            # print('stack (top to bottom) : ')
            for ele in reversed(self.stack):
                print(ele)

st=Stack()
st.push(10)
st.push(40)
st.push(30)
# print(st.pop())
# print(st.is_empty())
# st.display()

class Node:
    def __init__(self,value):
        self.value=value
        self.next=next
class LinkedStack:
    def __init__(self):
        self.top=None
    def push(self,value):
        new=Node(value)
        new.next=self.top
        self.top=new
    def pop(self):
        if self.is_empty():
            print('stack is empty')
        popped_val=self.top.value
        self.top=self.top.next
        return popped_val
    def is_empty(self):
        return self.top is None
    def peek(self):
        if self.is_empty():
            print('stack is empty')
        return self.top.value
    def display(self):
        if self.is_empty():
            print('stack is empty')
        else:
            curr=self.top
            while curr:
                print(curr.value)
                curr=curr.next
                
ss=LinkedStack()
ss.push(10)
ss.push(20)
ss.push(30)
ss.display()
# print(ss.pop())
# print(ss.peek())
# print(ss.is_empty())




