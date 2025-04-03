def f(x):
    return x**2 - 1
i = 1
xl = [1, 3]
shag = 0.1
while (abs(xl[i] - xl[i-1]) > 0.01):
    x = xl[i]
    gr = 2*x
    xl.append(xl[i] - shag*gr)
    i+=1
    if (i == 5):
        break

print(xl)
print(xl[-1], i)