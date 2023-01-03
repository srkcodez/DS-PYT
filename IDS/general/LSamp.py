class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertBegin(self, d):
        NewNode = Node(d)
        if self.head is None:
            self.head = NewNode
        else:
            NewNode.next = self.head
            self.head = NewNode

    def insertEnd(self, d):
        NewNode = Node(d)
        pos = self.head
        if self.head is None:
            self.head = NewNode
        else:
            pos = self.head
            while pos.next is not None:
                pos = pos.next
            pos.next = NewNode

    def insertPosition(self, d, position):
        if position < 0:
            print("Given position not present")
        elif self.head is None or position == 1:
            NewNode = Node(d)
            NewNode.next = self.head
            self.head = NewNode
        elif position > 1:
            pos = self.head
            i = 1
            while pos.next is not None and i < position - 1:
                i = i + 1
                pos = pos.next
            if i < position - 1:
                print("Node can not be inserted in given position is not present")
            else:
                NewNode = Node(d)
                NewNode.next = pos.next
                pos.next = NewNode

    def display(self):
        if self.head is None:
            print("No elements in List")
        else:
            pos = self.head
            while pos.next is not None:
                print(pos.data, end="-->")
                pos = pos.next
            print(pos.data)

    def deleteBegin(self):
        if self.head is None:
            print(" No elements in the List")
        else:
            print(self.head.data, "is deleted successfully")
            self.head = self.head.next

    def deleteEnd(self):
        if self.head is None:
            print(" No elements in the List")
        elif self.head.next is None:
            print(self.head.data, "is deleted successfully")
            self.head = None
        else:
            delitem = self.head
            previtem = self.head
            while delitem.next is not None:
                delitem = delitem.next
                previtem = previtem.next
            print(delitem.data, " is deleted successfully")
            previtem.next = None

            print(self.head.data, "is deleted successfully")
            self.head = self.head.next


l1 = LinkedList()
l1.display()
l1.insertBegin(10)
l1.insertBegin(20)
l1.insertBegin(30)
l1.insertPosition(25, 4)
l1.insertEnd(55)
l1.insertPosition(15, 4)
l1.display()
l1.deleteBegin()
l1.display()
l1.deleteEnd()
l1.display()
