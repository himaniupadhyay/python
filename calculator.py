# ADD
def sum(a, b):
    return a + b


# SUBTRACT
def sub(a, b):
    return a - b


# MULTIPLICATION
def mul(a, b):
    return a * b


def div(a=0, b=0):
    return a / b


print('SELECT THE OPREATION:')
print('1. ADD')
print('2. SUBTRACTION')
print('3. MULTIPICATION')
print('4. DIVISION')

selector = input('ENTER YOUR CHOICE(1/2/3/4) :')

number1 = int(input('ENTER YOUR 1st Number :'))
number2 = int(input('ENTER YOUR 2nd Number :'))

if selector == 1:
    print(number1, "+", number2, "=", sum(number1, number2))
elif selector == 2:
    print(number1, "-", number2, "=", sub(number1, number2))
elif selector == 3:
    print(number1, "*", number2, "=", mul(number1, number2))
elif selector == 4:
    print(number1, "/", number2, "=", div(number1, number2))
else:
    print 'INVALID CHOICE'
