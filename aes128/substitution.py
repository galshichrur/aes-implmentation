from aes128.state import State
from utils import s_box, rs_box


def substitute_bytes(state: State) -> None:
    """Applies the SubBytes transformation using the AES S-box."""
    for row in range(4):
        for col in range(4):
            state[row][col] = s_box[state[row][col]]

def inverse_substitute_bytes(state: State) -> None:
    """Apply inverse SubBytes using rs_box on a new state."""
    for row in range(4):
        for col in range(4):
            state[row][col] = rs_box[state[row][col]]

def test_inv_sub_bytes():
    state1 = [
        [0x00, 0x01, 0x02, 0x03],
        [0x10, 0x11, 0x12, 0x13],
        [0x20, 0x21, 0x22, 0x23],
        [0x30, 0x31, 0x32, 0x33]
    ]
    state2 = [
        [0x00, 0x01, 0x02, 0x03],
        [0x10, 0x11, 0x12, 0x13],
        [0x20, 0x21, 0x22, 0x23],
        [0x30, 0x31, 0x32, 0x33]
    ]

    substitute_bytes(state2)
    inverse_substitute_bytes(state2)

    assert state2 == state1, "InvSubBytes failed."
    print("InvSubBytes passed.")

if __name__ == '__main__':
    test_inv_sub_bytes()