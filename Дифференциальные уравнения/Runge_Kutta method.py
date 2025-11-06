class RungeKuttaMethod:

    @staticmethod
    def solve(f, y0: float, a: float, b: float, h=0.1):
        x, y = a, y0

        x_values = [x]
        y_values = [y]

        while x < b:
            k1 = f(x, y)
            k2 = f(x + h / 2, y + h / 2 * k1)
            k3 = f(x + h / 2, y + h / 2 * k2)
            k4 = f(x + h, y + h * k3)
            y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
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
print(RungeKuttaMethod.solve(f, y0, a, b))
