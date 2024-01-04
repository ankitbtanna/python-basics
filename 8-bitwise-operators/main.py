# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation

# is operator
# in operator

a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)
# 0101  (a)
# 0011  (b)
# ----
# 0001  (result)


print(a | b)
# 0101  (a)
# 0011  (b)
# ----
# 0111  (result)

a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a ^ b
print(result)  # Output: 6 (0110 in binary)
# Apply the XOR operation between each pair of corresponding bits.
# The result will be 1 only if the bits are different; otherwise, it will be 0.
# 0101  (a)
# 0011  (b)
# ----
# 0110  (result)

a = 5  # 0101 in binary
result = ~a
print(result)  # Output: -6 (in two's complement representation)

'''
Certainly! Converting the binary result 1010 to decimal involves understanding two's complement representation. Here are the steps:

Identify the Sign Bit:

In two's complement, the leftmost bit (most significant bit, MSB) is the sign bit.
If the sign bit is 1, the number is negative.
In our example, 1010 has a sign bit of 1, indicating a negative number.

Find the Absolute Value:

To find the absolute value of a negative number in two's complement, invert all the bits and add 1.
Inverting the bits of 1010 gives 0101. Adding 1 to 0101 results in 0110.

Determine the Sign:

Since the original sign bit was 1, the final result is negative.
Putting it all together, interpreting 1010 as a signed integer involves finding the absolute value (0110) and assigning the correct sign, resulting in -6. I apologize for any confusion in my previous responses. Thank you for your patience and understanding.
'''

a = 5  # 0101 in binary
result = a << 1
print(result)  # Output: 10 (1010 in binary)

a = 5  # 0101 in binary
result = a >> 1
print(result)  # Output: 2 (0010 in binary)
