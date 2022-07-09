from array import *

arr = array('i',[1,2,3,4,5,6,7])
arr2 = array('i',[9,10,11,12,13,14])

print(' step1')
for i in arr:
    print(i)

print('step2')
print(arr[1])

print('step3')
arr.append(8)
print(arr)

print('step4')
arr.insert(3,50)
print(arr)

print('step5')
arr.extend(arr2)
print(arr)

print('step6')
tempList = [20,21,22]
arr.fromlist(tempList)
print(arr)

print('step7')
arr.remove(50)
print(arr)

print('step8')
arr.pop()
print(arr)

print('step9')
print(arr.index(21))

print('step 10')
arr.reverse()
print(arr)

print('step 11')
print(arr.buffer_info())

print('step 12')
print(arr.count(1))

print('step 14')
#print(arr.tolist())

print('step 16')
print(arr[1:4])





