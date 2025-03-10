import csv
import os

class checacc:
    def __init__(slef, balance=0):
            slef.balance = balance

class saveacc: 
    def __init__(slef, balance=0):
        slef.balance = balance
        
class cus_acc:
    def __init__(slef, first_name, last_name):
        slef.first_name = first_name
        slef.last_name = last_name
        slef.full_name = f"{first_name} {last_name}"
        slef.chec_acc = None
        slef.save_acc = None
        
    def add_chec_acc(slef, balance=0):
        if not slef.chec_acc:
            slef.chec_acc = checacc(balance)
            print(f"{slef.first_name} has opened a checking account with balance: ${balance}")
        else:
            print(f"{slef.first_name} already has a saving account.")
            
    def add_save_acc(slef, balance=0):
        if not slef.save_acc:
            slef.save_acc = saveacc(balance)
            print(f"{slef.first_name} has openes a saving account with balance ${balance}")
        else:
            print(f"{slef.first_name} already has a savings accoun. ")
            
    def save_csv(self, file="bank.csv"):
        file_exit = os.path.isfile(filename)
        with open(filename, mode="a", newline="") as file:
          writer = csv.writer(file)
        if not file_exit:
            writer.writerow(["first name", "last name", "full name", "chec balance", "save balance"])
        chec_balance = self.chec_acc.balance if self.chec_acc else 0
        save_balance = self.save_acc.balance if self.save_acc else 0
        writer.writerow([self.first_name, self.last_name, self.full_name, chec_balance, save_balance])
    def info(self):
        print(f"hum{self.full_name} has been registerrd")
        chec_balance = self.chec_acc.balacne if self.chec_acc else 0
        save_balance = self.save_acc.balacne if self.save_acc else 0
        print(f"check balance: ${chec_balance}, save balance ${save_balance}")