def onedpeakfinder(ls):
    if len(ls) == 1:
        return ls[0]
    if len(ls) == 2:
        return max(ls[0],ls[1])
    elif ls[len(ls)//2] < ls[len(ls)//2+1]:
        return onedpeakfinder(ls[len(ls)//2:])
    elif ls[len(ls)//2] < ls[len(ls)//2 -1]:
        return onedpeakfinder(ls[:len(ls)//2])
    else:
        return ls[len(ls)//2]

array = [1,2,3,4,5,6,7,8,9]
print(onedpeakfinder(array))
print(array[:len(array)//2])
def twodpeakfinder(tdls):
    rows = len(tdls)
    columns = len(tdls[0])
    midrow = tdls[rows//2]
    maxnum = -1
    index = 0
    for i in range(columns):
        if midrow[i] > maxnum:
            index = i
            maxnum = midrow[i]
    if rows == 1:
        print("index:" + str(index) + " maximum:" + str(maxnum))
        return [index,maxnum]
    if midrow[index] < tdls[rows//2 +1][index]:
        return twodpeakfinder(tdls[rows//2:])
    elif midrow[index] < tdls[rows//2 -1][index]:
        return twodpeakfinder(tdls[:rows//2])
    else:
        print("index:" + str(index) + " maximum:" + str(maxnum))
        return [index,maxnum]
tdarray = [[10,8,10,10],
           [14,13,12,11],
           [15,9,11,21],
           [16,17,19,20]]
twodpeakfinder(tdarray)
narray = [1,2,3,4,5]
print(narray[len(narray)//2:])
print(narray[:len(narray)//2])
