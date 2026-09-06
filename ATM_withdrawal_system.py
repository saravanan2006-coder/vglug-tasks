balance = 10000
while balance > 0:
    withdrawal_amount = int(input("Enter the withdrawal amount: "))
    if withdrawal_amount <= balance:
        balance = balance - withdrawal_amount
        print("withdrawal successfull")
        print("remaining balance: ",balance)
    
    else:
        print("Insufficient balance")

    