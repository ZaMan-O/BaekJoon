import sys
import heapq
I = sys.stdin.readline

m_heap = []
p_heap = []
N = int(I().strip())
for _ in range(N):
    x = int(I().strip())
    if not x == 0:
        if x > 0:
            heapq.heappush(p_heap, x)
        else:
            heapq.heappush(m_heap, abs(x))
    else:
        if m_heap:
            if p_heap:
                a,b = heapq.heappop(m_heap), heapq.heappop(p_heap)
                if a == b:
                    heapq.heappush(p_heap, b)
                    print(-a)
                elif a < b:
                    heapq.heappush(p_heap, b)
                    print(-a)
                else:
                    heapq.heappush(m_heap, a)
                    print(b)
            else:
                print(-heapq.heappop(m_heap))
        elif p_heap:
            print(heapq.heappop(p_heap))
        else:
            print(0)