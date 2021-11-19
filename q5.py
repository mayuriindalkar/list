num = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max=0
i=0
c=[]
while i<len(num):
    if num[i]>max:
        max=num[i]
    i=i+1
print(max) 
num.remove(max)
c.append(num)
j=0
max=num[j]
while j<len(num):
    if num[j]>max:
        max=num[j]
    j=j+1
print(max)
