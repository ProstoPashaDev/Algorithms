n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a1 = 0
b1 = 0
d = 10**9
aotv = 0
botv = 0
fl = False
if m > n:
    a, b = b, a
    n, m = m, n
    fl = True
 
while a1 != n and b1 != m:
    if abs(a[a1] - b[b1]) < d:
        aotv = a[a1]
        botv = b[b1]
        d = abs(a[a1] - b[b1])
    if a[a1] < b[b1]:
        a1 += 1
    else:
        b1 += 1
    
if fl:
    print(botv, aotv)
else:
    print(aotv, botv)