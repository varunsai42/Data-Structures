class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Creation of Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return 'The Circular Doubly Linked List is created successfully'

    # Inserting a node
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print('There is no Linked List')
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next = newNode
                newNode.next.prev = newNode
            return 'The node has been successfully inserted '

    # Traversal through the Circular DLL
    def traverseCDLL(self):
        if self.head is None:
            print('There are no nodes to traverse')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    # Reverse Traversal
    def reverseTraverse(self):
        if self.head is None:
            print('There are no nodes to traverse')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head.prev:
                    break
                tempNode = tempNode.prev

    # Searching a node in Circular DLL
    def searchNode(self, nodeValue):
        if self.head is Node:
            return 'Circular DLL does not contain any node'
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return 'The node does not exist in the Circular DLL'
                tempNode = tempNode.next

    # Deleting a Node
    def deleteNode(self, location):
        if self.head is None:
            print('Circular DLL does not exist')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.tail.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print('The node has been successfully deleted')

    # Delete Entire Circular DLL
    def deleteEntire(self):
        if self.head is None:
            print('Circular DLL does not exist')
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print('The entire Circular DLL is deleted')


circularDLL = CircularDoublyLinkedList()

print(circularDLL.createCDLL(1))
circularDLL.insertNode(0, 0)
circularDLL.insertNode(2, 1)
circularDLL.insertNode(3, 1)
circularDLL.insertNode(4, 1)
circularDLL.insertNode(5, 2)

print([node.value for node in circularDLL])

#circularDLL.traverseCDLL()
#circularDLL.reverseTraverse()

#print(circularDLL.searchNode(2))

#circularDLL.deleteNode(2)
circularDLL.deleteEntire()
print([node.value for node in circularDLL])
