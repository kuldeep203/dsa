
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


class Dll:
    def __init__(self):
        self.head = None
        self.length = 0

    def transverse(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            data = current.data
            current = current.nxt
            print(data, end="->")
        print()

        return count

    def insert_at_begin(self, data):
        new_node = Node()
        new_node.data = data
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            current.pre = new_node
            new_node.nxt = current
            self.head = new_node
        self.length += 1

    def insert_at_last(self, data):
        new_node = Node()
        new_node.data = data
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.nxt is not None:
                current = current.nxt
            current.nxt = new_node
            new_node.pre = current
        self.length += 1

    def insert_at_postion(self, data, pos):
        if pos < 0 or pos > self.length:
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_begin(data)
        if pos == self.length:
            self.insert_at_last(data)
        else:
            new_node = Node()
            new_node.data = data
            count = 0
            current = self.head
            while count < pos - 1:
                current = current.nxt
                count += 1
            new_node.nxt = current.nxt
            new_node.pre = current
            current.nxt = new_node
            current.nxt.pre = new_node
        self.length += 1

    def delete_first(self):
        current = self.head
        self.head = current.nxt

    def delete_last(self):
        current = self.head
        while current.nxt is not None:
            current = current.nxt
            print(current.data)
        current.pre.nxt = None

    def delete_position(self, pos):
        count = 0
        current = self.head
        if pos ==0:
            self.delete_first()
        elif pos == self.length:
            self.delete_last()
        else:
            while count < pos - 1:
                print(count)

                current = current.nxt
                print(current.data)
                count +=1
            current.nxt = current.nxt.nxt
            current.nxt.pre = current
        # current.pre.nxt = current.nxt


    def search(self, value):
        current  = self.head
        while current is not None:
            current   = current.nxt
            print(current.data)
            if current.data == value:
                print("value found")
                return True



a = Dll()

a.insert_at_begin(1)
a.insert_at_begin(2)
a.insert_at_begin(3)
a.insert_at_begin(4)
a.insert_at_last(5)
a.transverse()
a.insert_at_postion(34, 3)
a.transverse()
# a.delete_last()
a.transverse()
print("fwdsdffffff")
a.delete_position(3)
a.transverse()
a.search(2)
