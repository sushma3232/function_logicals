def valid():
    a1,a2,b1,b2,c1,c2=0,0,0,0,0,0
    i=0
    while i<len(p):
        if p[i]=="(":
            a1=a1+1
        if p[i]==")":
            a2=a2+1
        if p[i]=="[":
            b1=b1+1
        if p[i]=="]":
            b2=b2+1
        if p[i]=="{":
            c1=c1+1
        if  p[i]=="}":
            c2=c2+1
        i=i+1
    if a1==a2 and b1==b2 and c1==c2:
        print(True)
    else:
        print(False)
p=input("enter your chr")
valid()



