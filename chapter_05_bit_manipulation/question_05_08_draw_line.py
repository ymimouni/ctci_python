"""
Draw line.
"""


def draw_line(screen, width: int, x1: int, x2: int, y: int):
    start_offset = x1 % 8
    first_full_byte = x1 // 8
    if start_offset != 0:
        first_full_byte += 1

    end_offset = x2 % 8
    last_full_byte = x2 // 8
    if end_offset != 7:
        last_full_byte -= 1

    # Set full bytes.
    for b in range(first_full_byte, last_full_byte + 1):
        screen[(width // 8) * y + b] = 0xFF

    start_mask = 0xFF >> start_offset
    end_mask = (~(0xFF >> (end_offset + 1))) & 0xFF

    # Set start and end of line.
    if x1 // 8 == x2 // 8:
        # If x1 and x2 are in the same byte.
        mask = start_mask & end_mask
        screen[(width // 8) * y + (x1 // 8)] |= mask
    else:
        if start_offset != 0:
            screen[(width // 8) * y + first_full_byte - 1] |= start_mask
        if end_offset != 7:
            screen[(width // 8) * y + last_full_byte + 1] |= end_mask


if __name__ == "__main__":
    values = [0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0]
    scr = bytearray(values)
    draw_line(scr, 64, 20, 42, 1)
    z = list(scr)
    print(z)
