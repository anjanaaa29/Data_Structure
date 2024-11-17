class Queue:
    def __init__(self):
        self.queue=[]
    def is_empty(self):
        return len(self.queue) == 0
    def enque(self,item):
        self.queue.append(item)
    def deque(self):
        if not self.is_empty():
            print(self.queue.pop(0))
        else:
            return 'Queue is empty'
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return 'Queue is empty'
    def display(self):
        print(self.queue)
q=Queue()
# q.enque(10)
# q.enque(20)
# q.enque(30)
# q.display()
# q.deque()