from aes128.state import State, state_to_bytes, bytes_to_state
from utils import xor_bytes, s_box


rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

def expand_key(key: State) -> list[State]:
    """
    Expands 16 bytes AES key (as a 4x4 state) into 11 round keys for AES-128.
    """
    words: list[bytes] = []

    # Insert the first 4 words from the key
    for col in range(4):
        word = b""
        for row in range(4):
            word += key[row][col].to_bytes(1, "big")
        words.append(word)

    # Generate the remaining 40 words
    for i in range(4, 44):
        if i % 4 == 0:
            # Every 4th word uses the g() function
            last_word = words[i-1]
            first_round_word = words[i-4]
            round_num = (i - 4) // 4
            result_word = xor_bytes(g(last_word, round_num), first_round_word)
            words.append(result_word)
        else:
            # Otherwise XOR with word 4 places earlier
            words.append(xor_bytes(words[i-1], words[i-4]))

    # Generate the round keys from the words list
    round_keys: list[State] = [bytes_to_state(b''.join(words[0:4]))]
    for i in range(4, len(words), 4):
        round_keys.append(bytes_to_state(b''.join(words[i:i + 4])))

    return round_keys

def g(word: bytes, round_num: int) -> bytes:
    """
     Transforms a word in the key schedule using AES key schedule core:
    - RotWord
    - SubWord
    - XOR with round constant
    """
    byte_list = list(word)

    # RotWord: move first byte to the end
    first_byte = byte_list.pop(0)
    byte_list.append(first_byte)

    # SubWord: apply S-box to each byte
    for i in range(len(byte_list)):
        byte_list[i] = s_box[byte_list[i]]

    # XOR the first byte with the current round constant
    byte_list[0] = byte_list[0] ^ rcon[round_num]

    return bytes(byte_list)

def test_expand_key():
    key_bytes = bytes(range(16))  # 0x00, 0x01, ..., 0x0F
    key_state = bytes_to_state(key_bytes)

    round_keys = expand_key(key_state)

    # Check number of round keys (AES-128 should give 11 keys)
    assert len(round_keys) == 11, f"Expected 11 round keys, got {len(round_keys)}"

    # Round key 0 should match the original key
    assert state_to_bytes(round_keys[0]) == key_bytes, "First round key doesn't match original key"

    # Check all round keys are 16 bytes
    for i, rk in enumerate(round_keys):
        flat = state_to_bytes(rk)
        assert isinstance(flat, bytes), f"Round key {i} is not bytes"
        assert len(flat) == 16, f"Round key {i} is not 16 bytes"

    print("ExpandKey passed.")

if __name__ == '__main__':
    test_expand_key()