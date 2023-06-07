#Brute Force
def seq_finder(arr, n):
    max_len_seq = set()
    for i in range(n):
        for j in range(i, n):
            max_elem, min_elem = max(arr[i:j + 1]), min(arr[i:j + 1])
            if max_elem - min_elem == j - i:
                max_len_seq.add(j - i + 1)
    return max(max_len_seq)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(seq_finder(arr, n))

main()


#Optimized Solution
def seq_finder(arr, n):
    max_len_seq = 1
    for i in range(n):
        max_elem, min_elem = arr[i], arr[i]
        s = set()
        s.add(arr[i])
        for j in range(i+1, n):
            s.add(arr[j])
            max_elem = max(max_elem, arr[j])
            min_elem = min(min_elem, arr[j])
            if max_elem - min_elem == len(s)-1:
                max_len_seq = max(j - i + 1, max_len_seq)
    return max_len_seq


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(seq_finder(arr, n))


main()