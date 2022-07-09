from array import *
import numpy as np
print(np.__version__)

# Day 1 - 11,15,10,6
# Day 2 - 10,14,11,5
# Day 3 - 12,17,12,8
# Day 4 - 15,18,14,9

print('Creating a Two Dimensional Array')
twoDarray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDarray)

print('Inserting a row or column using insert and append method')
print('1.Insert')
newtwoDarray = np.insert(twoDarray, 0, [[1, 2, 3, 4]], axis=0)
print(newtwoDarray)
print('2.Append')
newtwoDarray = np.append(twoDarray, [[1, 2, 3, 4]], axis=0)
print(newtwoDarray)

print('Accessing a Element using Index')
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
       print(array[rowIndex][colIndex])

accessElements(twoDarray, 2, 3)

print('Traversing through the Array')
def Traverse(array):
   for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
Traverse(twoDarray)

print('Searching a Element ')
def Search(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index '+str(i)+" "+str(j)
    return 'The element is not found'
print(Search(twoDarray, 14))

print('Deleting a row or a column')
newArray = np.delete(twoDarray, 0, axis=0)
print(newArray)






