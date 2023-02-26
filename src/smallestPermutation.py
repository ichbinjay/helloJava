def calculate_unlocking_key(lockingkey):
    # Convert to string and sort the digits
    sorted_digits = sorted(str(abs(lockingkey)))

    # Remove leading zeros, if any and store in a list
    zeros_list = []
    while sorted_digits and sorted_digits[0] == '0':
        zeros_list.append(sorted_digits.pop(0))

    # Convert back to string and return
    if zeros_list:
        res = sorted_digits[0]+''.join(zeros_list)+''.join(sorted_digits[1:])
        return res
    else:
        return ''.join(sorted_digits)


print(calculate_unlocking_key(int(620152)))