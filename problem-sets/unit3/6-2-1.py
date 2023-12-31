# Implementing a singly-linked list in Python
#
# 1a)
#
# Create a class NodeSinglyLinkedList* which could then be used in the next part to define a
# SinglyLinkedList class. You should be able to initialize the node with a "key" (or value).
# The class should have the following methods; the names of the methods are meant to be self-explanatory:
#
#     get_key()
#     set_key()
#     get_next()
#     set_next()


class NodeSinglyLinkedList:
    """
    Singly linked list node
    """

    def __init__(self, key=0):
        self.key = key
        self.nxt = None

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_nxt(self):
        return self.nxt


    def set_nxt(self, nxt):
        self.nxt = nxt



nsll = NodeSinglyLinkedList()
nsll.set_key(1)
nsll.set_key(2)
nsll.set_key(3)
nsll.set_key(4)
print ("NodeSinglyLinkedList")
print ("get key :")
print(nsll.get_key())
nsll.set_nxt(5)
print ("get next :")
print(nsll.get_nxt())
print("\n")




# 1b)
#
# Create a class SinglyLinkedList that can store integers. For this part, it should have a head pointer
# only (so no tail pointer). It should initialize as an empty list, and the following methods should be defined:
#
#     empty()               # checks if linked list is empty
#     insert_head()         # inserts a node object of type NodeSinglyLinkedList at the head of the list
#     search_key()          # search for a given key in the linked list, returns the node if found, None if not found
#     size()                # returns the number of nodes in the linked list
#     print_all_keys()      # iterate through the entire linked list and print all keys
#
# Test all the methods of this linked-list to ensure they work correctly.

class SinglyLinkedList:
    """
    Singly linked list, with head pointer only
    Insertion at the head
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        if self.head == None:
            return True
        else:
            return False

    def insert_head(self, key):
        # create a new node and set key
        node = NodeSinglyLinkedList(key)

        # node inserted at head, so its next should point to where the list head was pointing
        node.nxt = self.head

        # the list's head should now be updated to point at this new node
        self.head = node

    def search_key(self, key):
        node = self.head
        while node != None and node.key != key:
            node = node.nxt
        return node

    def size(self):
        i = 0
        node = self.head
        while node != None:
            node = node.nxt
            i += 1
        return i


    def print_all_keys(self):
        # list = []
        node = self.head
        while node != None:
            # list.append(node.get_key())
            print(node)
            node = node.nxt
        print (list)

    # def insert_tail(self, key):
    #     if self.tail == None:
    #         node = NodeSinglyLinkedList(key)
    #         node.nxt = self.head
    #         self.head = node
    #     else:
    #         node = self.head
    #         while node.nxt != None:







        # node = self.head
        # while node.nxt != None:
        #     node = node.nxt
        #     self.key = key
        #





    def insert_tail(self, key):

        node = NodeSinglyLinkedList(key)

        while self.head != None:
            node = node.nxt

        self.tail = node


####!!!!!!!!!!!#############


sll = SinglyLinkedList()
print("ssl empty? -")
print(sll.empty())
sll.insert_head(1)
sll.insert_head(2)
sll.insert_head(3)
sll.insert_head(4)
# sll.insert_head(13)
print("SinglyLinkedList")
print("print all keys :")
sll.print_all_keys()
print("size :")
print(sll.size())
print("search result :")
if sll.search_key(3): print ("Found key")
if sll.search_key(13): print("Found key")
print("ssl empty? -")
print(sll.empty())
