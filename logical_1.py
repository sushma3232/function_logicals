value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbol=["m","cm","d","cd","d","xd","l","xi","x","ix","v","iv","i"]
def convert():
    roman=''
    i=0
    while num>0:
        div=num//value[i]
        num=num%value[i]
        while div:
            roman=roman+symbol[i]
            div=div-1
        i=i+1
    return roman
num=input()
print(convert()) 