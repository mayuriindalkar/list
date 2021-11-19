# list = [20,35,60,45,28,40,32,38,98,91,84,87]
# i=0
# evan1=[]
# odd1=[]
# while i<len(list):
#     if list[i]%2==0:
#         evan1.append(list[i])
#     elif list[i]%2!=0:
#         odd1.append(list[i])
#     i=i+1
# print(evan1,"evan")
# print(odd1,"odd")


list = [20,35,60,45,28,40,32,38,98,91,84,87]
i=0
count=0
count1=0
sumeven=0
sumodd=0
evan1=[]
odd1=[]
while i<len(list):
    if list[i]%2==0:
        sumeven=sumeven+list[i]
        evan1.append(list[i])
        count=count+1
    elif list[i]%2!=0:
        sumodd=sumodd+list[i]
        odd1.append(list[i])  
        count1=count1+1 
    i=i+1
print(evan1,"evan" and odd1,"odd" and count,"count of evan number" and count1,"count of odd number" and sumeven,"sum of evan number" and sumodd,"sum of odd number")
# print(odd1,"odd")
# print(count,"count of evan number")
# print(count1,"count of odd number")
# print(sumeven,"sum of evan number")
# print(sumodd," sum of odd number")