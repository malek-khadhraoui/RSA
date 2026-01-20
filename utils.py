# Pure Python helpers — no Sympy, no recursion

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    # Iterative Extended Euclidean Algorithm
    a, b = e, phi
    x0, x1 = 1, 0
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
    if a != 1:
        raise ValueError("No modular inverse exists for given e and φ(n).")
    return x0 % phi

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
