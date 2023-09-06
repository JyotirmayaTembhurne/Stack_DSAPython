class MyQueue:
    def __init__(self):
        self.queue = list()

    def length(self):
        print(len(self.queue))

    def push(self, val):
        self.queue.append(val)
        return self.queue

    def pop(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def IsEmpty(self):
        class MyQueue:

    def __init__(self):
        self.queue = list()

    def push(self, x: int) -> None:
        self.queue.append(x) 

    def pop(self) -> int:
        return self.queue.pop(0)
        

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return self.queue == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

    def Display(self):
        for i in self.queue:
            print(i)


q = MyQueue()
q.push(0)
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.Display()
print(q.peek())
