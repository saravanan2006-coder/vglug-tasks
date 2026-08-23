#this is just a prototype of how atm works after the user insert their card

print("Insert Your ATM card")
pin = input("Enter your 4 digit PIN: ")
if len(pin) == 4:
    withdrawal_amt = int(input("Enter the amount to be Withdraw(amount must be multiple of 100,200,500): "))
    if withdrawal_amt % 100 == 0:
        print("your transaction completed , collect your ATM card then your cash")
    else:
        print("enter a valid amount")
else:
    print("invalid pin")
    print("collect your card and try again")

