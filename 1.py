
input_string = "Hello World"

and_result = ''
for char in input_string:
    and_result += chr(ord(char) & 127)

xor_result = ''
for char in input_string:
    xor_result += chr(ord(char) ^ 127)

print("Original String: ", input_string)
print("AND with 127: ", and_result)
print("XOR with 127: ", xor_result)