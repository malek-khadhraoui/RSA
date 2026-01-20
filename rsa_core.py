import utils

def generate_keys_manual(p: int, q: int, e: int):
    """
    Accepts manual p, q, e. Computes n, phi, d.
    Validates primes and coprimality of e with phi.
    Returns (public_key, private_key, n, phi).
    """
    if p <= 1 or q <= 1:
        raise ValueError("p and q must be > 1.")
    if not utils.is_prime(p) or not utils.is_prime(q):
        raise ValueError("p and q must be prime.")
    if p == q:
        raise ValueError("p and q must be distinct primes.")

    n = p * q
    phi = (p - 1) * (q - 1)

    if e <= 1 or e >= phi:
        raise ValueError("e must satisfy 1 < e < φ(n).")
    if utils.gcd(e, phi) != 1:
        raise ValueError("e must be coprime with φ(n). Choose another e.")

    d = utils.mod_inverse(e, phi)
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key, n, phi

def encrypt(message: str, pub_key: tuple[int, int]) -> list[int]:
    e, n = pub_key
    return [pow(ord(ch), e, n) for ch in message]

def decrypt(cipher: list[int], priv_key: tuple[int, int]) -> str:
    d, n = priv_key
    return ''.join(chr(pow(c, d, n)) for c in cipher)
