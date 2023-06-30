def generateAllSubstrings(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return substrings

s = input("Enter a string: ")
print(generateAllSubstrings(s))