#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Iterate over each byte in the data
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & bytes:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte character
            if num_bytes == 0:
                continue

            # UTF-8 characters can only be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If this byte is a continuation byte, it must start with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # We decrease the number of bytes to be processed
        num_bytes -= 1

    # If num_bytes is not zero, then we have an incomplete UTF-8 character
    return num_bytes == 0

# Example usage:


data = [197, 130, 1]
print(validUTF8(data))

data = [235, 140, 4]
print(validUTF8(data))
