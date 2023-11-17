class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size


    def push(self,key):         #insert element x in stack S
        self.stack.append(key)


    def pop(self):              #remove and return the most recently inserted element from stack S
        if len(self.stack) == 0:
            return print("Underflow")
        return self.stack.pop()

    def peek(self):             #return (but don’t remove) the most recently inserted element from stack S
        return self.stack[-1]


    def stack_size(self):       #return the number of elements stored in stack S
        return len(self.stack)

    def stack_empty(self):     #test if stack S is empty
        if not self.stack:
            return False
        else:
            return True

    