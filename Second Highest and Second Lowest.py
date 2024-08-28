array = [4,4,3,3,4,7,7,0,9,2,6,8,1,99,10,8,0,3,99]

for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if array[i] > array[j]:
           z = array[i]
           array[i] = array[j]
           array[j] = z
print(array)


length = len(array)-1
lowest = array[length]
highest = array[0]
secondLowest = array[1]
print(lowest)
print(highest)

for z in range(1,len(array)-1):
    if highest<array[z]:
        highest = array[z]
        secondHighest = array[z-1]
print(secondHighest)

for p in range(1,len(array)-1):
    if lowest>array[p]:
        lowest = array[p]
        secondLowest = array[p+1]
print(secondLowest)



