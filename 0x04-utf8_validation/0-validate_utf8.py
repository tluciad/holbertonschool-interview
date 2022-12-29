#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    for num in data:

        # Get the binary representation. 8 bits
        bin_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:

            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios according to the rules of the problem.
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:

            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        # We reduce the number of bytes to process by 1 after each integer.
        n_bytes -= 1

    return n_bytes == 0
