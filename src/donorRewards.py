t = int(input())
for _ in range(t):
    x = int(input())
    if x <= 3:
        print("BRONZE")
    elif 3 < x <= 6:
        print("SILVER")
    else:
        print("GOLD") 