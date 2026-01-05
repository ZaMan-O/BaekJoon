import sys
I = sys.stdin.readline

def operate(dn, o, tmp):
    while True:
        if tmp == 1:
            break
        o += 1
        if tmp % dn != 0:
            tmp -= 1
        else:
            tmp //= dn
            break
    if tmp == 1:
        return o
    return min(operate(2,o,tmp), operate(3,o,tmp))

N = int(I().strip())
print(min(operate(2,0,N), operate(3,0,N)))