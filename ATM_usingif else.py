pin=1234
balance=50000
entered_pin=int(input("enter the pin:"))
if pin==entered_pin:
    print("ATM OPTIONS:")
    print("1.check the balance:")
    print("2.withdraw the cash:")
    print("3.deposit the cash:")
    print("4.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("your balance is:",balance)
    elif choice==2:
        amount=int(input("enter the amount:"))
        if amount<=balance:
            print("cash withdraw successful")
            balance-=amount
            print("remaining",balance)
        else:
            print("cash withdrawl unsuccessful")
    elif choice==3:
        amount=int(input("enter the amount to deposit"))
        balance+=amount
        print("the total balance is:",balance)
    elif choice==4:
        print("thanks for using the service")
else:
    print("incorrect pin")
