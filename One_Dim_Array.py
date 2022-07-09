from array import *

arr1 = array('i',[1,2,3,4,5,6])
arr2 = array('d',[1.3,1.5,1.6])

# Insertion
arr2.insert(2,9)
print(arr2)

#Array traversal
def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)

#Accessing Element
def accessElement(array,index):
    if index >= len(array):
        print('There is not any element in this index')
    else:
        print(array[index])

accessElement(arr1,8)

# Finding Element
def SearchInArray(array,value):
    for i in array :
        if i == value:
            return array.index(value)
    return 'The element does not exist in Array'

print(SearchInArray(arr1,3))

# Deleting an Element

arr1.remove(1)
print(arr1)