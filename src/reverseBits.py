def reverse_bits(num):
    # Get the binary representation of the number
    binary = bin(num)[2:].zfill(32)
    # Reverse the binary string
    reversed_binary = binary[::-1]
    # Convert the reversed binary string back to an integer
    reversed_num = int(reversed_binary, 2)
    return reversed_num

# Read the number of test cases
t = int(input())

# Process each test case
for i in range(t):
    # Read the input number
    num = int(input())
    # Reverse the bits and print the result
    print(reverse_bits(num))
