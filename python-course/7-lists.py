
print('>>>>> List <<<<<')

primes = [2, 3, 5, 7]

matrix = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]

print(matrix)

my_favourite_things = [32, 'raindrops on roses', help]


print('>>>>> Indexing <<<<<')

print(primes[-1])
print(primes[1:3])
print(primes[:2])
print(primes[2:])

primes[:3] = ['one', 'Three', 'Five']
print(primes)


print('>>>>> List functions <<<<<')

print(len(primes))
print(sorted(primes[:3]))
primes = [2, 3, 5, 7]
print(sum(primes))
print(max(primes))


print('>>>>> List methods <<<<<')

primes.append(11)
primes.pop()

if(5 in primes):
    print(primes.index(5))


print('>>>>> Tuples <<<<<')

t = (1, 2, 3)
# or
t = 1, 2, 3

print(t)

x = 0.125
print(x.as_integer_ratio())
numerator, denominator = x.as_integer_ratio()
print(numerator, denominator)
