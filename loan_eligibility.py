#Loan eligibility checker

name = input("enter your name: ")
age = int(input("Enter your age: "))

if age > 21 and age < 61:
    credit_score = int(input("Enter your credit score: "))
    if credit_score < 300 and credit_score > 900:
        print("invalid credit score")
    elif credit_score < 650:
        print("Rejected, credit score is too low")
    else:
        salary = int(input("enter your monthly income: "))
        if salary < 15000:
            print("Rejected, your monthly income does not met the eligibility criteria")
        else:
            print("congratulations..! mr.",name," you have passed all eligibility criterias")
else:
    print("sorry mr.",name, " You are rejected age must be between 21 and 60 years")
