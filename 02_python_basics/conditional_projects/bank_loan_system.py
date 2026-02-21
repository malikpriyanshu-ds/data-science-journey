Name = input("Enter your name: ")
age = int(input("Enter your age: "))
income = int(input("Enter your montyly income: "))

if age > 21:
    if income > 25000:
        if income > 50000:
            print("Loan Approved✅\nNo Collateral Needed❌")
        else:
            print("Loan Approved✅\nCollateral Needed")
    else:
        print("Loan not approved❌low income")
else:
    print("Loan not approved❌underage")
