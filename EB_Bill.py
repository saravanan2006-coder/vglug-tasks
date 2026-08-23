#eb bill calculator
cmr = int(input("enter the current meter reading: "))
lmr = int(input("enter the last meter reading: "))
if cmr < 0 or lmr < 0 :
    print("Enter a valid reading")
else:
    unit = cmr - lmr
    bill_amount = unit * 5
    print("you have consumed ",unit," units.")
    print("your bill amount is : ", bill_amount)
