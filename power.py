def power(n):
    if n >= 0 and n!=0:
        while n%2==0:
            n = n // 2
        print(n==1)
    else:
        print("false")
    
n = int(input("enter a number: "))
power(n)
