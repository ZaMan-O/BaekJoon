import sys
I = sys.stdin.readline

n,m,k = map(int, I().split())
print(round((n+1)*(m+1)//(k+1))-1)