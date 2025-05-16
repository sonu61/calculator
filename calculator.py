from art import logo
import os

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

Operations ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide    
}
def calculator():
    print(logo)

    should_continue = True
    num1 = float(input("Whats the first number???\n"))
    for op in Operations:
        print(op)
    while should_continue:
        operation_symbol = input("pick the operation from the line above:\n") 
        num2=float(input("Whats the next number???\n"))
        calculation_function = Operations[operation_symbol]
        answer = round(calculation_function(num1,num2) )
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"type 'y' to continue calculating with{answer}, or type 'n' to exit: \n")=='y':
            num1=answer
        else:
            should_continue=False
            os.system('cls')
            calculator()

calculator()