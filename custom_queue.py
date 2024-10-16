class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [0] * max_size  # Fixed-size array
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_full(self):
        return self.count == self.max_size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow")
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
            self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return -1
        else:
            value = self.queue[self.front]
            self.front = (self.front + 1) % self.max_size
            self.count -= 1
            return value

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return -1
        else:
            return self.queue[self.front]

# Example usage:
if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Front of queue:", queue.peek())
    print("Dequeued element:", queue.dequeue())
    print("Front of queue after dequeue:", queue.peek())
