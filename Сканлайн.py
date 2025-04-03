n, m = map(int, input().split())
a = []
for i in range(n):
    a1, b1 = map(int, input().split())
    a.append([min(a1, b1), 0, i])
    a.append([max(a1, b1), 2, i])
sp = list(map(int, input().split()))
for i in range(m):
    a.append([sp[i], 1, i])
a.sort(key = lambda x: [x[0], x[1]])
d = 0
otv = []
#print(a)
for i in range(len(a)):
    if a[i][1] == 0:
        d += 1
    elif a[i][1] == 2:
        d -= 1
    else:
        otv.append([d, a[i][2]])
otv.sort(key = lambda x: x[1])
for i in otv:
    print(i[0], end = " ")
    