import numpy as np


class FiniteDifferenceMethod:

    @staticmethod
    def solve(p, q, r,
          a1, b1, c1,  # left BC: a1*y(x0) + b1*y'(x0) = c1
          a2, b2, c2,  # right BC: a2*y(xN) + b2*y'(xN) = c2
          x0, xN, N=5):
        """
        Solves general 2nd order ODE:
            y'' + p(x)*y' + q(x)*y = r(x)
        with boundary conditions:
            a1*y(x0) + b1*y'(x0) = c1
            a2*y(xN) + b2*y'(xN) = c2

        Returns:
            x_values : numpy array of grid points
            y_values : numpy array of solution values
        """

        # Step size and grid points
        h = (xN - x0) / N
        x_values = np.linspace(x0, xN, N + 1)

        # Coefficient matrix
        A = np.zeros((N + 1, N + 1))
        b = np.zeros(N + 1)

        # --- Left boundary (at x0) ---
        # a1*y0 + b1*y'(x0) = c1
        # Approximate y'(x0) = (y1 - y0)/h
        A[0, 0] = a1 - b1 / h
        A[0, 1] = b1 / h
        b[0] = c1

        # --- Interior nodes ---
        for i in range(1, N):
            xi = x_values[i]
            pi = p(xi)
            qi = q(xi)
            ri = r(xi)

            # Using central differences:
            # y'' = (y_{i-1} - 2y_i + y_{i+1}) / h^2
            # y'  = (y_{i+1} - y_{i-1}) / (2h)
            A[i, i - 1] = 1 / h ** 2 - pi / (2 * h)
            A[i, i] = -2 / h ** 2 + qi
            A[i, i + 1] = 1 / h ** 2 + pi / (2 * h)
            b[i] = ri

        # --- Right boundary (at xN) ---
        # a2*yN + b2*y'(xN) = c2
        # Approximate y'(xN) = (yN - yN-1)/h
        A[N, N - 1] = -b2 / h
        A[N, N] = a2 + b2 / h
        b[N] = c2

        # --- Solve the system ---
        y_values = np.linalg.solve(A, b)

        return x_values, y_values


# Problem: y'' + (1/x)*y' + 2y = x
p = lambda x: 1 / x
q = lambda x: 2
r = lambda x: x

# Boundary conditions:
# y(0.7) = 0.5  -> a1=1, b1=0, c1=0.5
# 2y(1) + 3y'(1) = 1.2 -> a2=2, b2=3, c2=1.2
a1, b1, c1 = 1, 0, 0.5
a2, b2, c2 = 2, 3, 1.2

print(FiniteDifferenceMethod.solve(p, q, r, a1, b1, c1, a2, b2, c2, x0=0.7, xN=1.0))



