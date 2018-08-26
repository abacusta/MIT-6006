
#root of tree: first element in the array, corresponding to i = 1 parent(i) =i/2: returns index of node's parent
#left(i)=2i: returns index of node's left child
#right(i)=2i+1: returns index of node's right child

def max_heapify(ls, el):
    if 2*el < len(ls)+1:
        left = 2*el
    else:
        left = -1
    if 2*el + 1 < len(ls)+1:
        right = 2*el + 1
    else:
        right = -1
    if left == -1:
        return ls
    elif right == -1 and left != -1:
        if ls[left-1] > ls[el-1]:
            temp = ls[left-1]
            ls[left-1] = ls[el-1]
            ls[el-1] = temp
            return ls
        else:
            return ls
    else:
        if max(ls[el-1], ls[right-1],ls[left-1]) == ls[el-1]:
            return ls
        elif max(ls[el-1], ls[left-1], ls[right-1]) == ls[left-1]:
            temp = ls[left-1]
            ls[left-1] = ls[el-1]
            ls[el-1] = temp
            return max_heapify(ls,left)
        else:
            temp = ls[right-1]
            ls[right-1] = ls[el-1]
            ls[el-1] = temp
            return max_heapify(ls,right)
ls = [16,4,10,14,7,9,3,2,8,1]
def build_max_heap(ls):
    for i in range(len(ls)//2, 0, -1):
        max_heapify(ls,i)
    return ls

def duplicate_list(ls):
    newls = []
    for i in range(len(ls)):
        newls.append(0)
    return newls
def heap_sort(ls):
    ls=build_max_heap(ls)
    ls2 = duplicate_list(ls)
    count = len(ls)-1
    while len(ls) > 0:
        ls2[count] = ls.pop(0)
        count -= 1
        ls = max_heapify(ls,1)
    return ls2
def input_ls():
    length = int(input("How long do you want your list to be? "))
    ls = []
    for i in range(length):
        ls.append(int(input("Input the " + str(i+1) + "th element of the list: ")))
        print(ls)
    return ls
print(heap_sort(input_ls()))
