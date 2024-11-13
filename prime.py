#!/usr/bin/env python3
import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # No even number greater than 2 is prime

    # Check divisibility from 3 upwards, only odd numbers
    for i in range(3, int(math.sqrt(num)) + 1, 2):  # Skip even numbers
        if num % i == 0:
            return False
    return True

# Generate list of prime numbers in the range 1 to 255
primes = [x for x in range(1, 256) if is_prime(x)]

# Count the number of primes
prime_count = len(primes)

# Save the result to a file
with open("results.txt", "w") as file:
    file.write(f"Prime numbers between 1 and 255:\n")
    file.write(", ".join(map(str, primes)) + "\n")
    file.write(f"\nTotal number of primes: {prime_count}\n")

# Print the results to the console
print(f"Prime numbers between 1 and 255: {primes}")
print(f"Total number of primes: {prime_count}")
