class Employee:
    def __init__(self, name, **kwargs):
        self.name = name
        self.params = kwargs

    def get_pay(self):
        total_pay = 0
        if 'salary' in self.params:
            total_pay += self.params['salary']
        else:
            total_pay += self.params['hourly_wage'] * self.params['hours_worked']

        if 'bonus' in self.params:
            total_pay += self.params['bonus']
        elif 'contracts_landed' in self.params:
            total_pay += self.params['contracts_landed'] * self.params['commission_per_contract']

        return total_pay

    def __str__(self):
        description = f"{self.name} works on a "
        if 'salary' in self.params:
            description += f"monthly salary of {self.params['salary']}"
        else:
            description += f"contract of {self.params['hours_worked']} hours at {self.params['hourly_wage']}/hour"

        if 'bonus' in self.params:
            description += f" and receives a bonus commission of {self.params['bonus']}"
        elif 'contracts_landed' in self.params:
            description += f" and receives a commission for {self.params['contracts_landed']} contract(s) at {self.params['commission_per_contract']}/contract"

        description += f". Their total pay is {self.get_pay()}."
        return description



billie_params = {'salary': 4000}
charlie_params = {'hourly_wage': 25, 'hours_worked': 100}
renee_params = {'salary': 3000, 'contracts_landed': 4, 'commission_per_contract': 200}
jan_params = {'hourly_wage': 25, 'hours_worked': 150, 'contracts_landed': 3, 'commission_per_contract': 220}
robbie_params = {'salary': 2000, 'bonus': 1500}
ariel_params = {'hourly_wage': 30, 'hours_worked': 120, 'bonus': 600}

billie = Employee('Billie', **billie_params)
charlie = Employee('Charlie', **charlie_params)
renee = Employee('Renee', **renee_params)
jan = Employee('Jan', **jan_params)
robbie = Employee('Robbie', **robbie_params)
ariel = Employee('Ariel', **ariel_params)
