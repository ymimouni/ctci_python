from typing import Optional, List, ByteString

NUMBER_OF_INTS = pow(2, 31)


def bits(n: int):
    while n:
        yield n & 1
        n >>= 1


# def find_missing_int(file_name: str) -> Optional[int]:  # noqa
#     bit_field = bytearray(int(NUMBER_OF_INTS / 8))
#     with open(file_name) as f:
#         for line in f:
#             n = int(line)
#             bit_field[int(n / 8)] |= 1 << int(line) % 8
#
#     for i, x in enumerate(bit_field):
#         if x != 255:
#             for j, b in enumerate(bits(x)):
#                 if not b:
#                     return 8 * i + j
#
#     return None


def find_missing_int(file_name: str) -> Optional[int]:  # noqa
    range_size = 1 << 20  # 2^20 bits.

    # Get count of number of values within each block.
    blocks = get_counter_per_block(file_name, range_size)

    # Find a block with a missing value.
    block_index = find_block_with_missing_int(blocks, range_size)

    if block_index is None:
        return None

    # Create a bit vector for items within this range.
    bit_vector = get_bit_vector_for_range(file_name, block_index, range_size)

    # Find a zero in the bit vector.
    offset = find_zero(bit_vector)

    if bit_vector is None:
        return None

    # Compute missing value.
    return offset + block_index * range_size


def get_counter_per_block(file_name: str, range_size: int) -> List[int]:  # noqa
    array_size = int((pow(2, 31) - 1) / range_size)
    blocks = [0] * array_size
    with open(file_name) as f:
        for line in f:
            n = int(line)
            blocks[int(n / range_size)] += 1

    return blocks


def find_block_with_missing_int(blocks: List[int], range_size: int) -> Optional[int]:
    for i, count in enumerate(blocks):
        if count < range_size:
            return i

    return None


def get_bit_vector_for_range(file_name: str, block_index: int, range_size: int) -> ByteString:  # noqa
    bit_vector = bytearray(int(range_size / 8))
    start_range = block_index * range_size
    end_range = start_range + range_size

    with open(file_name) as f:
        for line in f:
            n = int(line)
            if start_range <= n < end_range:
                offset = n - start_range
                bit_vector[int(offset/8)] |= 1 << (offset % 8)

    return bit_vector


def find_zero(bit_vector: ByteString) -> Optional[int]:
    for i, x in enumerate(bit_vector):
        if x != 255:
            for j, b in enumerate(bits(x)):
                if not b:
                    return 8 * i + j

    return None


if __name__ == "__main__":
    file_name = 'input.txt'
    print(find_missing_int(file_name))
