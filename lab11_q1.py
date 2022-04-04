
# add method that returns sum of input1 and input2
def adder(input1, input2):
    return (input1 + input2)
    
# subtract method that returns the difference of input1 and input2
def subtractor(input1, input2):
    return (input1 - input2)

# multiply method that returns the product of input1 and input2
def multiplier(input1, input2):
    return (input1 * input2)
    
# divide method that returns the result of input1 / input2
def divider(input1, input2):
    return (input1 / input2)
    
# resets the calculator to 0
def clear():
    print("Calculator is reset to 0.")
    input1 = 0
    input2 = 0
    return input1, input2

# user inputs input1, the symbol, input2
input1 = int(input('Enter 1st number: '))
symbol = input('Enter symbol (+, -, *, /):')
input2 = int(input('Enter 2nd number: '))


# call the functions according to the symbols and prints result of the calculations
if symbol == '+':
    print("Addition of ", input1, "and", input2, "is", adder(input1, input2))
elif symbol == '-':
    print("Subtraction of ", input1, "and", input2, "is", subtractor(input1, input2))
elif symbol == '*':
    print("Multiplication of ", input1, "and", input2, "is", multiplier(input1, input2))
elif symbol == '/':
    print("Division of ", input1, "and", input2, "is", divider(input1, input2))

# calcultor resets
clear()


