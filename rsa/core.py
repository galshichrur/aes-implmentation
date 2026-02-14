import json
import base64
from dataclasses import dataclass
from rsa.primes_gen import distant_random_primes
from typing import Generator


@dataclass
class PublicKey:
    n: int
    e: int

@dataclass
class PrivateKey:
    n: int
    d: int

class RSA:
    @staticmethod
    def _encrypt(data: int, key: PublicKey) -> int:
        return pow(data, key.e, key.n)

    @staticmethod
    def _decrypt(data: int, key: PrivateKey) -> int:
        return pow(data, key.d, key.n)

    @staticmethod
    def _sign(data: int, key: PrivateKey) -> int:
        return pow(data, key.d, key.n)

    @staticmethod
    def _verify(data: int, signature: int, key: PublicKey) -> bool:
        return data == pow(signature, key.e, key.n)

    @staticmethod
    def encrypt_bytes(data: bytes, key: PublicKey) -> bytes:
        encrypted_ints = [RSA._encrypt(m, key) for m in RSA.chunk_bytes(data, key.n)]
        return RSA.encode_json_b64(encrypted_ints)

    @staticmethod
    def sign_bytes(data: bytes, key: PrivateKey) -> bytes:
        signed_ints = [RSA._sign(m, key) for m in RSA.chunk_bytes(data, key.n)]
        return RSA.encode_json_b64(signed_ints)

    @staticmethod
    def decrypt_bytes(data: bytes, key: PrivateKey) -> bytes:
        decoded_data = RSA.decode_json_b64(data)
        decrypted = [RSA._decrypt(c, key) for c in decoded_data]
        return RSA.ints_to_bytes(decrypted, key.n)

    @staticmethod
    def chunk_bytes(data: bytes, n: int) -> Generator[int, None, None]:
        max_bytes = (n.bit_length() - 1) // 8

        for i in range(0, len(data), max_bytes):
            chunk = data[i:i+max_bytes]
            yield int.from_bytes(chunk, byteorder='big')

    @staticmethod
    def ints_to_bytes(ints: list[int], n: int) -> bytes:
        max_bytes = (n.bit_length() - 1) // 8
        return b''.join(i.to_bytes(max_bytes, byteorder='big') for i in ints)

    @staticmethod
    def encode_json_b64(ints: list[int]) -> bytes:
        json_data = json.dumps(ints)
        print(json_data)
        b64_data = base64.urlsafe_b64encode(json_data.encode())

        return b64_data

    @staticmethod
    def decode_json_b64(data: bytes) -> bytes:
        json_data = base64.urlsafe_b64decode(data.decode())
        print(json_data)
        decrypted_data = json.loads(json_data)

        return decrypted_data


def main() -> None:
    private, public = rsa_keys(distant_random_primes(2056))
    original = input("Enter data to encrypt: ")
    ciphertext = RSA.encrypt_bytes(original.encode(), public)
    print(f"Ciphertext = {ciphertext}")
    plaintext = RSA.decrypt_bytes(ciphertext, private)
    print(f"Plaintext = {plaintext.decode()}")

if __name__ == '__main__':
    main()