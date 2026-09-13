#to check if a word is a palindrome

p_word=input("enter a word to check it is a palindrome: ")
if p_word == p_word[::-1]:
    print(p_word," is a palindrome")
else:
    print(p_word," is not a palindrome")

#to check if a number is a palindrome or not

p_num=int(input("enter a number to check if it is a palindrome or not: "))
num=str(p_num)
if num == num[::-1]:
    print(num,"is a palindrome")
else:
    print(num, "is not a palindrome")