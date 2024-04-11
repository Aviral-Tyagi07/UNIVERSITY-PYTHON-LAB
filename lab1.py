def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2

def modulos(n1,n2):
    return n1%n2

#this function calculate the product
def calculator():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '%':modulos
    }
    #for taking input from the user
    while True:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+,-,*,/,%): ")
        num2 = float(input("Enter second number: "))

        if op in operations:
            result = operations[op](num1, num2)
            print(f"{num1} {op} {num2} = {result}")
        elif op == 'ma0007':
            print("Exiting calculator...")
            break
        else:
            print("Invalid operator")

calculator()
     
