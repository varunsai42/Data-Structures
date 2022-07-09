class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation of Doubly Linked List
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'The DLL created successfully'

    # Insetion
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print('Node cannot be inserted')
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    # Traverse through Doubly Linked List
    def traverseDLL(self):
        if self.head is None:
            print('There is not any element to traverse')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    # Reverse traversal
    def reverseTraversal(self):
        if self.head is None:
            print('There is no element to Reverse transverse')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Searching a Node
    def searchNode(self, nodeValue):
        if self.head is None:
            print('There are no elements to Search')
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return 'The Node does not exist in this List'

    # Deleting a Node
    def deleteNode(self, location):
        if self.head is None:
            print('There is no element to delete')
        else:
            if location == 0 :
                if self.head == self.tail:
                    self.tail = None
                    self.head = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.tail = None
                    self.head = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print('The Node has been successfully deleted')

    # Deleting entire Doubly Linked List
    def delEntire(self):
        if self.head is None:
            print('There is no Node to delete')
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print('The Doubly Linked List has been successfully deleted')


doubleLL = DoublyLinkedList()
doubleLL.createDLL(1)

print([node.value for node in doubleLL])


doubleLL.insertNode(0, 0)
doubleLL.insertNode(2, 1)
doubleLL.insertNode(5, 2)
doubleLL.insertNode(3, 1)
doubleLL.insertNode(4, 1)

print([node.value for node in doubleLL])

#doubleLL.traverseDLL()
#doubleLL.reverseTraversal()

#print(doubleLL.searchNode(5))

#doubleLL.deleteNode(0)

doubleLL.delEntire()
print([node.value for node in doubleLL])