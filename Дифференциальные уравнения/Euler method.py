class EulerMethod:

    @staticmethod
    def solve(f, y0: float, a: float, b: float, N=5):
        x = a
        y = y0
        h = (b - a) / N
        x_values = [x]
        y_values = [y]

        # Euler loop
        for _ in range(N):
            y = y + h * f(x, y)
            x = x + h
            x_values.append(x)
            y_values.append(y)

        return x, y, x_values, y_values


print("Enter differential equation in format dy = f(x, y). Example dy = x + y")
eq = input()
f = lambda x, y: eval(" ".join(eq.split(" ")[3::]))
print("Enter y0")
y0 = int(input())
print("Enter a b intervals")
a, b = map(float, input().split())
print(EulerMethod.solve(f, y0, a, b)[:2])
