def defuse_bomb(size, key, message):
    result = []
    for i in range(size):
        if i+key < size:
            result.append(sum(message[i+1:i+1+key]))
        else:
            extra = (i+1+key) - size
            result.append(sum(message[i+1:i+1+key-extra])+sum(message[:extra]))
    return result


size = int(input())
key = int(input())
message = [int(x) for x in input().split()]
print(*defuse_bomb(size, key, message))