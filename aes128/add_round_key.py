from aes128.state import State, bytes_to_state, state_to_bytes
from utils import xor_bytes

def add_round_key(key: State, state: State) -> None:
    for col in range(4):
        for row in range(4):
            state_byte = state[col][row].to_bytes()
            key_byte = key[col][row].to_bytes()
            state[col][row] = int.from_bytes(xor_bytes(state_byte, key_byte))

def test_add_round_key():
    key = bytes_to_state(bytes(range(16)))
    state = bytes_to_state(bytes(range(1, 17)))
    print(state)
    add_round_key(key, state)

    print(state)

if __name__ == '__main__':
    test_add_round_key()