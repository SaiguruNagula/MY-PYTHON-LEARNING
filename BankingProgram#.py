import time
database= {
    "12345": {"name": "Alice", "balance": 1000 , 'password': "password123"},
    "67890": {"name": "Bob", "balance": 500, 'password': "mypassword"},
    "54321": {"name": "Charlie", "balance": 1500, 'password': "charliepass"},
    "98765": {"name": "David", "balance": 2000 , 'password': "davidpass"},
    "11223": {"name": "Eve", "balance": 750 , 'password': "evepass"},
   }

def show_balance(acc_no,database,):
    print(f"Your current balance is: {database[acc_no]['balance']}")

def deposit(acc_no,database):
    amt = int(input("Enter the amount to deposit: "))
    if amt <= 0:
        print("Deposit amount must be positive.")
    else:
        database[acc_no]['balance'] += amt
        print(f"Deposited {amt}. New balance is: {database[acc_no]['balance']}")

def withdraw(acc_no,database):
    amt=int(input("Enter the amount to withdraw: "))
    if amt <= 0:
        print("Withdrawal amount must be positive.")
    elif amt > database[acc_no]['balance']:
        print("Insufficient balance for this withdrawal.")
    else:
        database[acc_no]['balance'] -= amt
        print(f"Withdrew {amt}. New balance is: {database[acc_no]['balance']}")

def transfer(acc_no,database):
    acc_no2 = (input("Enter the account number to transfer to: "))
    if acc_no2 not in database:
        print("Account number not found. Please check the account number and try again.")
        return
    amt = int(input("Enter the amount to transfer: "))
    if amt <= 0:
        print("Transfer amount must be positive.")
    elif amt > database[acc_no]['balance']:
        print("Insufficient balance for this transfer.")
    else:
        database[acc_no]['balance'] -= amt
        database[acc_no2]['balance'] += amt
        print(f"Transferred {amt} to account {acc_no2}. New balance is: {database[acc_no]['balance']}")

def main():
    
    is_playing = True
    while is_playing:
     print("welcome to the banking program")

     acc_no = (input("Enter your account number: "))
     print("Please wait while we process your request...")
     time.sleep(3)

     if  not acc_no.isdigit() or len(acc_no) != 5:
        print("Invalid account number. Please enter a 5-digit number.")
        continue
    
     if acc_no in database:
        print(f"Welcome {database[acc_no]['name']}!")
        password = input("Enter your password: ")
        print("Please wait while we are checking ...")
        time.sleep(3)

        if password == database[acc_no]['password']:
            while is_running := True:
                print("\nMenu:")
                print("1. Show Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. Exit")

                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    print("Please wait while we process your request...")
                    time.sleep(3)
                    show_balance( acc_no,database)
                elif choice == '2':
                    print("Please wait while we process your request...")
                    time.sleep(3)
                    deposit(acc_no,database)
                elif choice == '3':
                    print("Please wait while we process your request...")
                    time.sleep(3)
                    withdraw(acc_no,database)
                elif choice == '4':
                    print("Please wait while we process your request...")
                    time.sleep(3)
                    transfer(acc_no,database)
                elif choice == '5':
                    print("Please wait while we process your request...")
                    time.sleep(3)
                    print("Thank you for using the banking program!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            print("do u want to continue? (yes/no)")
            continue_choice = input("Enter your choice (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                print("Thank you for using the banking program!")
                is_running = False
        
        else: 
            print("Incorrect password. Please try again.")
            print("do u want to continue? (yes/no)")
            continue_choice = input("Enter your choice (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                print("Thank you for using the banking program!")
                is_playing = False

     else:
        print("Account number not found. Please check your account number and try again.")
        print("do u want to continue? (yes/no)")
        continue_choice = input("Enter your choice (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Thank you for using the banking program!")
            is_playing = False
    print("Thank you for using the banking program!")

if __name__ == "__main__":
    main()
# This code is a simple banking program that allows users to check their balance, deposit money, withdraw money, and transfer money.
