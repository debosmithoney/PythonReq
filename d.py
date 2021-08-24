add = lambda x, y : x+y
subtract = lambda x, y : x-y
multiply = lambda x, y : x*y
divide = lambda x, y : x/y
modulo = lambda x, y : x%y

print('Select Operation:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

c = int(input('Enter Choice: '))

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if c == 1:
    print(f'{a}+{b}={add(a, b)}')
elif c == 2:
    print(f'{a}-{b}={subtract(a, b)}')
elif c == 3:
    print(f'{a}*{b}={multiply(a, b)}')
elif c == 4:
    print(f'{a}/{b}={divide(a, b)}')
else:
    print("Invalid Input!!!!")
