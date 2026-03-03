print("______________PYTHON ATM______________\n")

Balance = 10000
pin = 1234
attempt = 5

while attempt > 0:
    enter_pin = int(input("Enter your 4-digit pin: "))
    if enter_pin == pin:
        print("Login successfull✅")
        break

    attempt -= 1
    print(f"Wrong pin❌\nAttempts left: {attempt}")


else:
    print("Too many attempts📛\nTry again after 24hr❗\n")
    exit()

while True:
    print("=========================\n")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("=========================\n")

    choice = int(input("Select the numnber: "))
    if choice == 1:
        print("Your Balance is: ", Balance)

    elif choice == 2:
        deposit = int(input("Enter your deposit amount: "))
        Balance += deposit
        print("Deposit successfull✅\nNew Balance: ", Balance)

    elif choice == 3:
        withdraw = int(input("Enter your withdraw amount: "))

        if withdraw <= Balance:
            Balance -= withdraw
            print("Withdraw successfull✅\nNew Balance: ", Balance)
        else:
            print("Insufficent balance❗")

    elif choice == 4:
        print("Thanks for using python ATM🙏")
        break
    else:
        print("Invalid option❌")
