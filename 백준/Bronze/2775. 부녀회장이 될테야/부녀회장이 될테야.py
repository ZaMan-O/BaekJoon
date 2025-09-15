import sys
I = sys.stdin.readline

tc = int(I().strip())
result = []

for i in range(tc):
    k = int(I().strip())
    n = int(I().strip())
    x = [[0]*n for _ in range(k+1)]
    for ii in range(n):
        x[0][ii] = ii + 1
    
    for ii in range(1,k+1):
        for iii in range(n):
            temp = 0
            for iv in range(1):
                for v in range(iii + 1):
                    temp += x[ii-1][v]
            x[ii][iii] = temp
    result.append(x[k][n-1])

for i in result:
    print(i)