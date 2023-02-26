def count_and_say(n):
    if n == 1:
        return "1"
    prev = count_and_say(n-1)
    result = ""
    i = 0
    while i < len(prev):
        count = 1
        while i < len(prev)-1 and prev[i] == prev[i+1]:
            count += 1
            i += 1
        result += str(count) + prev[i]
        i += 1
    return result

# Example usage
n = int(input())
for i in range(1, n+1):
    print(count_and_say(i))
