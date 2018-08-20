def on_square(integer_number):
    if integer_number>64 or integer_number<1:
        raise ValueError("invalid square")
    return 2**(integer_number-1)


def total_after(integer_number):
    if integer_number>64 or integer_number<1:
        raise ValueError("invalid square")
    return (2**integer_number)-1

