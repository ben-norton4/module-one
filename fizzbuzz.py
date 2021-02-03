def fizz_buzz(numberToCheck):
    output = ''

    if( ((numberToCheck % 3) == 0) and ((numberToCheck % 5) == 0) ):
        output = 'FizzBuzz'
    elif((numberToCheck % 3) == 0):
        output = 'Fizz'
    elif((numberToCheck % 5) == 0):
        output = 'Buzz'
    else:
        output = str(numberToCheck)
    return output

def main():
    for x in range(100):
        print(fizz_buzz(x + 1))


main()

