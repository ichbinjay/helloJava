maxLen = 0

def someCondition(g1, g2):
    if g1 == "A":
        if g2 == "A" or g2 == "AB":
            return True
    elif g1 == "B":
        if g2 == "B" or g2 == "AB":
            return True
    elif g1 == "AB":
        if g2 == "AB":
            return True
    elif g1 == "O":
        return True
    return False

def function(bgroups, count):
    if len(bgroups) == 1:
        return
    
    global maxLen
    for i in range(len(bgroups)):
        for j in range(len(bgroups)):
            if i != j:
                if someCondition(bgroups[i], bgroups[j]):
                    if maxLen < count:
                        maxLen = count
                    function(bgroups[:i] + bgroups[i+1:], count+1)


def main():
    t = 1 #int(input())
    for _ in range(t):
        n  = 5 #input()
        bgroups = ["AB A A AB A".split()]
        function(bgroups, 0)
        print(maxLen)

main()
    