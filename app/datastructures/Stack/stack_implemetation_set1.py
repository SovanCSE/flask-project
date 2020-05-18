"""
Stack implementationn using list
Stack is last in first out process every operation means insertion and deleteion will happen from
oneend which is called as top
"""

class Stack:
    def __init__(self):
        self.MAX_CAPACITY = 5
        self.stack_list = ['' for i in range(self.MAX_CAPACITY)]
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            print("Stack is empty")
            return True

    def isFull(self):
        return (self.top+1) == self.MAX_CAPACITY

    def push(self, item):
        if self.isFull():
            print("Stack is full")
            return
        elif self.isEmpty():
            self.top = 0
        else:
            self.top+=1
        self.stack_list[self.top] = item
        print("Added item:",item)

    def pop(self):
        if self.isEmpty():
            return
        else:
            delete_index = self.top
            self.top -= 1
        print("Deleted item:", self.stack_list.pop(delete_index))

    def top_item(self):
        if self.isEmpty():
            return
        else:
            print("Top item:", self.stack_list[self.top])

    def print_stack(self):
        print("Current stack list:",self.stack_list)

if __name__ == "__main__":
    stack = Stack()
    stack.push(12)
    stack.push(15)
    stack.push(16)
    stack.push(17)
    stack.push(18)
    stack.push(19)
    stack.print_stack()
    stack.pop()
    stack.top_item()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.top_item()
    stack.pop()
    stack.pop()
    stack.print_stack()