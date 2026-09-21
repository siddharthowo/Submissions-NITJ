class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("No elements in stack")
        return self.data[-1]

    def is_empty(self):
        return len(self.data)==0

    def size(self):
        return len(self.data)

    def display(self):
        print("Stack (bottom -> top):", self.data)

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.data.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def display(self):
        print("Queue (front -> rear):", self.data)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Top element (peek):", s.peek())
print("Popped:", s.pop())
print("Stack size:", s.size())
s.display()

q = Queue()
q.enqueue("xyz")
q.enqueue("abz")
q.enqueue("123")
q.display()
print("Front element:", q.front())
print("Dequeued:", q.dequeue())
print("Queue size:", q.size())
q.display()