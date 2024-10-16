class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [0] * max_size  # Fixed-size array
        self.top = -1

    def is_full(self):
        return self.top == self.max_size - 1

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        if self.is_full():
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return -1
        else:
            value = self.stack[self.top]
            self.top -= 1
            return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return -1
        else:
            return self.stack[self.top]

# Example usage:
if __name__ == "__main__":
    stack = Stack(5)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top of stack:", stack.peek())
    print("Popped element:", stack.pop())
    print("Top of stack after pop:", stack.peek())
