Row = list[int]
State = list[Row]


def bytes_to_state(data: bytes) -> State:
    """Returns 16 bytes matrix State of the given data."""
    assert len(data) == 16, "Input must be 16 bytes."

    state = [[0, 0, 0, 0] for _ in range(4)]

    for i in range(16):
        row = i % 4
        col = i // 4
        state[row][col] = data[i]

    return state

def state_to_bytes(state: State) -> bytes:
    """Returns 16 bytes from the given State matrix."""
    result = bytearray(16)
    for col in range(4):
        for row in range(4):
            result[4 * col + row] = state[row][col]

    return bytes(result)

def test_state():
    data = bytes(range(16))
    print(data)
    state = bytes_to_state(data)
    print(state)
    original = state_to_bytes(state)
    print(original)
    assert original == data

if __name__ == '__main__':
    test_state()