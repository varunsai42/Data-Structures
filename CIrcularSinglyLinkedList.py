class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
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

    # Creation of Circular Singly Linked List
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return 'CSLL has been created'

    # Insertion of a node in Circular SLL
    def insertCSLL(self, value, location):
        if self.head is None:
            return 'Circular SLL does not exist'
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return 'The Node has been successfully inserted'

    # Traverse through Circular SLL
    def traverseCSLL(self):
        if self.head is None:
            return "There is not any element for traversal "
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    # Searching a node in Circular SLL
    def searchNodeinCSLL(self,nodeValue):
        if self.head is Node:
            return 'Circular SLL does not contain any node'
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return 'The node does not exist in the CSLL'

    # Deletion of a node in circular SLL
    def deleteNodeinCSLL(self, location):
        if self.head is None:
            return 'Nodes does not exist'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else :
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else :
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # Deleting Circular SLL
    def deleteTotalCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None



circularSLL = CircularSinglyLinkedList()
print(circularSLL.createCSLL(1))
circularSLL.insertCSLL(0, 0)
circularSLL.insertCSLL(2, 1)
circularSLL.insertCSLL(3, 1)
circularSLL.insertCSLL(2, 1)

print([node.value for node in circularSLL])

#circularSLL.traverseCSLL()

#print(circularSLL.searchNodeinCSLL(5))

#circularSLL.deleteNodeinCSLL(4)

circularSLL.deleteTotalCSLL()
print([node.value for node in circularSLL])

