from aes128.state import State


def xtime(a):
    return ((a << 1) ^ 0x1B) & 0xFF if a & 0x80 else (a << 1) & 0xFF

def mul(a, b):
    if b == 1:
        return a
    elif b == 2:
        return xtime(a)
    elif b == 3:
        return xtime(a) ^ a
    elif b == 9:
        return xtime(xtime(xtime(a))) ^ a
    elif b == 11:
        return xtime(xtime(xtime(a)) ^ a) ^ a
    elif b == 13:
        return xtime(xtime(xtime(a) ^ a)) ^ a
    elif b == 14:
        return xtime(xtime(xtime(a) ^ a) ^ a)
    else:
        raise ValueError("Unsupported multiplier in MixColumns")

def mix_columns(state: State) -> None:
    for col in range(4):
        a0 = state[0][col]
        a1 = state[1][col]
        a2 = state[2][col]
        a3 = state[3][col]

        state[0][col] = mul(a0,2) ^ mul(a1,3) ^ mul(a2,1) ^ mul(a3,1)
        state[1][col] = mul(a0,1) ^ mul(a1,2) ^ mul(a2,3) ^ mul(a3,1)
        state[2][col] = mul(a0,1) ^ mul(a1,1) ^ mul(a2,2) ^ mul(a3,3)
        state[3][col] = mul(a0,3) ^ mul(a1,1) ^ mul(a2,1) ^ mul(a3,2)

def inverse_mix_columns(state: State) -> None:
    for col in range(4):
        a0 = state[0][col]
        a1 = state[1][col]
        a2 = state[2][col]
        a3 = state[3][col]

        state[0][col] = mul(a0,14) ^ mul(a1,11) ^ mul(a2,13) ^ mul(a3,9)
        state[1][col] = mul(a0,9)  ^ mul(a1,14) ^ mul(a2,11) ^ mul(a3,13)
        state[2][col] = mul(a0,13) ^ mul(a1,9)  ^ mul(a2,14) ^ mul(a3,11)
        state[3][col] = mul(a0,11) ^ mul(a1,13) ^ mul(a2,9)  ^ mul(a3,14)
