class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.nxt

    def set_next(self, nxt):
        self.nxt = nxt

    def has_next(self):
        return self.nxt is not None


class Sll:
    def __init__(self):
        self.head = None
        self.length = 0

    def le(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            data = current.data
            current = current.nxt
            print(data, end="->")

        return count

    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.data = data
        if self.length == 0:
            self.head = new_node
        else:
            new_node.nxt = self.head
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.nxt is not None:
                current = current.nxt
            current.nxt = new_node
        self.length += 1

    def insert_at_position(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        elif pos == 0:
            self.insert_at_beginning(data)
        elif pos == self.length:
            self.insert_at_end(data)
        else:
            newNode = Node()
            newNode.data = data
            count = 1
            current = self.head
            while count < pos - 1:
                count += 1
                current = current.nxt
            newNode.nxt = current.nxt
            current.nxt = newNode
            self.length += 1

    def show_list(self):
        pass

    def delete_first(self):
        if self.length == 0:
            return None
        current = self.head
        self.head = current.nxt
        self.length -= 1

    def delete_last(self):
        if self.length == 0:
            return None
        currentnode = self.head
        previousnode = self.head
        while currentnode.nxt is not None:
            previousnode = currentnode
            currentnode = currentnode.nxt
        previousnode.nxt = None
        self.length - +1

    def delete_at_position(self, pos):
        if pos > self.length or pos < 0:
            print("invalid Position")

        curent = self.head
        count = 1
        while count < pos - 1:
            curent = curent.nxt

        curent.nxt = curent.nxt.nxt
        self.length -= 1

    def delete_by_value(self, val):
        currentnode = self.head
        previousnode = self.head
        while currentnode.nxt is not None:
            if currentnode.data == val:
                previousnode.nxt = currentnode.nxt.nxt
                self.length-=1
                return
            previousnode = currentnode
            currentnode = currentnode.nxt


a = Sll()
a.insert_at_end(12)
a.insert_at_end(13)
a.insert_at_end(14)
a.insert_at_end(15)

a.insert_at_position(4, 45)
a.le()
print()
# a.delete_last()
# a.delete_at_position(2)
# a.delete_first()
a.delete_by_value(15)
a.le()
print(a.length)
