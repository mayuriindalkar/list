# if else:
# last digit 3

# num=int(input("enter the number : "))
# a=num%10
# if a==3:
#     print("Yes")
# else:
#     print("no")

# found age for birth year and present year

# birth_age=int(input("enter the number : "))
# if birth_age<2021:
#     print(2021-birth_age,"current age")
# else:
#     print("child age is less than 1 year")

# LOOP:
# sum of 1 to 100

# i=1
# sum=0
# while i<=100:
#     sum=sum+i
#     print(i)
#     i=i+1
# print(sum)

# (1,-2,3-4...............-100)

# i=1
# while i<=100:
#     if i%2==0:
#         print(-i,end=" ")
#     else:
#         print(i,end=" ")
#     i=i+1

# A
# A B
# A B C 
# A B C D 
# A B C D E 

for i in range (65,70):
    for j in range (65,i+1):
        print(chr(j),end=" ")
    print()

# LIST:

# Maxium number 

# num=[70,80,20,30,90,10,8,40,120,6,15]
# max=0
# i=0
# while i<len(num):
#     if num[i]>max:
#         max=num[i]
#     i=i+1
# print(max)

# nested list 

# i=0
# a=[1,2,3,[5,2],3,2]
# sum=0
# while i<len(a):
#     j=0
#     sum1=0
#     while j<len(a[0:1]): 
#         sum1=sum1+[i][j]
#         j=j+1
#     i=i+1
#     sum=sum1+sum
# print(sum)  

# 1
# 1 2
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

# a=1
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1
