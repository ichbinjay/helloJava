t = int(input())
for _ in range(t):
    cmd_count = int(input())
    status = 0
    cmds = input().split()
    for cmd in cmds:
        if cmd == "START":
            status = 1
        elif cmd == "STOP":
            if status == 0:
                print("404")
            else:
                status = 0
        elif cmd == "RESTART":
            status = 1
