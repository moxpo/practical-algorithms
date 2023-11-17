class node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node()

    def insert(self, data):
        new = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new

    def length(self):
        count = 0
        current = self.head.next
        while current != None:
            count += 1
            current = current.next
        return count

    def display(self):
        elements = []
        current = self.head.next
        while current != None:
            elements.append(current.data)
            current = current.next
        print(elements)

    def get(self, index):
        if index >= self.length() or index <0:
            print("ERROR")
        current_index = 0
        current_node = self.head
        while True:
            current_node=current_node.next
            if current_index == index:
                return current_node.data
            current_index+=1

    def erase(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: Index out of range")
            return

        current_index = 0
        current_node = self.head
        while current_node.next is not None:
            if current_index == index:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            current_index += 1


ll = linkedlist()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

ll.display()
print(ll.length())

print(ll.get(2))

ll.erase(3)

ll.display()
