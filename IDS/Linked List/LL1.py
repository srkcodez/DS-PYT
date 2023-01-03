class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertBegin(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def insertEnd(self, data):
        NewNode = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = NewNode

    def insertPosition(self, pos, data):
        temp = self.head
        NewNode = Node(data)
        i = 1
        while temp.next is not None and i < pos - 1:
            i += 1
            temp = temp.next
        if i is not pos - 1:
            print("Given position not available")
        else:
            NewNode.next = temp.next
            temp.next = NewNode

    def display(self):
        temp = self.head
        while temp.next is not None:
            print(temp.data, "-->", end=' ')
            temp = temp.next
        print(temp.data)

    def deleteBegin(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("No element present in the begining")

    def deleteEnd(self):
        temp = self.head
        if temp is not None:
            delNext = temp.next
            while delNext.next is not None:
                temp = temp.next
                delNext = delNext.next
            temp.next = delNext.next
        else:
            print("No element present in the beginning")

    def deleteElement(self):
        if temp is not None:
            delNext = temp.next
            while delNext.next is not None:
                temp = temp.next
                delNext = delNext.next
            temp.next = delNext.next
        else:
            print("No element present in the begining")


l1 = LinkedList()

l1.insertBegin(10)
l1.insertBegin(20)

l1.insertEnd(30)
l1.insertEnd(40)
l1.insertBegin(5)
l1.insertPosition(3, 7)
l1.display()
l1.deleteBegin()
l1.display()
l1.deleteEnd()
l1.display()
