def concecutive(l):
    x = max(l)
    y = min(l)
    a=[]
    while y<=x:
        a.append(y)
        y=y+1
    j=0
    while j<len(a):
        if a[j] not in l:
            return [a[j]+1]
        j=j+1
print(concecutive([-3,-1,0,1,2,3,5])) 