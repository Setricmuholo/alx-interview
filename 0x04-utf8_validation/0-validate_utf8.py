#!/usr/bin/python3

"""
UTF-8 Validation
"""


def validUTF8(data):

    """
    Helper function to check if a given byte is a continuation byte (i.e., starts with "10" in binary)
    """
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    # Helper function to get the number of bytes in a character based on the first byte
    def get_num_bytes(first_byte):
        if (first_byte & 0b10000000) == 0b00000000:  # 1-byte character
            return 1
        elif (first_byte & 0b11100000) == 0b11000000:  # 2-byte character
            return 2
        elif (first_byte & 0b11110000) == 0b11100000:  # 3-byte character
            return 3
        elif (first_byte & 0b11111000) == 0b11110000:  # 4-byte character
            return 4
        else:
            return 0  # Invalid first byte

    i = 0
    while i < len(data):
        num_bytes = get_num_bytes(data[i])

        if num_bytes == 0:
            return False  # Invalid first byte

        # Check continuation bytes
        for j in range(1, num_bytes):
            if i + j >= len(data) or not is_continuation(data[i + j]):
                return False

        i += num_bytes

    return True
