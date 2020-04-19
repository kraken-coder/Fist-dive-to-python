# A function is a block of code which only runs when it is called. unlike javasctipt, we dont use curly braces, we use indentation

#  creating a function
def say_hello(name = "Sam" ):
    print(f'Hello {name}')

#  function return
def get_sum(num1, num2):
    total = num1 + num2
    return total
num = get_sum(2, 5)

#  Lambda functions
#  a version of arrow functions in javascript
get_sum = lambda num1, num2 : num1 + num2



