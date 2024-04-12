# primes.py
# the program generates prime number, written during lecture
# author: atacan buyuktalas
'''
primes = []

for candidate in range(2, 101):
  #  print(candidate)
    
    # how to check if the number is prime
    isPrime = True # assumed it's a prime
    
    for divisor in range(2,candidate):
        if (candidate % divisor == 0):
            isPrime = False
            break 
    if isPrime:
        primes.append(candidate) # append all prime numbers into the list 'primes'

print(primes)
'''

# Here is more clear and efficient way of doing it

primes = []
upto = 1001

for candidate in range(2,upto):
    isPrime = True
    # only need to check if it divisible by prime
    for divisor in primes:
        # if divisible by an int it is not a prime number
        if (candidate % divisor == 0):
            isPrime = False
            # so there is no reason to keep checking
            break
    if isPrime:
        primes.append(candidate)

print(primes)