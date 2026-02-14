from rsa.core import RSA
from rsa.keys_gen import rsa_keys
from rsa.primes_gen import distant_random_primes


private, public = rsa_keys(distant_random_primes(2056))

ciphertext = RSA.encrypt_bytes(b"test string to encode", public)
print(f"Ciphertext = {ciphertext}")

plaintext = RSA.decrypt_bytes(ciphertext, private)
print(f"Plaintext = {plaintext.decode()}")