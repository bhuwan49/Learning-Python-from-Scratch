"""  """
import random

class BankAccount:
    """
    A class to represent a customer's bank account.
    Demonstrates encapsulation by bundling data and operations together.
    """
    def __init__(self, name, initial_deposit):
        # Generate a unique 5-digit account number as a string
        self.account_number = str(random.randint(10000, 99999))
        self.account_holder = name
        self.balance = float(initial_deposit)
        print(f"\n[SUCCESS] Account successfully created for {self.account_holder}!")
        print(f"Account Number: {self.account_number} | Opening Balance: ${self.balance:,.2f}")

    def check_balance(self):
        """Displays current available balance."""
        print(f"\nAccount Details:")
        print(f"Holder: {self.account_holder}")
        print(f"Account No: {self.account_number}")
        print(f"Available Balance: ${self.balance:,.2f}")
        return self.balance

    def deposit(self, amount):
        """Deposits a positive amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"\n[SUCCESS] Deposited ${amount:,.2f}")
            print(f"New Balance: ${self.balance:,.2f}")
        else:
            print("\n[ERROR] Deposit amount must be positive!")

    def withdraw(self, amount):
        """Withdraws money after validating available funds."""
        if amount <= 0:
            print("\n[ERROR] Withdrawal amount must be positive!")
        elif amount > self.balance:
            print(f"\n[ERROR] Insufficient funds! Your balance is ${self.balance:,.2f}")
        else:
            self.balance -= amount
            print(f"\n[SUCCESS] Withdrew ${amount:,.2f}")
            print(f"Remaining Balance: ${self.balance:,.2f}")


def main():
    # Database dictionary to simulate database tracking of active accounts
    bank_database = {}
    
    print("==============================================")
    print("Welcome to the XYZ Bank ")
    print("==============================================")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Create New Bank Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Account Balance")
        print("5. Exit Application")
        
        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            name = input("Enter Account Holder's Full Name: ").strip()
            if not name:
                print("[ERROR] Name field cannot be empty.")
                continue
            try:
                initial_deposit = float(input("Enter Initial Deposit Amount: $"))
                if initial_deposit < 0:
                    print("[ERROR] Initial deposit cannot be negative.")
                    continue
            except ValueError:
                print("[ERROR] Invalid amount entered. Please type a number.")
                continue
            
            # Instantiate the object and map it in our tracking dictionary
            new_account = BankAccount(name, initial_deposit)
            bank_database[new_account.account_number] = new_account

        elif choice in ['2', '3', '4']:
            acc_num = input("Enter 5-digit Account Number: ").strip()
            
            # Validation layer: verify account existence before performing tasks
            if acc_num not in bank_database:
                print("[ERROR] Account number not found. Please try again.")
                continue
                
            account = bank_database[acc_num]

            if choice == '2':
                try:
                    amount = float(input("Enter Deposit Amount: $"))
                    account.deposit(amount)
                except ValueError:
                    print("[ERROR] Invalid numeric input.")
            
            elif choice == '3':
                try:
                    amount = float(input("Enter Withdrawal Amount: $"))
                    account.withdraw(amount)
                except ValueError:
                    print("[ERROR] Invalid numeric input.")
            
            elif choice == '4':
                account.check_balance()

        elif choice == '5':
            print("\nThank you for using the Banking Technology Application. Goodbye!")
            break
        else:
            print("[ERROR] Invalid entry. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
