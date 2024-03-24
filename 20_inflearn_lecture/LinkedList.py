class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    # 시간복잡도는 O(N)
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node

    # 시간복잡도는 O(N)
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    
    def insert_at(self, idx, value):
        new_node = Node(value)
        current = self.get(idx)
        current.next = new_node.next
        current.next = new_node

    def remove_at(self, idx):
        remove = self.get(idx)
        current = self.get(idx - 1)
        current.next = remove.next

    def insert_back(self, )
        

class LinkedListTail(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

print(2//1)