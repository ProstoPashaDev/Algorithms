
def soz(n):
    global a
    global p
    a = []
    p = []
    for i in range(n):
        p.append(i)
        a.append([i])

def pre(v):
    return p[v]

def ch(b, c):
    return p[b] == p[c]

def add(b, c):
    if ch(b, c):
        return True
    else:
        c = pre(c)
        b = pre(b)
        sgl1 = s[b]
        s[b] = s[b] + s[c]
        s[c] = sgl1 + s[c]
        if len(a[c]) > len(a[b]):
            c, b = b, c
        for i in a[c]:
            p[i] = b
            a[b].append(i)


        a[c] = []
    return False

a = []
p = []
n = int(input())
s = [[i+1] for i in range(n)]
soz(n)
for i in range(n-1):
    x, y = map(int, input().split())
    #a.append([x-1, y-1])
    #merge(x-1, y-1)
    add(x-1, y-1)

for i in range(n):
    if len(s[i]) == n:
        print(*s[i])
        break
