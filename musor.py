n=1001

byte_length = (n.bit_length() + 7) // 8   # мінімальна кількість байтів
b = n.to_bytes(byte_length, byteorder='big')
print(b)