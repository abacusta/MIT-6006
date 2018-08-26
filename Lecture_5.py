from math import *
def duplicate_list(ls):
    newls = []
    for i in range(len(ls)):
        newls.append(-1)
    return newls
def insert_binary_search_tree(ls,el, st):
    for i in range(int(2**(ceil(log(len(ls))/log(2))))-len(ls)):
        ls.append(-1)
    left = 2*st
    right = 2*st + 1
    if left >= len(ls)+1:
        ls.append(-1)
    if right >= len(ls) +1:
        ls.append(-1)
    if el < ls[st-1]:
        if ls[left-1] == -1:
            ls[left-1] = el
            return ls
        else:
            return insert_binary_search_tree(ls,el,left)
    if el > ls[st-1]:
        if ls[right-1] == -1:
            ls[right-1] = el
            return ls
        else:
            return insert_binary_search_tree(ls,el,right)

def find_BST_min(bst):
    left = 2*1
    while bst[left-1] != -1:
        if left*2 <= len(ls):
            left = 2*left
            print(left)
        else:
            break
    return bst[left-1]
def find_BST_max(bst):
    right = 2*1+1
    while bst[right-1] != -1:
        if right*2+1 <= len(ls) and bst[right*2] != -1 :
            right = 2*right+1
        else:
            break
    return bst[right-1]

ls = [49]
ls = insert_binary_search_tree(ls,79,1)
print(ls)
ls = insert_binary_search_tree(ls,46,1)
print(ls)
ls = insert_binary_search_tree(ls,41,1)
print(ls)
ls = insert_binary_search_tree(ls,64,1)
print(ls)
print(find_BST_min(ls))
print(find_BST_max(ls))
def delete_BST_element(ls, el):
    count = 1
    left = 2*count
    right = 2*count + 1
    while ls[count-1] != el:
        count += 1
        if ls[count-1] > el and ls[count-1] != -1:
            count = 2*count
        elif ls[count-1] < el and ls[count-1] != -1:
            count = 2*count+1
    ls[count-1] = -1
    return ls

#Hook length
#L shape plus a boundary
#Total number of

def avl_tree(ls):


def binary_search_tree(ls):
    root = ls[0]
    newls = [root]
    for i in range(1, len(ls)):
        insert_binary_search_tree(newls,ls[i],1)
    return newls
print(delete_BST_element(ls,64))
