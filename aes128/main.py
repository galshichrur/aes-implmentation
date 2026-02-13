from aes128.add_round_key import add_round_key
from aes128.key_expansion import expand_key
from aes128.substitution import substitute_bytes, inverse_substitute_bytes
from aes128.shift_rows import shift_rows, inverse_shift_rows
from aes128.mix_columns import mix_columns, inverse_mix_columns
from aes128.state import State, state_to_bytes, bytes_to_state


def aes128_encrypt(key: bytes, plaintext: bytes) -> bytes:
    assert len(key) == 16, "The key size must be 16 bytes."
    assert len(plaintext) == 16, "The plaintext size must be 16 bytes."

    keys: list[State] = expand_key(bytes_to_state(key))
    state: State = bytes_to_state(plaintext)

    for round_num in range(11):
        current_key: State = keys[round_num]
        if round_num == 0:
            add_round_key(current_key, state)
        else:
            substitute_bytes(state)
            shift_rows(state)
            if round_num != 10:
                mix_columns(state)

            add_round_key(current_key, state)

    return state_to_bytes(state)

def aes128_decrypt(key: bytes, ciphertext: bytes) -> bytes:
    assert len(key) == 16, "The key size must be 16 bytes."
    assert len(ciphertext) == 16, "The ciphertext size must be 16 bytes."

    keys: list[State] = expand_key(bytes_to_state(key))
    state: State = bytes_to_state(ciphertext)

    for round_num in range(11):
        current_key: State = keys[10 - round_num]
        if round_num == 0:
            add_round_key(current_key, state)
        else:
            inverse_shift_rows(state)
            inverse_substitute_bytes(state)
            add_round_key(current_key, state)

            if round_num != 10:
                inverse_mix_columns(state)

    return state_to_bytes(state)

def test() -> None:
    pt = b"gal_is_the_best_"
    print(f"Plaintext: {pt}")
    key = b"1234567890123456"
    print(f"Key: {key}")
    ct = aes128_encrypt(key ,pt)
    print(f"Ciphertext: {ct}")

    decrypted_pt = aes128_decrypt(key, ct)
    print(f"Decrypted plaintext: {decrypted_pt}")

if __name__ == '__main__':
    test()
