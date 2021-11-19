# a=[23,14,56,12,19,9,15,25,31,42,43]
# b=len(a)
# even=0
# odd=0
# for i in range(b):
#     if a[i]%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print("even number =" ,even)
# print("odd number =" ,odd)



a=[23,14,56,12,19,9,15,25,31,42,43]
b=len(a)
c=[]
even=0
odd=0
for i in range(b):
    if a[i]%2==0:
        c.append(a)
        print(a[i])
    else:
        odd=odd+1
# print("even number =" ,even)
print("odd number =" ,odd)