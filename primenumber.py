# https://www.tutorialgateway.org/python-program-to-print-prime-numbers-from-1-to-100/?utm_content=cmp-true
# https://www.programiz.com/python-programming/examples/prime-number-intervals
# https://stackoverflow.com/questions/27748381/printing-primes-less-than-100
# Iterates over the numbers from 2 to 100
for num in range(2, 100):
    # We assume the number is prime
    is_prime = True
    # Checks if the number is divisible by any number from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    # If the number is prime, print it
    if is_prime:
        print(num)