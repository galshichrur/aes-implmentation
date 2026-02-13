from aes128.state import State


def shift_rows(state: State) -> None:
    for row in range(1, 4):
        state[row] = state[row][row:] + state[row][:row]

def inverse_shift_rows(state: State) -> None:
    for row in range(1, 4):
        state[row] = state[row][-row:] + state[row][:-row]

def test_shift_rows():
    state = [
        [0x00, 0x01, 0x02, 0x03],
        [0x10, 0x11, 0x12, 0x13],
        [0x20, 0x21, 0x22, 0x23],
        [0x30, 0x31, 0x32, 0x33]
    ]

    expected_shifted = [
        [0x00, 0x01, 0x02, 0x03],
        [0x11, 0x12, 0x13, 0x10],
        [0x22, 0x23, 0x20, 0x21],
        [0x33, 0x30, 0x31, 0x32]
    ]

    shift_rows(state)
    assert state == expected_shifted, "ShiftRows failed"

    inverse_shift_rows(state)
    assert state == [
        [0x00, 0x01, 0x02, 0x03],
        [0x10, 0x11, 0x12, 0x13],
        [0x20, 0x21, 0x22, 0x23],
        [0x30, 0x31, 0x32, 0x33]
    ], "Inverse ShiftRows failed"

    print("ShiftRows passed.")

if __name__ == '__main__':
    test_shift_rows()