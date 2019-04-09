
print('>>>>> Functions applied to functions <<<<<')

print('3.0 == 3', 3.0 == 3, 'Javascript?', sep='  ,  ')
print('\'3\' == 3', '3' == 3, 'Javascript? no', sep='  ,  ')

print('True or True and False ==', True or True and False)
print('and has priority')



print('>>>>> Conditionals <<<<<')

def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)


print('>>>>> Boolean conversion <<<<<')

print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))


print('>>>>> Conditional expressions (aka \'ternary\') <<<<<')

outcome = 'failed' if 1 < 50 else 'passed'
