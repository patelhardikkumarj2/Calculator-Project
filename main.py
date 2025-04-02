from multiprocessing.connection import answer_challenge
from operator import truediv
import art
# print(art.logo)

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

cal_dict = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
def calculator():
    print(art.logo)
    go_ahead = True
    num_1 = float(input("What is the first number?: \n"))
    while go_ahead:


            for symbols in cal_dict:
                print(symbols)

            operation = input("Pick an operation:")
            num_2 = float(input("What is the next number?: \n"))
            answer = cal_dict[operation](num_1,num_2)
            print(f"{num_1} {operation} {num_2} = {answer}")
            next = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()

            if next == 'y':
                num_1 = answer
            else:
                go_ahead = False
                calculator()
calculator()

