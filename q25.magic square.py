magic=[
    
    [8,3,4],
    [1,5,9],
    [6,7,2]
]
i = 0
sum = 0
sum1 = 0
sum2 = 0
while i<len(magic):
    colum=0
    while colum<len(magic):
        sum=sum+magic[i][colum]
        break
    i=i+1
print(sum)
j=0
sum1=0
while j<len(magic):
    row=0
    while row<len(magic):
        sum1=sum1+magic[j][row]
        break
    row=row+1
    j=j+1
print(sum1)
k=0
sum2=0
while k<len(magic):
    dig=0
    while dig<len(magic):
        sum2=sum2+magic[k][dig]
        break
    dig=dig+1
    k=k+1
print(sum2)
if sum==sum1==sum2:
    print("it is magic square")
else:
    print("it is not magic square")
