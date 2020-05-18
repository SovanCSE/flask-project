"""
Stack implementationn using linkedlist
Stack is last in first out process every operation means insertion and deleteion will happen from
oneend which is called as top
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head=None

    def get_size(self):
        count = 0
        itr_head = self.head
        while itr_head:
            count += 1
            itr_head = itr_head.next
        return count

    def push(self, item):
        new_node = Node(item)
        itr_head = self.head
        if not itr_head:
            self.head = new_node
            print("Added item:", item)
            return
        while itr_head.next:
            itr_head = itr_head.next
        itr_head.next = new_node
        print("Added item:",item)

    def pop(self):
        if not self.get_size():
            print("Stack is empty")
        else:
          if self.get_size() == 1:
             print("removed item:", self.head.data)
             self.head = None
          else:
            itr_head = self.head
            while itr_head.next.next:
                itr_head = itr_head.next
            print("Removed item:",itr_head.next.data)
            itr_head.next = None




    def print_stack(self):
        li = []
        itr_head = self.head
        while itr_head:
            li.append(itr_head.data)
            itr_head = itr_head.next
        print("Current Stack elements:", li)


if __name__ == "__main__":
    stack = Stack()
    stack.push(12)
    stack.push(14)
    stack.push(15)
    stack.push(17)
    stack.print_stack()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.print_stack()