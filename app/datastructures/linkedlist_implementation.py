class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
    """
    Print data sequence in node list
    """
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr=self.head
        node_str = ''
        while itr:
            node_str += str(itr.data) + "-->"
            itr = itr.next
        print(node_str)

    """
     get length of linked list
    """
    def get_length(self):
        itr= self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    """
    Insert node beginning of the linkedlist
    """
    def insert_at_begin(self, data):
        """

        :param data:
        :return:
        Note: Always one case will follow this is will create new node which next will be as
        current head(prior node address) and recent insrted node will be as head node
        """
        node = Node(data, self.head)
        self.head = node

    """
    Insert node end of the linked list
    """
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_begin(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    """
    Insert list of values at end of the linked list
    """
    def insert_values(self, data_list):
       for data in data_list:
           self.insert_at_end(data)

    """
    Insert node at middle of the linked list
    """
    def insert_at_middle(self, index, data):
        if index < 0 or index >= self.get_length():
            Exception("Index is invalid")
            return

        if index == 0:
            self.insert_at_begin(data)

        else:
            itr = self.head
            count=0
            while itr:
                if count == index-1:
                    node=Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1
    """
    Delete node middle of the linked list
    """
    def remove_at_middle(self, index):
        if index < 0 or index >= self.get_length():
            Exception("Index is invalid")
            return

        if index == 0:
            self.head = self.head.next

        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1

    """
    Deleting at beginning of linkedlist 
    """
    def remove_at_begin(self):
        if self.head is None:
            Exception("Linked list is empty")
            return
        self.head = self.head.next

    """
     Deleting at end of linkedlist
    """
    def remove_at_end(self):
        if self.head is None:
            Exception("Linked list is empty")
            return

        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None

if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.print()
    linkedlist.insert_at_begin(70)
    linkedlist.insert_at_begin(40)
    linkedlist.insert_at_end(80)
    linkedlist.insert_values([90,100])
    linkedlist.print()
    linkedlist.insert_at_middle(1,60)
    linkedlist.insert_at_middle(1,50)
    linkedlist.print()
    linkedlist.remove_at_middle(4)
    linkedlist.remove_at_middle(4)
    linkedlist.print()
    linkedlist.remove_at_begin()
    linkedlist.remove_at_end()
    linkedlist.print()

