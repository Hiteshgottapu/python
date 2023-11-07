class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

# test
linked_list = LinkedList()
linked_list.insert(5)
linked_list.insert(10)
linked_list.insert(15)
linked_list.insert(20)
linked_list.insert(25)
linked_list.print_list()
linked_list.delete(15)
linked_list.print_list()

linked_list.delete(20)
linked_list.print_list()