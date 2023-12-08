"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, salary=0, hours_worked=0, hourly_rate=0, commission=0, bonus_commission=0):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.commission = commission
        self.bonus_commission = bonus_commission


    def get_pay(self):
        return self.get_contract_pay() + self.get_commission_pay()

    def get_contract_pay(self):
        if self.contract_type == "salary":
            return self.salary
        elif self.contract_type == "hourly":
            return self.hours_worked * self.hourly_rate

    def get_commission_pay(self):
        if self.commission > 0 and self.bonus_commission <= 0:
            return self.commission
        elif self.commission > 0 and self.bonus_commission > 0:
            return self.commission * self.bonus_commission
        else:
            return 0

    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
