import os
import art

# Define functions
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def sub(n1, n2):
    return n1 - n2

# Multiply
def mul(n1, n2):
    return n1 * n2

#Divide
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
  os.system("cls")
  print(art.logo)
  cont = True
  num1 = float(input("What is the first number? "))
  
  # Ask for first number, operator, and second number
  while cont == True:
      for f in operations:
          print(f)
      func = input("What function would you like to perform? ")
      num2 = float(input("What is the next number? "))
      calculate = operations[func]
      answer = calculate(num1, num2)
  
      print(f"{num1} {func} {num2} = {answer}")
  
      if input("Continue? 'y' or 'n' to start a new operation: ").lower() == 'y':
          num1 = answer
      else:
          cont = False
          calculator()

calculator()