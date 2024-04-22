class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.front = self.rear = -1
        self.capacity = k
        self.space = k 

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        if self.front == -1:
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.space -= 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.front = (self.front + 1) % self.capacity
        self.space += 1

        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty(): return -1

        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.space == self.capacity

    def isFull(self) -> bool:
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
