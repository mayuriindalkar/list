list1 = [1,2,3,4,5,7,6,8,9]
list2 = [2,3,1,0,6,7] 
i=0
a=[]
while i<len(list1):
    m=list1[i]
    if m not in list2:
        a.append(m)
    i=i+1
print(a)