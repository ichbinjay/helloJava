def count_palindromes(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if s[i:j+1] == s[i:j+1][::-1]:
                count += 1
    return count

# Example usage
s = "racecar level deed noon"
num_palindromes = count_palindromes(s) # this considers each single character as a palindrome
print(f"Number of palindromes in '{s}': {num_palindromes}")
