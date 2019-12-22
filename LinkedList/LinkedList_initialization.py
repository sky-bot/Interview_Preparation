class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def insert(self, data):
        temp = Node(data)
        temp.link = self.head
        self.tail = temp
        self.head = temp

    
    def display(self):
        temp = self.get_head()
        while(temp):
            print("{}".format(temp.data), end="-->")
            temp = temp.link
    
    def insert_at_end(self, data):
        temp = Node(data)
        head = self.get_head()

        if not head:
            self.head = temp
            self.tail = temp
        else:
            self.tail.link = temp
            self.tail = temp
    
    def search(self, data):
        temp = self.get_head()
        pos = 1
        while(temp):
            if temp.data==data:
                print ("Element found at {}".format(pos))
                return
            pos = pos + 1
            temp = temp.link
        print("Element not present")
        return 

linked = LinkedList()
linked.insert_at_end(1)
linked.insert_at_end(2)
linked.insert_at_end(3)
linked.insert_at_end(4)
linked.insert_at_end(5)
linked.search(5)

linked.display()