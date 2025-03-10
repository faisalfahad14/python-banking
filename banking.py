import csv
import os
print("its work")
class checacc:
    def __init__(self, balance=0):
            self.balance = balance

class saveacc: 
    def __init__(self, balance=0):
        self.balance = balance
        
class cus_acc:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.chec_acc = None
        self.save_acc = None
        
    def add_chec_acc(self, balance=0):
        if not self.chec_acc:
            self.chec_acc = checacc(balance)
            print(f"{self.first_name} has opened a checking account with balance: ${balance}")
        else:
            print(f"{self.first_name} already has a saving account.")
            
    def add_save_acc(self, balance=0):
        if not self.save_acc:
            self.save_acc = saveacc(balance)
            print(f"{self.first_name} has openes a saving account with balance ${balance}")
        else:
            print(f"{self.first_name} already has a savings accoun. ")
            
    def save_csv(self, file="bank.csv"):
        file_exit = os.path.isfile(bank.csv)
        with open(bank.csv, mode="a", newline="") as file:
          writer = csv.writer(file)
        if not file_exit:
            writer.writerow(["first name", "last name", "full name", "chec balance", "save balance"])
        chec_balance = self.chec_acc.balance if self.chec_acc else 0
        save_balance = self.save_acc.balance if self.save_acc else 0
        writer.writerow([self.first_name, self.last_name, self.full_name, chec_balance, save_balance])
    def info(self):
        print(f"hum{self.full_name} has been registerrd")
        chec_balance = self.chec_acc.balance if self.chec_acc else 0
        save_balance = self.save_acc.balance if self.save_acc else 0
        print(f"check balance: ${chec_balance}, save balance ${save_balance}")
        first_name = input("Enter your first name : ").strip().titel()
        last_name = input("Enter your last name : ").strip().titel()