
def find_kth_smallest(l, k):
    l.sort()

    return l[k]


l = [4, 3, 25, 5, 23, 13, 4, 2, 1, 2, 9, 12]
print(find_kth_smallest(l, 7))
