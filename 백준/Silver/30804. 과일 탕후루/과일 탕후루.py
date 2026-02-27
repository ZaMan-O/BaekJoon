from collections import defaultdict
import sys
I = sys.stdin.readline

N = int(I().strip())
fruits = list(map(int, I().split()))
count = defaultdict(int)
max_count = 0
start,end = 0, 0

while end < N:
    count[fruits[end]] += 1
    while len(count.keys()) > 2:
        count[fruits[start]] -= 1
        if count[fruits[start]] == 0:
            del count[fruits[start]]
        start += 1
    max_count = max(sum(count.values()), max_count)
    end += 1
print(max_count)