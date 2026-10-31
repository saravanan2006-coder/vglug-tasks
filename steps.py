num = int(input("Enter a number: "))
count=0
while num > 0 :
    if num % 2 == 0:
        num = num // 2
    else:
        num -=1
    count += 1
print("number of steps: ",count)
