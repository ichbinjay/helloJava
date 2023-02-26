def balanced_parentheses(str):
    stack = []
    count = 0
    for char in str:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return -1
            else:
                stack.pop()
                count += 1
    if not stack:
        return count
    else:
        return -1


if __name__ == "__main__":
    str = input()
    print(balanced_parentheses(str))