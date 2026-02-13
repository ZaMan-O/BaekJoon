import sys
I = sys.stdin.readline

x,y,w,h = map(int, I().split())
min_x = min(x, abs(w-x))
min_y = min(y, abs(h-y))
min_distance = min(min_x, min_y)
print(min_distance)