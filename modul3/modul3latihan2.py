class Queue:
    def _init_(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.items = [None] * capacity
        self.capacity = capacity

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] = item
            self.size += 1

    def dequeue(self):
        if not self.is_empty():
            item = self.items[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return item

    def peek(self):
        if not self.is_empty():
            return self.items[self.front]

    def search(self, item):
        for i in range(self.size):
            idx = (self.front + i) % self.capacity
            if self.items[idx] == item:
                return i + 1
        return -1

q = Queue(10)

q.enqueue("Java")
q.enqueue("DotNet")
q.enqueue("PHP")
q.enqueue("HTML")

print("remove : ", q.dequeue())
print("element : ", q.peek())
print("poll : ", q.dequeue())
print("peek : ", q.peek())

count = q.search("Java")
while count != -1 and count > 1:
    q.dequeue()
    count -= 1

print(q.dequeue())
print(q.is_empty())