import random


def distant_random_primes(size: int) -> tuple[int, int]:
    each_num_size = size // 2
    print(f"Searching for p, q prime numbers ({each_num_size} bits each).")

    p = random_prime(each_num_size)
    print(f"p = {p} ({bin(p)})")

    left_half_p = get_left_half_bits(p, size)

    while True:
        q = random_prime(each_num_size)

        left_half_q = get_left_half_bits(q, each_num_size)

        if left_half_p != left_half_q:
            print(f"q = {q} ({bin(q)})")
            return p, q
        else:
            print("q is to close to p, trying again.")

def get_left_half_bits(n: int, total_bits: int) -> str:
    binary = bin(n)[2:].zfill(total_bits)
    return binary[:total_bits // 2]

def count_digits(n: int) -> int:
    count = 1
    while n > 9:
        count += 1
        n /= 10
    return count

def random_prime(size: int) -> int:
    count = 1

    n = random.getrandbits(size)

    while not is_prime(n):
        n = random.getrandbits(size)
        count += 1

    print(f"Total of {count} searched numbers.")
    return n

def is_prime(n, k=5):
    if n <= 1 or n % 2 == 0:
        return False
    if n == 2:
        return True

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Miller-Rabin test
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True