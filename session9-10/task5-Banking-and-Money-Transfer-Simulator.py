#===============================================
#=====================Task 5====================
#===============================================
#====Banking and Money Transfer Simulator=======
#===============================================


class BankAccount:
    def __init__(self, owner, account_number, balance):
        if type(balance) is not int:
            raise TypeError("mojoodi bayad adad bashad.")

        if balance < 0:
            raise ValueError("mojoodi nemitavanad manfi bashad.")
            
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, deposit_amount:int):
        if type(deposit_amount) is not int:
            print("mablaghe variz bayad adad sahih bashad.")
            return
        
        if deposit_amount <= 0:
            print("mablaghe variz bayad bishtar az 0 bashad.")
            return
    
        self.balance = self.balance + deposit_amount
        self.transactions.append(("variz",deposit_amount))
        print("mablaghe moredde nazar be hesab variz shod.")
    
    def withdraw(self, withdraw_amount:int):
        if type(withdraw_amount) is not int:
            print("mablaghe bardasht bayad adad sahih bashad.")
            return
        
        if withdraw_amount <= 0:
            print("mablaghe bardasht bayad bishtar az 0 bashad.")
            return
        
        elif withdraw_amount > self.balance:
            print("mojoodi baraye bardasht kafi nist.")
            return
    
        self.balance = self.balance - withdraw_amount
        self.transactions.append(("bardasht",withdraw_amount))
        print("mablaghe moredde nazar az hesab bardasht shod.")
    
    def get_balance(self):
        return self.balance

    
    def transaction_history(self):
        print("========== Transaction History ==========")
        print(f"Account Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print("-----------------------------------------")
    
        if not self.transactions:
            print("No transactions found.")
    
        else:
            for number, (transaction_type, amount) in enumerate(self.transactions, start=1):
                if transaction_type == "variz":
                    print(f"{number}. Variz: +{amount:,}")
    
                elif transaction_type == "bardasht":
                    print(f"{number}. Bardasht: -{amount:,}")
                    
                elif transaction_type == "enteghal":
                    print(f"{number}. enteghal: -{amount:,}")
                    
                elif transaction_type == "daryaft":
                    print(f"{number}. daryaft: +{amount:,}")    
    
        print("-----------------------------------------")
        print(f"Total Transactions: {len(self.transactions)}")
        print("=========================================")

    
    def transfer(self, target_account, transfer_amount: int):
        if type(transfer_amount) is not int:
            print("mablaghe enteghal bayad adad sahih bashad.")
            return
        
        if not isinstance(target_account, BankAccount):
            print("hesab maghsad sahih nist.")
            return
        
        if target_account is self:
            print("nemitavan be haman hesab enteghal dad.")
            return
        
        if transfer_amount <= 0:
            print("mablaghe enteghal bayad bishtar az 0 bashad.")
            return
        
        elif transfer_amount > self.balance:
            print("mojoodi baraye enteghal kafi nist.")
            return
        
        else:
            self.balance = self.balance - transfer_amount
            target_account.balance = target_account.balance + transfer_amount
            self.transactions.append(("enteghal", transfer_amount))
            target_account.transactions.append(("daryaft", transfer_amount))
            print("enteghal ba movafaghiat anjam shod.")
    
    def __str__(self):
        return (
            "-------------\n"
            "Bank Account Data:\n"
            f"Owner: {self.owner}\n"
            f"Account number: {self.account_number}\n"
            f"Balance: {self.balance}\n"
            "-------------"
        )




#---------------------test------------------------  

elen_account = BankAccount("Elen", "101", 5000000)
milad_account = BankAccount("milad", "102", 7000000)

print(elen_account)

elen_account.deposit(2000000)
elen_account.deposit("fdvf")
elen_account.deposit(-2000000)

elen_account.transactions

elen_account.withdraw(500000)
elen_account.withdraw(100000)
elen_account.withdraw(-52000)
elen_account.withdraw("vsvf")
elen_account.withdraw(15000000)

elen_account.get_balance()

elen_account.transaction_history()

elen_account.transfer(milad_account, 2500000)
elen_account.transfer(milad_account, 3500000)
elen_account.transfer(milad_account, "jj")
elen_account.transfer(milad_account, -3500000)



print(milad_account)
milad_account.transaction_history()


#----------------------challenge----------------------

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, owner, account_number, balance):
        for each_account in self.accounts:
            if each_account.account_number == account_number:
                print("account number tekrari mibashad.")
                return
        new_account = BankAccount(owner, account_number, balance)   
        self.accounts.append(new_account)
        print("account jadid ba movafaghiat ezafe shod.")
        return new_account
        
        
    def find_account(self, account_number):
        if type(account_number) is not int:
            print("account number bayad adad sahih bashad.")
            return
        
        for each_account in self.accounts:
            if each_account.account_number == account_number:
                return each_account
    
        print("hsabi ba in account number peyda nashod.")
        return None
    
    def total_balance(self):
        total_balance = 0
        for each_account in self.accounts:
            total_balance = total_balance + each_account.balance
            
        print(f"kole mojoodi bank {total_balance} mibashad.")    
        return total_balance    
    
                





my_bank = Bank()

sara_account = my_bank.create_account("sara", 104 , 8600000)

milad_account = my_bank.create_account("milad", 105 , 7500000)


my_bank.find_account(104)
print(my_bank.find_account(104))
print(my_bank.find_account(105))
print(my_bank.find_account("dfs"))



my_bank.total_balance()


















