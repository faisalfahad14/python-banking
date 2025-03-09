import csv

class Bank:
    def __init__(self, filename):
        self.filename = filename
    def write_data(self):
        with open(self.filename, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["account_id", "first_name", "password", "balance_checking", "balance_savings"])
            writer.writerow([1001, "faisal", "123321faisal", 5000, 10000])
            writer.writerow([1002, "yazeed", "123321yz", 2500, 15000])
    def read_data(self):
        with open(self.filename, "r") as file:
            for i in file:
                print(i.strip())
bank = Bank("bank.csv")
bank.write_data()
bank.read_data() 
