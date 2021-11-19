elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
sum=0
count=0
while i<len(elements):
    if elements [i]%2==0:
        print(elements[i],"even")
    elif elements [i]%2!=0:
        print(elements[i],"odd")
        count=count+elements[i]
        sum=sum+elements[i]
    i=i+1
print(count)
print(sum)
print(sum//i)