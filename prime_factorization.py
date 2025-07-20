
import sys

def prime_factorization(n):
    """
    Given an integer n, return a list of its prime factors.
    """
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
       factors.append(n)
    return factors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python prime_factorization.py <number>")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
        if number < 2:
            print("Please enter a number greater than 1.")
        else:
            factors = prime_factorization(number)
            print(f"The prime factors of {number} are: {factors}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

