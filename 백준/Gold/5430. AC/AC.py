T = int(input().strip())
for _ in range(T):
    p = input().strip()
    n = int(input().strip())
    tmp = input().strip()[1:-1]
    if tmp == "":
        arr = "[]"
    else:
        arr = list(map(int, tmp.split(',')))
    rv = False
    pl, mi = 0, 0
    for i in p:
        if i == 'R':
            if rv:
                rv = False
            else:
                rv = True
        else:
            if rv:
                mi += 1
            else:
                pl += 1
    if pl + mi > n:
        print("error")
    else:
        print("[", end="")
        if rv:
            for i in range(n-1-mi, pl-1, -1):
                if i != n-1-mi:
                    print(",", end="")
                print(arr[i], end="")
        else:
            for i in range(pl, n-mi):
                if i != pl:
                    print(",", end="")
                print(arr[i], end="")
        print("]")