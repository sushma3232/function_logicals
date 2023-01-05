
# Merge Two Sorted Lists
def merge(list1,list2):
    if len(list1) or len(list2)>0:
        l=list1+list2
        l.sort()
        return l
    else:
        return []
print(merge([1,4,2,3],[1,3,4,5,6]))
print(merge([], [0]))
print(merge([],[]))