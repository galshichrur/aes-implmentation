import math
from rsa.core import PublicKey, PrivateKey


def rsa_keys(primes: tuple[int, int]) -> tuple[PrivateKey, PublicKey]:
    p = primes[0]
    q = primes[1]

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if math.gcd(e, phi) != 1:
        e = 3
        while math.gcd(e, phi) != 1:
            e += 2
    print(f"e chosen to be: {e}.")

    d = pow(e, -1, phi)
    print(f"d: {d}")

    return PrivateKey(n, d), PublicKey(n, e)