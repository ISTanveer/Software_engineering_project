from abc import ABC, abstractmethod
from user_admin import common, user, Admin
class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.users = []
        self.admins = []
        self.__total_amount = 0
        self.__loan_taken = 0
        self.loan_feature = True
        
    def amount(self):
        return self.total_amount
    
    def add_user(self, user):
        tem = len(self.users)+1
        user.ac_no = f'AC{tem}'
        self.users.append(user)
        self.__total_amount += user.balance
        
    def diposit(self, user, balance):
        if user in self.users:
            user.add_balance(balance)
            print(f'Balance Tk. - {balance} is suceessed....')
            self.__total_amount += balance
        else:
            print(f'Sorry, we do not find your account.........!')
            
    def withdrawal(self, user, balance):
        if user in self.users:
            if user.balance <balance:
                print(f'Your account do not have saficiant balancee....')
            else:
                if self.__total_amount >= balance:
                    user.withd_balance(balance)
                    self.__total_amount -= balance
                    print(f'you withdraw--{balance} and now ur account has--{user.balance}')
                else:
                    print(f'Sorry, The bank is bankrupt.......................!')
                
        else: 
            print(f'We do not get your account.......!')
    
    
    def check_balance(self, user):
        if user in self.users:
            print(f'Your balance is ---{user.balance}')
        else:
            print(f'We do not find ur account......')
     
            
    def transfer_balance(self, user1, user2, balance):
        if user1 in self.users and user2 in self.users:
            if user1.balance >= balance:
                user.trans_balance(user1, user2, balance)
                print(f'Transfer successed.............!')
            else:
                print(f'Not saficiant balance..........!')
        else:
            print(f'we do not find those account...............!')
            
    def check_trans_history(self, user):
        if user in self.users:
            user.trans_his_display()
        else:
            print(f'Account not found...........!')
    
    
    def take_a_loan(self, user, balance):
        if self.loan_feature == True:
            if user in self.users:
                if self.__total_amount>=balance and user.balance*2 >= balance:
                    user.take_loan(balance)
                    self.__total_amount -= balance
                    self.__loan_taken +=balance
                    print(f'you get the loan succeessfully...........')
                else:
                    print(f'Not permittable for loan.......sorry.......!')
            else:
                print(f'User not found................!')
        else:
            print(f'Sorry, loan features is off...................!')
            
    
    def add_admin(self, admin):
        if admin in self.admins:
            print(f'Same admin present.........error')
        else:
            admin.emp_id = len(self.admins) + 1
            self.admins.append(admin)
    

    def total_balance(self, admin):
        if admin in self.admins:
            return f'The Total balance of {self.name} is Tk. = {self.__total_amount}'
        else:
            return f'we can not share the confidencial info.............!'
        
    def total_loan(self, admin):
        if admin in self.admins:
            return f'The Total loan of {self.name} is Tk. = {self.__loan_taken}'
        else:
            return f'we can not share the confidencial info.............!'
        
    def controling_loan(self, admin, control):
        if admin in self.admins:
            if control == 'ON':
                self.loan_feature = True
            else:
                self.loan_feature = False
            return f'Action successed...............!'
        else:
            return f'You cannot control the features of loan..........!'
    
    def __repr__(self):
        print()
        print(f'-----{self.name}---------')
        print(f'{self.address}------')
        print()
        print(f'----------users are---------')
        for user in self.users:
            #print(user.name, user.balance)
            print(user)
        print("--------------------------------")
        print()
        print("----------Admins are------------")
        for ad in self.admins:
            print(ad)
        print("-------------------------------")
        return ''
         
  
      
b = Bank("AB bank", "Uttara")

#user add in bank..
ur1 = user("Iftaker", "ift@gmail.com", 122, 10000)
b.add_user(ur1)
ur2 = user("Siddique", "sid@gmail.com", 123, 3000)
b.add_user(ur2)
ur3 = user("Tanveer", "tan@gmail.com", 153, 50000)
b.add_user(ur3)


b.diposit(ur2, 3000)
print()
b.withdrawal(ur3, 10000)
print()
b.check_balance(ur1)
print()
b.transfer_balance(ur3, ur2, 500)
print()
b.take_a_loan(ur1, 500)
print()
b.take_a_loan(ur2, 100000)
print()
b.check_trans_history(ur2)
print()
a1 = Admin("Iftaker Tanveer", "Ef@gmail.com", 251)
b.add_admin(a1)
a2 = Admin("Rafi Alam", "rf@gmail.com", 258)
b.add_admin(a2)
a3 = Admin("Rafi Alam", "rf@gmail.com", 258)

a3.Check_total_balance(b)
print()
a2.Check_total_balance(b)
print()

a3.Check_total_loan(b)
print()
a2.Check_total_loan(b)
print()

a1.control_loan(b, 'OFF')
print()
a3.control_loan(b, 'OFF')

print(b)
