def generate_subsequences(s):
    if len(s) == 0:
        return set([''])

    char = s[0]
    substrings = generate_subsequences(s[1:])
    subsequences = set(substrings)

    for substring in substrings:
        subsequences.add(char + substring)

    return subsequences

n = int(input())
s = input()
subsequenes = generate_subsequences(s)
count = 0
for i in range(n):
    word = input()
    if word in subsequenes:
        count += 1

print(count)


# optimized solution
n=int(input())
s=input()
c=0
for i in range(n):
    x=input()
    j=0
    for i in range(len(s)):
        if s[i]==x[j]:
            j+=1
            if j==len(x):c+=1; break
print(c)
