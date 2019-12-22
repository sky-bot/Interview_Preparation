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
    
    def delete(self, data):
        temp = self.get_head()

        if temp.data == data:
            self.head = temp.link
            del temp
            print("Element Deleted")
            return True
        prev = temp
        cur = temp.link
        while(cur):
            if cur.data == data:
                prev.link = cur.link
                del cur
                print("Element Deleted")
                return True
            else:
                prev = cur
                cur = cur.link
            
            
            
            
            # if cur.data==data:
            #     temp2 = NextNode.link
            #     print(temp2.data)
            #     temp.link = temp2
            #     print("Element Deleted")
            #     return True
            temp = temp.link
        print("Element not present")
        return False

        # while(temp):

linked = LinkedList()
linked.insert_at_end(1)
linked.insert_at_end(2)
linked.insert_at_end(3)
linked.insert_at_end(4)
linked.insert_at_end(5)
# linked.search(5)
linked.delete(5)
linked.display()