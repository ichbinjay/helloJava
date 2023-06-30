from collections import defaultdict

def generateAllSubstrings(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return substrings


def main():
    k = int(input())
    s = input()
    substrings = generateAllSubstrings(s)
    longestSubstring = ""
    longestSubstringLength = 0
    for substring in substrings:
        freqs = defaultdict(int)
        for char in substring:
            freqs[char] += 1

        isGood = True
        for i in freqs.values():
            if i < k:
                isGood = False
                break
        
        if isGood and len(substring) > longestSubstringLength:
            longestSubstringLength = len(substring)
            longestSubstring = substring

    print(longestSubstringLength)
    print(longestSubstring)
    print(substrings)

main()
