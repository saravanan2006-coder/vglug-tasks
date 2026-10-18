#find the duplicate letters in the string
#find the subsring in the string
#find the letter count in the string

def duplicate(input_str):
    seen = []
    duplicates = []
    for i in input_str:
        if i in seen:
            if i not in duplicates:
                duplicates.append(i)
        else:
            seen.append(i)
    
    return duplicates


def substring(input_str,substr):
    if substr in input_str:
        return True
    else:
        return False

def letter_count(input_str):
    count = 0
    for c in input_str:
        if c.isalpha():
            count = count + 1
    return count

input_str = input("Enter a string : ")
usr_choice = input("What do you want to perform ? \n press 1 to find the duplicates in a string \n press 2 to find the substring in the string \n press 3 to find the letter count in the string  \n")

if usr_choice == "1":
    print("duplicate leters : ",duplicate(input_str))

elif usr_choice == "2":
    substr = input("enter a substring : ")
    if substring(input_str,substr):
        print(substr,"is a substring of ",input_str)
    else:
        print(substr,"is not a substring of ",input_str)

elif usr_choice == "3":
    print("the number of letters in the string :",letter_count(input_str))
    
else:
    print("Invalid choice")
