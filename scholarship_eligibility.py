#this program checks the scholarship elgibility of a student
mark = int(input("enter your mark: "))
attendance = int(input("enter your attendance pescentage: "))

if mark >= 75:
    if attendance >= 95:
        print("you are eligible for scholarship")
    else: 
        print("you don't have enough attendance percentage")
elif mark < 75:
    print("you are not eligible for scholarship")

elif mark > 100:
    print("enter a valid mark and attendance percentage")
