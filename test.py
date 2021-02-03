def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculate (operator, parameterA, parameterB):
    result = 0
    if((operator == '*') or (operator == 'x')):
        result = multiply(parameterA, parameterB)
    elif(operator == '+'):
        result = add(parameterA, parameterB)
    elif(operator == '-'):
        result = subtract(parameterA, parameterB)
    elif(operator == '/'):
        result = divide(parameterA, parameterB)
    else:
        result = 0
    return result

#myOperator = input('Please input a mathematical operator: ')
#myParameterA = int(input('Please input first integer: '))
#myParameterB = int(input('Please input second integer: '))

#result = calculate(myOperator, myParameterA, myParameterB)
#print(result)


result = 0

with open('numbers.txt', 'r') as input_file:
    text_lines = input_file.read().splitlines()

for line in text_lines:
    line_parts = line.split()
    operator = line_parts[1]
    int_a = int(line_parts[2])
    int_b = int(line_parts[3])
    result = result + calculate(operator, int_a, int_b)
      
print(result)



text_lines

with open('numbers2.txt', 'r') as input_file:
    text_lines = input_file.read().splitlines()

for line in text_lines:
    line_parts = line.split()
    goto_or_calc = line_parts[0]
    line_to_goto = line_parts[1]
    operator = line_parts[2]
    int_a = int(line_parts[3])
    int_b = int(line_parts[4])

    if line_to_goto == 'calc':
        line_parts.append(calculate(operator, int_a, int_b))
    else:
        line_parts.append(int(line_to_goto))

    

