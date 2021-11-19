name=[ "m","o","m"] 
a=[]
i=0
j=len(name)-1
while i<len(name):
    if name[i]==name[j]:
        a.append(name[j])
        i=i+1
        j=j-1
if name==a:
    print("it is palindrome")
else:
    print("it is not palindrome")