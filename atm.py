# Simple ATM System


# Stored data
password = 1234
current_balance = 5000


# Taking PIN input
entered_pin = int(input("Enter your PIN: "))


# Checking PIN
if entered_pin != password:

    print("Incorrect PIN!")
    print("Access Denied")


else:

    print("Choose option:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")


    # Taking menu choice
    choice = int(input("Enter choice: "))


    # Check Balance
    if choice == 1:

        print(f"Current Balance: ₹{current_balance}")


    # Withdraw
    elif choice == 2:

        amount = int(input("Enter withdrawal amount: "))


        # Invalid amount check
        if amount <= 0:

            print("Invalid Withdrawal Amount")


        # Not enough balance
        elif amount > current_balance:

            print("Insufficient Balance!")


        else:

            # Updating balance
            current_balance = current_balance - amount

            print("Withdrawal Successful!")
            print(f"Remaining Balance: ₹{current_balance}")



    # Deposit
    elif choice == 3:

        amount = int(input("Enter deposit amount: "))


        if amount <= 0:

            print("Invalid Deposit Amount")


        else:

            # Updating balance
            current_balance = current_balance + amount

            print("Deposit Successful!")
            print(f"Updated Balance: ₹{current_balance}")



    else:

        print("Invalid Choice!")
