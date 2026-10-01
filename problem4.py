balance =float(input("enter the balance"))
amount=float (input ("enter the shoppping amount"))
availaible_balance=balance-amount
if balance >=amount:
    print("payment successful")
    print(availaible_balance)
else:
    print(  "not sufficient balance")
