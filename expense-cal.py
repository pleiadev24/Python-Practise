from enum import Enum
class users:
    def __init__(self,user_id,phone,email):
        self.user_id=user_id
        self.phone=phone
        self.email=email

    def __str__(self,email,user_id):
        return -f"For the {self.user_id},the {self.phone}"

class expense_type(Enum):
    EQUAL ="EQUAL"
    EXACT ="EXACT"
    PERCENT ="PERCENT"
    SHARE ="SHARE"

class Split:
    def __init__(self,user,group):
        self.user=user
        self.group=group


class EqualSplit(Split):
    def calculate_amount(self,total_amount,num_people):
        return round(total_amount/num_people,2)
    
class ExactSplit(Split):
    def __init__(self, user, amount):
        super().__init__(user, None)
        self.amount = amount

    def calculate_amount(self, total_amount, num_people):
        return self.amount


class PercentSplit(Split):
    def __init__(self, user, percent):
        super().__init__(user, None)
        self.percent = percent

    def calculate_amount(self, total_amount, num_people):
        return round(total_amount * (self.percent / 100), 2)

    

class Expense:
    def __init__(self,paid_by,total_amount,num_people,expense_type,splits):
        self.paid_by=paid_by
        self.total_amount = total_amount
        self.num_people = num_people
        self.expense_type=expense_type
        self.splits=splits

    def calculate_splits(self):
        for split in self.splits:
            split.share = split.calculate_amount

class ExpenseManager:
    def __init__(self):
        self.users={}
        self.Expense=[]

    def add_user(self,user,user_id):
        self.users[user,user_id] = user
    
    def add_expense(self,expense):
        self.expenses.append(expense)


                
