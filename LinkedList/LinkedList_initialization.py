class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head=Node(None)
        self.tail=self.head

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def insert(self, data):
        temp = Node(data)
        temp.link = self.head
        self.tail = temp
        self.head = temp

        print("Data Inserted successfully")
    
    def display(self):
        temp = self.get_head()
        print("Inside display")
        while(temp.data):
            print("{}".format(temp.data), end="-->")
            temp = temp.link

linked = LinkedList()
linked.insert(1)
linked.insert(2)
linked.insert(3)
linked.insert(4)
linked.insert(5)
linked.display()