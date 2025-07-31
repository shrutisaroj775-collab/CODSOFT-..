## TASK-2
# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perfrom the calculation and display the result 
from termcolor import colored

# Input formatter class
class FormatInput:
    def __init__(self):
        self.expression = input(colored("Enter expression in pattern 'num_1 operator num_2': ", "cyan"))

    def format_exp(self):
        exp = self.expression.strip().split()
        if len(exp) != 3:
            print(colored("Please use correct format :", "red"))
            return 
        try:
            val1 = float(exp[0])
            operator = exp[1]
            val2 = float(exp[2])
            print(colored(f"First Number = {val1}", "magenta"))
            print(colored(f"Operator = {operator}", "magenta"))
            print(colored(f"Second Number = {val2}", "magenta"))
            return val1, val2, operator
        except ValueError:
            print(colored("Got anything other than numbers!", "red"))
            return None, None, None

# Calculator class 
class Calculator:
    def calculate(self, val1, val2, operator):
        if operator == '+':
            return val1 + val2
        elif operator == '-':
            return val1 - val2
        elif operator == '*':
            return val1 * val2
        elif operator == '/':
            if val2 == 0:
                return "Error: Cannot divide by zero"
            return val1 / val2
        else:
            return "Invalid operator"

# Main loop
if __name__ == "__main__":
    while True:
        formatter = FormatInput()
        val1, val2, operator = formatter.format_exp()
        if val1 is None:
            continue
        calc = Calculator()
        result = calc.calculate(val1, val2, operator)
        print(colored(f"Result: {result}", "green"))
        cont = input(colored("Do you want to continue calculation (y/n): ", "yellow"))
        if cont.lower() != 'y':
            print(colored("Calculator closed.", "magenta"))
            break