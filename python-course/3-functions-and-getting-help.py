
print('>>>>> Help function <<<<<')
help(print)
help(abs)




print('>>>>> Create function <<<<<')
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """

    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

help(least_difference)


print('>>>>> Default arguments <<<<<')

print(1, 2, 3, sep=' wut! ')

def greet(wut="???"):
    print('greeting the', wut)
    
greet()
greet("Kaggle")
greet(wut="!!!")


print('\n>>>>> Functions applied to functions <<<<<')

def call(fn, arg):
    fn(arg)

call(greet, 'puntch')

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)