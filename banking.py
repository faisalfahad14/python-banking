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
            self.customers = [account for account in reader]

    def save_cust(self):
        with open(self.bank_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Account ID", "Account Type", "First Name", "Last Name", "Password", "Checking Balance", "Savings Balance"])
            writer.writerows(self.customers)

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
                    return True
            print("wrong account ID or password.")
            

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
        if bank_system.login():
            break
    else:
        print("wrong choice, please try again.")

print("""What would you like to do today?
1. Deposit money
2. Withdraw money
3. Transfer money""")

while True:
    operation = input("Enter your choice (1/2/3): ").strip()
    if operation == "1":
        
        break
    elif operation == "2":
        
        break
    elif operation == "3":
        break
    
    else:
        print("wrong choice, please try again")