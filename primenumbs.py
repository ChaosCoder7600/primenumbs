__author__ = 'todd'

# print(9 % 2)


def iseven(numb):
    if numb % 2 == 0:
        return True
    else:
        return False

def isprime(num):
    i = 2
    isprime=True
    while i < num - 1:
        if (num % i) == 0:
            isprime = False
        i += 1
    if isprime:
        return num

def print_prime_numbs(num_of_primes):
    i = 5
    print(1)
    print(2)
    print(3)
    while i <= num_of_primes:
        if not iseven(i):
            if isprime(i):
                print(i)
    i += 1
