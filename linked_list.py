class Node:
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

    def setData(self, data=None):
        self.data = data

    def setNoxt(self, next=None):
        self.next = next

    def getData(self):
        return self.data

    def getNode(self):
        return self.next


class SingleLinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def insertTop(self, data):
        if self.start == None and self.end == None:
            newnode = Node(None, data)
            self.start = newnode
            self.end = newnode

        elif self.start != None:
            newnode = Node(self.start, data)
            self.start = newnode

    def insertBottom(self, data):
        if self.start == None and self.end == None:
            newnode = Node(None, data)
            self.start = newnode
            self.end = newnode

        elif self.end != None:
            newnode = Node(None, data)
            self.end.next = newnode
            self.end = newnode

    def printlist(self):
        temp = self.start
        while(temp is not None):
            print(temp.data)
            temp = temp.next


def main():
    mylist = SingleLinkedList()
    mylist.insertTop(10)
    mylist.insertTop(20)
    mylist.insertTop(30)
    mylist.insertBottom(50)
    mylist.printlist()


main()
