# Basic Calculate

def calc(x, y, ops):

    if ops not in '+-/*':
        return 'Wrong Op!!! Choose Operator: "+, -, *, /"!'

    if ops == '+':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x + y))
    if ops == '-':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x - y))
    if ops == '*':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x * y))
    if ops == '/':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x / y))

while True:

	x = int(input('Enter first number: '))
	y = int(input('Enter second number: '))
	ops = input("Choose between +, -, *, / ")

	print(calc(x, y, ops))