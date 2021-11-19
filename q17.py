num=input("enter the name : ")
list1=list(num)
print(list1)
i=0
b=[]
while i<len(list1):
    c=0
    j=0
    while j<len(list1):
        if list1[i]==list1[j]:
            b.append(list1[j])
            c=c+1
        j=j+1
        k=0
        while k<1:
            if b[i]=="a" or b[i]=="e" or b[i]=="i" or b[i]=="o" or b[i]=="u":
                print(b[i],"vowal")
            k=k+1
        i=i+1