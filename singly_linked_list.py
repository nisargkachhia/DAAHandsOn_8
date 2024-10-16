class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class SinglyLinkedList:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = [None] * max_size  # Fixed-size array for nodes
        self.head = -1
        self.free_list = 0
        # Initialize free list
        for i in range(max_size - 1):
            self.list[i] = Node(next_node=i + 1)
        self.list[max_size - 1] = Node(next_node=-1)

    def allocate_node(self):
        if self.free_list == -1:
            return -1  # No space
        new_node = self.free_list
        self.free_list = self.list[new_node].next_node
        return new_node

    def free_node(self, index):
        self.list[index].next_node = self.free_list
        self.free_list = index

    def insert(self, data):
        new_node_index = self.allocate_node()
        if new_node_index == -1:
            print("Out of space")
            return
        self.list[new_node_index].data = data
        self.list[new_node_index].next_node = self.head
        self.head = new_node_index

    def display(self):
        current = self.head
        while current != -1:
            print(f"{self.list[current].data} -> ", end="")
            current = self.list[current].next_node
        print("NULL")

# Example usage:
if __name__ == "__main__":
    sll = SinglyLinkedList(5)
    sll.insert(10)
    sll.insert(20)
    sll.insert(30)
    sll.display()
