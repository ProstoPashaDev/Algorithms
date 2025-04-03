def find_del(x):
    ans = []
    for i in range(1, int(x**0.5) + 1):
        if i * i == x:
            ans.append(i)
        elif x % i == 0:
            ans.append(i)
            ans.append(x//i)
    return ans
    
 
def get_hash(l, r):
    return (h[r] - (h[l-1] * pp[r-l+1])) % m

def ordr(a):
    return ord(a) - 96
s = input()
p = 71
m = 10**9 + 7
lens = len(s) + 1
pp = [0] * lens
pp[0] = 1
for i in range(1, lens):
    pp[i] = pp[i-1] * p % m
 
h = [0] * lens
for i in range(1, len(s)+1):
    h[i] = (p * h[i-1] + ordr(s[i-1])) % m
    
print(h)
delit = find_del(lens-1)
ans = []
for i in range(len(delit)):
    fl = True

    for j in range(delit[i], len(s), delit[i]):
        if get_hash(j-delit[i]+1, j) != get_hash(j+1, j+delit[i]):
            fl = False
            break
            
    if fl:
        ans.append(delit[i])

print((lens-1) // min(ans))