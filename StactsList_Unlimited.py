# Creating a stack Using Lists without Size Limit
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # Push
    def push(self, value):
        self.list.append(value)
        return 'The element has been successfully inserted'

    # Pop
    def pop(self):
        if self.isEmpty() :
            return 'There is no element to pop in the Stack'
        else:
            return self.list.pop()

    # Peek
    def peek(self):
        if self.isEmpty() :
            return 'There is no element to peek in the Stack'
        else:
            return self.list[len(self.list)-1]

    # Delete
    def delete(self):
        self.list = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

#print(customStack)

#print(customStack.pop())

#print(customStack.peek())
