# Import your custom Queue class
from custom_queue import Queue

# Example usage of Queue
if __name__ == "__main__":
    q = Queue(5)  # Create a queue with a size of 5
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Front element:", q.peek())  # Should print 10
    print("Dequeued:", q.dequeue())   # Should dequeue 10
    print("Front element after dequeue:", q.peek())  # Should print 20
