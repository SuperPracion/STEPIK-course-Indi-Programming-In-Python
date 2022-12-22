import sys

hex_nums = [hex(int(num.strip())).replace('0x', '').zfill(2).upper() for num in sys.stdin]
print('#' + ''.join(hex_nums))
