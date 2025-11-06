class AdamsBashforth:

    @staticmethod
    def solve(f, y0: float, a: float, b: float, h=0.1):
        # Interval and step
        N = int((b - a) / h)

        # Initial condition
        x_values = [a]
        y_values = [1]

        # Use Runge-Kutta for the first step
        x0, y0 = a, 1
        k1 = f(x0, y0)
        k2 = f(x0 + h / 2, y0 + h / 2 * k1)
        k3 = f(x0 + h / 2, y0 + h / 2 * k2)
        k4 = f(x0 + h, y0 + h * k3)
        y1 = y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x1 = x0 + h

        x_values.append(x1)
        y_values.append(y1)

        # Compute slopes for Adams-Bashforth
        f_prev = f(x0, y0)
        f_curr = f(x1, y1)

        # Adams-Bashforth
        for n in range(2, N + 1):
            x_next = x_values[-1] + h
            y_next = y_values[-1] + h / 2 * (3 * f_curr - f_prev)  # 2-order accuracy formula

            # Update lists and slopes
            x_values.append(x_next)
            y_values.append(y_next)

            f_prev, f_curr = f_curr, f(x_next, y_next)

        return x_next, y_next, x_values, y_values

print("Enter differential equation in format dy = f(x, y). Example dy = x + y")
eq = input()
f = lambda x, y: eval(" ".join(eq.split(" ")[3::]))
print("Enter y0")
y0 = int(input())
print("Enter a b intervals")
a, b = map(float, input().split())
print(AdamsBashforth.solve(f, y0, a, b))
