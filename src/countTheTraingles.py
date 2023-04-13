def count_triangles(n, rod_lengths):
    rod_lengths.sort()
    count = 0
    i = 0
    while i < n - 2:
        k = i + 2
        j = i + 1
        while j < n:
            while k < n and rod_lengths[i] + rod_lengths[j] > rod_lengths[k]:
                k += 1
            if k > j:
                count += k - j - 1
            j += 1
        i += 1

    return count


t = int(input())

for _ in range(t):
    n = int(input())
    rod_lengths = list(map(int, input().split()))

    result = count_triangles(n, rod_lengths)
    print(result)
