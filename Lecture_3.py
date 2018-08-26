def insertionsort(array):
    for i in range(1,len(array)):
        el = array[i]
        for j in range(i,-1,-1):
            if el < array[j]:
                temp = array[j]
                array[j] = el
                array[j+1] = temp
    return array
array = [4,6,3,5,8,7,2,1,10,9]
#print(insertionsort(array))
def binarysearch(ls,element):
    currentel = ls[len(ls)//2]
    index = len(ls)//2
    while currentel != element:
         if currentel > element:
             index = index//2
             currentel = ls[index]
         else:
            index = index + index//2
            if index > len(ls)-1:
                index = len(ls)-1
            currentel = ls[index]
    return index



#print(binarysearch(insertionsort(array),10))

def merge(larray, rarray):
    narray = []
    while len(larray) > 0 or len(rarray)>0:
        if len(larray) == 0 and len(rarray)>0:
            for i in range(len(rarray)):
                narray.append(rarray.pop(0))
        elif len(larray) > 0 and len(rarray)==0:
            for i in range(len(larray)):
                narray.append(larray.pop(0))
        elif larray[0] >= rarray[0]:
            narray.append(rarray.pop(0))
        else:
            narray.append(larray.pop(0))
    return narray
#https://::ffff:208.113.165.172
def mergesort(array):
    larray = array[:len(array)//2]
    rarray = array[len(array)//2:]
    if len(array) == 1:
        return array
    larray = mergesort(larray)
    rarray = mergesort(rarray)
    print(larray)
    print(rarray)
    return merge(larray, rarray)

print(mergesort([1,6,5,3,8,10,7,4,2]))
