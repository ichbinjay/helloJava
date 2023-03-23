import sys

def magic_min_cost(s):
    possible_magic_squares = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]], 
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
    min_cost = sys.maxsize
    for magic_square in possible_magic_squares:
        curr_cost = 0
        for j in range(3):
            for k in range(3):
                curr_cost += abs(magic_square[j][k] - s[j][k])
        min_cost = min(min_cost, curr_cost)
    return min_cost

a = []
for i in range(3):
    a.append(list(map(int, input().split())))
print(magic_min_cost(a))

