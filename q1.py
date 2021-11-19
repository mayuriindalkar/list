numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
index=0
total_count=0
while index < len(numbers):
    if numbers[index] >= 20 and numbers[index] <= 40:
        total_count=total_count+1
    index=index+1
print("total_count: " + str(total_count))