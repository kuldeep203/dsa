


class Node:
    def __init__(self, data=None, nxt=None, pre=None):
        self.data = data
        self.nxt = nxt
        self.pre = pre

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.nxt

    def set_next(self, nxt):
        self.nxt = nxt

    def get_pre(self):
        return self.nxt

    def set_pre(self, nxt):
        self.nxt = nxt

    def has_next(self):
        return self.nxt is not None


class Csl:
    def __init__(self):
        self.head = None
        self.length = 0

    def traverse(self):
        if self.head is None:
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.nxt
            if current == self.head:
                break
        print("HEAD")

    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.data = data

        if self.head is None:  # Case when the list is empty
            new_node.nxt = new_node  # The new node points to itself
            self.head = new_node
        else:
            current = self.head
            # Traverse the list to find the last node
            while current.nxt != self.head:
                current = current.nxt
            new_node.nxt = self.head  # New node points to the current head
            current.nxt = new_node  # Last node points to the new node
            self.head = new_node  # Update head to the new node

        self.length += 1

    def insert_at_end(self, data):
        new_node = Node()
        new_node.data = data

        if self.head is None:  # Case when the list is empty
            new_node.nxt = new_node  # The new node points to itself
            self.head = new_node
        else:
            current = self.head
            # Traverse the list to find the last node
            while current.nxt != self.head:
                current = current.nxt
            new_node.nxt = self.head  # New node points to the current head
            current.nxt = new_node  # Last node points to the new node
            new_node.nxt = self.head  # Update head to the new node

        self.length += 1

    def delete_at_end(self):
        previousnode = self.head
        # Traverse the list to find the last node
        currentnode = self.head
        while currentnode.nxt != self.head:
            previousnode = currentnode
            currentnode = currentnode.nxt
        previousnode.nxt = self.head


a = Csl()
a.insert_at_beginning(1)
a.insert_at_beginning(2)
a.insert_at_beginning(3)
a.insert_at_beginning(4)
a.insert_at_end(5)
a.insert_at_end(6)
a.insert_at_end(7)
a.insert_at_end(8)
a.delete_at_end()
a.delete_at_end()
print(a.length)
print(a.traverse())
