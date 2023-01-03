# Function to initialize the node object
def __init__(self, data):
    self.data = data  # Assign data
    self.next = None  # Initialize
    # next as null

# Linked List class
class LinkedList:
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            self.head.next = self.head
            self.head = new_node
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end='->')
            current = current.next


a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end='')
a_llist.display()
