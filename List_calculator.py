#Code calculates with given method all the values in a list
# Importing colors from colorama
from colorama import Fore, Style, init 

# Creating necessary variables
values = []
z = 0
y = 1
b = ""
g = 0

# Asking calculation method
print (Fore.LIGHTMAGENTA_EX + "\nWanna sum, minus, multiply or divide? (input +, -, * or /)")

# Checking if the character is correct, otherwise error message
while 1 > 0:
    c = input(Fore.LIGHTBLUE_EX)
    if(c == '+') or (c == '-') or (c == '*') or (c == '/'):

        # Ending the check loop
        break
    else:
        print(Fore.LIGHTRED_EX +"Incorrect character")

# Asking and giving a name for the table
print(Fore.LIGHTMAGENTA_EX + "\nTable's name:",)
x = input(Fore.LIGHTBLUE_EX)

# Looping to get an infinite possible amount of values from the user
print(Fore.LIGHTMAGENTA_EX + "\nGive values or input (c) to calculate ")
while 1 > 0:
    g = input(Fore.GREEN + f"{y}:th Value: "+ Fore.LIGHTWHITE_EX)

    # If the value is numeric, it will be placed on the listk, otherwise error message
    if g == 'c':
        # Printing the list with values
        print("")
        print(Fore.LIGHTBLUE_EX + x, Fore.LIGHTWHITE_EX + "=", values)
        # Ending the value loop
        break
    else:
        # Trying to convert the input to float
        try:
            fvalue = float(g)
            values.append(fvalue)
            y += 1
        except:
            print(Fore.LIGHTRED_EX + "Value has to be numeric")

# Looping until all the values have been calculated
while len(values) >= 2:

    # Checking calculation method and calculating the value
    if(c == '+'):
        z = values[0] + values[1]
        values = [z] + values[2:]
    elif(c == '-'):
        z = values[0] - values[1]
        values = [z] + values[2:]
    elif(c == '*'):
        z = values[0] * values[1]
        values = [z] + values[2:]
    elif(c == '/'):
        z = values[0] / values[1]
        values = [z] + values[2:]
# Results
print(Fore.LIGHTBLUE_EX + x ,Fore.LIGHTWHITE_EX + f"= [{z}]")
