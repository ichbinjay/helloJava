def check_bit(num, i):
    return num & (1 << i)


def find_single_element(arr):
    ans = 0
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if check_bit(arr[j], i):
                count += 1
        if count % 3 != 0:
            ans += 2 ** i
    return ans


# Driver code
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_single_element(arr))


# approach 2
def find_single_element(arr):
    # Initialize variables to keep track of counts
    ones = twos = 0

    for num in arr:
        # If the bit is set in the current element, increment ones
        ones = (ones ^ num) & ~twos

        # If the bit is set in both ones and the current element, increment twos
        twos = (twos ^ num) & ~ones

    # The element that occurs once is the value in ones
    return ones


# Driver code
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_single_element(arr))