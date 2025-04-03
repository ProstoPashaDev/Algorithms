def create_do():
    global c
    for i in range(st-1, -1, -1):
        c[i] = max(c[i*2], c[i*2+1])
    c[0] = 0

def do(i, linp, rinp, l, r):
    global ans
    m = (l + r) // 2
    #print(i, linp, rinp, l, r)
    if l == linp and r == rinp:
        ans.append([c[i], i])
        return c[i]
    if linp > rinp:
        return -1
    if i * 2 > 2 * st:
        return -1
    
    do(i*2, linp, min(rinp, r, m), l, m)
    do(i*2+1, max(l, linp, m+1), rinp, m+1, r)
    


ans = []
n = int(input())
a = list(map(int, input().split()))
st = 0
for i in range(5000):
    if 2**i >= n:
        st = 2**i
        break

k = int(input())
c = [0 for i in range(st)] + [0 for i in range(st - n)] + a
ans = []
create_do()
#print(c)
res = []
for i in range(k):
    x, y = map(int, input().split())
    if x == y:
        res.append(x-1)
    else:
        do(1, x+st-n-1, y+st-n-1, 0, st-1)
        print(ans)
        ans.sort(key = lambda x: x[0])
        res.append(ans[-1][1] - (st - n))
        
        ans = []
print(*res)