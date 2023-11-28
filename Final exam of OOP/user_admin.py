from abc import ABC, abstractmethod
        
       
class common(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid

class user(common):
    def __init__(self, name, email, nid, balance):
        super().__init__(name, email, nid)
        self.balance = balance
        self.loan = 0
        self.tran_history = []
        self.ac_no = None
        
    def add_balance(self, balance):
        self.balance += balance
        self.tran_history.append(f'Deposit balance Tk. - {balance}')
    
    def withd_balance(self, balance):
        self.balance -= balance
        self.tran_history.append(f'Withdrawal balance Tk. - {balance}')
        
    @staticmethod
    def trans_balance(user1, user2, balance):
        user1.balance -= balance
        user2.balance += balance
        user1.tran_history.append(f'Transfer balance Tk. - {balance}')
        user2.tran_history.append(f'Received balance Tk. - {balance}')
        
    def trans_his_display(self):
        print(f'Displaying Transfer History of ----{self.name}')
        for ur in self.tran_history:
            print(ur)
            
    def take_loan(self, balance):
        self.loan = balance
        self.tran_history.append(f'Taking loan from bank Tk. {balance}')
        
        
    def __repr__(self):
        return f'Name is {self.name}-- Account No. {self.ac_no} -- Balance is {self.balance}'
        
                
         
         
class Admin(common):
    def __init__(self, name, email, nid):
        super().__init__(name, email, nid)
        self.emp_id = None
        
    def Check_total_balance(self, bank):
        print(bank.total_balance(self))
        
    def Check_total_loan(self, bank):
        print(bank.total_loan(self))
        
    def control_loan(self, bank, control):
        print(bank.controling_loan(self, control))
        
        
    def __repr__(self):
        return f'Admin name--{self.name}, Employee ID -- {self.emp_id}'
        
    
        