class User:
    #  constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def greetings(self):
        return f'My name is {self.name}and i am {self.age} '
    #  init user object

#  extend class

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
        
    def set_balance(self, balance):
        self.balance = balance

    def greetings(self):
        return f'My name is {self.name}and i am {self.age}. My account balance is {self.balance} '
    
#  init user
brad = User('Brad Traversy', 'brad@gmail.com',
30) 

#  init customer
janet = Customer("Janet j", "h@j.com", 30 )

janet.set_balance(500)
print(janet.greetings())