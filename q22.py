# a=50
# b=30
# if a==a>b:
#     print(a,"greater number")
# else:
#     print(b,"greater number")

# num=int(input("enter the number : "))
# i=2
# while i<=num:
#     j=1
#     while j<=10:
#         print(i*j)
#         j=j+1
#     i=i+1


# a=123
# a=a%10
# print(a)

number_list=[1,6,0,7,0,2,3]
last=number_list[-1]
i=0
while i<len(number_list):
    if last==0:
        last=number_list[i]
    i=i+1
print(last)