s = "A man, a plan, a canal: Panama"
s = s.lower()
for i in s:
    if not i.isalnum():
        s = s.replace(i, '')
print(s == s[::-1])
