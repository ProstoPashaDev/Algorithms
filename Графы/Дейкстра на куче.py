import heapq
def dikstra(start):
    visited = set()
    heap = [(0, start)]
    heapq.heapify(heap)
    #print(heap)
    while heap:
        dist, ver = heapq.heappop(heap)
        #print(dist, ver)
        if ver not in visited:
            visited.add(ver)
            distance[ver] = dist
            
            for v in a[ver]:
                if v[1] not in visited:
                    heapq.heappush(heap, (dist + v[0], v[1]))
    return distance


n, s, f = map(int, input().split())
a = [[] for i in range(n)]
for i in range(n):
    b = list(map(int, input().split()))
    for j in range(n):
        if b[j] != -1 and i != j:
            a[i].append((b[j], j))
#print(a)
distance = [10**9 for i in range(n)]
ans = dikstra(s-1)[f-1]
if ans == 10**9:
    print(-1)
else:
    print(ans)

