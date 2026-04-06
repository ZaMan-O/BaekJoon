import sys
I = sys.stdin.readline

arr = [0] * 3
arr[0] = (I().strip())[0]
arr[1] = (I().strip())[0]
arr[2] = (I().strip())[0]
if 'l' in arr:
    if 'k' in arr:
        if 'p' in arr:
            print('GLOBAL')
            exit()
print('PONIX')