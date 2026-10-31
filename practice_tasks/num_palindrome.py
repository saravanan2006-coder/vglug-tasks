def palindrome(a,b=0):
    if a == 0:
        return b
    x = a % 10
    b = b * 10 + x
    return palindrome(a // 10, b)
a = int(input("Enter a number: "))
if a < 0 :
    print("false")
else:
    if a == palindrome(a):
        print("True")
    else:
        print("False")
