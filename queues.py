class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def Enqueue(self,data):
        self.queue.append(data)

    def Dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]
    
    def sizeQueue(self):
        return len(self.queue)

queue = Queue()

queue.Enqueue(12)
queue.Enqueue(13)
queue.Enqueue(42)
queue.Enqueue(18)

print(queue.sizeQueue())
print(queue.Dequeue())
print(queue.peek())
print(queue.sizeQueue())
