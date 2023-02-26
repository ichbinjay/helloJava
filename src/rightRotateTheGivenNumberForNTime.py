N = int(input())
num = input()

# Convert string input to list of integers
num_list = list(map(int, num))

# Compute actual number of rotations needed
rotations = N % len(num_list)

# Right rotate the list 'num_list' for 'rotations' times
num_list = num_list[-rotations:] + num_list[:-rotations]

# Convert list of integers back to string and print
result = ''.join(map(str, num_list))
print(result)