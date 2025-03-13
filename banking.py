import csv

print("""
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                                              
████████╗ ██████╗      █████╗  ██████╗███╗   ███╗███████╗     
╚══██╔══╝██╔═══██╗    ██╔══██╗██╔════╝████╗ ████║██╔════╝     
   ██║   ██║   ██║    ███████║██║     ██╔████╔██║█████╗       
   ██║   ██║   ██║    ██╔══██║██║     ██║╚██╔╝██║██╔══╝       
   ██║   ╚██████╔╝    ██║  ██║╚██████╗██║ ╚═╝ ██║███████╗     
   ╚═╝    ╚═════╝     ╚═╝  ╚═╝ ╚═════╝╚═╝     ╚═╝╚══════╝     
                                                              
██████╗  █████╗ ███╗   ██╗██╗  ██╗                            
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝                            
██████╔╝███████║██╔██╗ ██║█████╔╝                             
██╔══██╗██╔══██║██║╚██╗██║██╔═██╗                             
██████╔╝██║  ██║██║ ╚████║██║  ██╗                            
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝                            
      """)

class Bank:
    def __init__(self, bank_file):
        self.bank_file = bank_file
        self.customers = []
        self.load_customers()

    def load_customers(self):
        with open(self.bank_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None) 
            self.customers = [account if len(account) == 8 else account + ["0"] for account in reader]
            
            for customer in self.customers:
                customer[7] = int(customer[7])
    def save_cust(self):
        with open(self.bank_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Account ID", "Account Type", "First Name", "Last Name", "Password", "Checking Balance", "Savings Balance", "Overdraft Flag"])
            writer.writerows(self.customers)
            
    def find_customer(self, account_id):
        return next((customer for customer in self.customers if customer[0] == account_id), None)
            
    def generate_account_id(self):
        if not self.customers:
            return 1001
        else:
            last_id = int(self.customers[-1][0])
            return last_id + 1

    def create_account(self):
        first_name = input("Enter your first name: ").strip().title()
        last_name = input("Enter your last name: ").strip().title()
        password = input("Enter your password: ").strip()

        print("Choose your account type:")
        print("1. Checking")
        print("2. Savings")
        print("3. Both")

        account_type = None
        while True:
            choice = input("Enter choice (1/2/3): ")
            account_type = {"1": "Checking", "2": "Savings", "3": "Both"}.get(choice)
            if account_type:
                break
            else:
                print("wrong choice. Please select again.")

        account_id = self.generate_account_id()
        chec_balance = 0
        save_balance = 0
        self.customers.append([account_id, account_type, first_name, last_name, password, chec_balance, save_balance])
        self.save_cust()
        print(f"Welcome {first_name}, your account has been created, Your account ID is {account_id}")

    def login(self):
        while True:
            account_id = input("Enter your account ID: ").strip()
            password = input("Enter your password: ").strip()

            for customer in self.customers:
                if customer[0] == account_id and customer[4] == password:
                    print(f"""---------------------------------------
|   Welcome back, {customer[2]} {customer[3]}  |
---------------------------------------""")
                    return account_id
            print("wrong account ID or password.")

class Withdraw:
    def __init__(self, bank_file):
        self.bank_file = bank_file
        self.customers = []
        self.load_customers()

    def load_customers(self):
        with open(self.bank_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None) 
            self.customers = [account if len(account) == 8 else account + ["0"] for account in reader]
            
            for customer in self.customers:
                customer[7] = int(customer[7])

    def save_cust(self):
        with open(self.bank_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Account ID", "Account Type", "First Name", "Last Name", "Password", "Checking Balance", "Savings Balance", "Overdraft Flag"])
            writer.writerows(self.customers)

    def withdraw_from_checking(self, account_id, amount):
        for customer in self.customers:
            if customer[0] == account_id:
                current_balance = float(customer[5])
                overdraft_flag = int(customer[7])
                print(current_balance)
                print(amount)
                print(current_balance-amount)
                if (current_balance - amount) < 0:
                    print("You are being charged a $35 overdraft fee.")
                    amount += 35
                    customer[7] = 1
                print(amount)
                if current_balance - amount >= -100:
                    customer[5] = current_balance - amount
                    print(f"Successfully withdrew {amount} from Checking account.")
                    self.save_cust()
                    return True
                else:
                    print("Insufficient funds in Checking account.")
                    return False


    def withdraw(self, account_id):
        print("Choose the account type to withdraw from:")
        print("1. Checking")
        print("2. Savings")
        while True:
            choice = input("Enter choice (1/2): ").strip()
            if choice == "1":
                amount = float(input("Enter amount to withdraw from Checking: "))
                if self.withdraw_from_checking(account_id, amount):
                    break
            elif choice == "2":
                amount = float(input("Enter amount to withdraw from Savings: "))
                if self.withdraw_from_savings(account_id, amount):
                    break
            else:
                print("wrong choice, please select again.")
                print("1. Checking")
                print("2. Savings")
                                
class Deposit(Bank):
    def __init__(self, bank_file):
        super().__init__(bank_file)

    def deposit(self, account_id):
        print("Please choose the account type you'd like to deposit into:")
        print("1. Checking Account")
        print("2. Savings Account")

        while True:
            account_choice = input("Enter your choice (1/2): ").strip()
            if account_choice == "1":
                account_type = "Checking"
                balance_index = 5
                break
            elif account_choice == "2":
                account_type = "Savings"
                balance_index = 6
                break
            else:
                print("Invalid choice, please try again.")

        amount = float(input("Enter the amount you'd like to deposit: "))

        for customer in self.customers:
            if customer[0] == account_id:
                current_balance = float(customer[balance_index])
                customer[balance_index] = float(customer[balance_index]) + amount
                self.save_cust()
                print(f"Successfully deposited {amount} into your {account_type} account.")
                break
            
class Transfer(Bank):
    def __init__(self, bank_file):
        super().__init__(bank_file)

    def transfer_funds(self, from_acc, to_acc, amount):
        if from_acc and to_acc and amount > 0 and float(from_acc[5]) >= amount:
            from_acc[5] = str(float(from_acc[5]) - amount)
            to_acc[5] = str(float(to_acc[5]) + amount)
            self.save_cust()
            print(f"Transfer of {amount} successful.")
        else:
            print("Transfer failed. Check balance and input details.")

    def trans_same_acc(self, account_id):
        customer = self.find_customer(account_id)
        if customer:
            print("Choose account to transfer from:")
            print("1. Checking")
            print("2. Savings")
            from_type = None
            while True:
                choice = input("Enter choice (1/2): ").strip()
                if choice == "1":
                    from_type = 5
                    to_type = 6
                    break
                elif choice == "2":
                    from_type = 6
                    to_type = 5
                    break
                else:
                    print("wrong choice, please try again.")
            
            amount = float(input("Enter amount: "))
            if amount > 0 and float(customer[from_type]) >= amount:
                customer[from_type] = str(float(customer[from_type]) - amount)
                customer[to_type] = str(float(customer[to_type]) + amount)
                self.save_cust()
                print(f"Transferred {amount} between your accounts.")
            else:
                print("not enough funds or wrong amount.")

    def trans_another_acc(self):
        to_id = input("Recipient Account ID: ")
        from_cust = self.find_customer(account_id)
        to_cust = self.find_customer(to_id)
        if from_cust and to_cust:
            amount = float(input("Enter amount: "))
            self.transfer_funds(from_cust, to_cust, amount)
        else:
            print("wrong account details.")
                             
bank_system = Bank("bank.csv")

print("Do you have an account or want to create a new one?")
print("1. Create a new account")
print("2. Login")

while True:
    choice = input("Enter your choice (1/2): ").strip()
    if choice == "1":
        bank_system.create_account()
        break
    elif choice == "2":
        account_id = bank_system.login()
        break
    else:
        print("Wrong choice, please try again.")


withdraw_system = Withdraw("bank.csv")
deposit_system = Deposit("bank.csv")
transfer_system = Transfer("bank.csv")


while True:
    print("""What would you like to do today?
    1. Deposit money
    2. Withdraw money
    3. Transfer money""")
    operation = input("Enter your choice (1/2/3): ").strip()
    if operation == "1":
        deposit_system.deposit(account_id)
    elif operation == "2":
        withdraw_system.withdraw(account_id)
    elif operation == "3":
        print("Is this transfer to your own account or another account?")
        print("1. To same account")
        print("2. To another account")
        transfer_choice = input("Enter your choice (1/2): ").strip()
        if transfer_choice == "1":
            transfer_system.trans_same_acc(account_id)
        elif transfer_choice == "2":
            transfer_system.trans_another_acc()
    else:
        print("Wrong choice, please try again")

    print("\nDo you want to do another operation or logout?")
    print("1. Another operation")
    print("2. Logout")
    
    choice = input("Enter your choice (1/2): ").strip()
    if choice == "1":
        continue
    elif choice == "2":
        print("goodbye")
        break
    else:
        print("wrong choice, please try again.")