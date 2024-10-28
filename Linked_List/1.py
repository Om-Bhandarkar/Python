class Node:
    def __init__(self):
        self.next = None
        self.head = None


    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")   