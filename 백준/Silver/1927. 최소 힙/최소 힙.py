import sys
import heapq
I = sys.stdin.readline

heap = []
N = int(I().strip())
for _ in range(N):
    x = int(I().strip())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)