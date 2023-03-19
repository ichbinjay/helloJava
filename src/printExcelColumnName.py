def getExcelColumnName(n):
    # initialize output string
    result = ""

    while n > 0:
        # find remainder with 26
        remainder = n % 26

        # if remainder is 0, then 'Z' represents 26th column
        if remainder == 0:
            result += 'Z'
            n = (n // 26) - 1
        else:
            # else find corresponding character and add to result
            result += chr((remainder - 1) + ord('A'))
            n = n // 26

    # reverse the result string and return
    return result[::-1]

# example usage
print(getExcelColumnName(705))

# do the reverse of above function. Given a column name, find its corresponding number
# Path: src\printExcelColumnNumber.py
def getExcelColumnNumber(columnName):
    # initialize result
    result = 0

    # traverse columnName from left to right
    for i in range(len(columnName)):
        # find the value of current character 'c'
        c = columnName[i]
        val = ord(c) - ord('A') + 1

        # multiply result by 26 and add 'val'
        result = result * 26 + val

    return result


print(getExcelColumnNumber(input()))
