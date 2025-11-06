import numpy as np
from scipy.integrate import quad


class Galerkin:
    @staticmethod
    def solve(p, q, r, a, b, y_a=None, yp_b=None, N=5):
        # Basis functions
        def phi(i, x):
            return x ** (2 * i - 2) * (1 - x ** 2)

        def phi_prime(i, x):
            if x == 0 and i == 1:
                return 0.0
            return (2 * i - 2) * x ** (2 * i - 3) * (1 - x ** 2) - 2 * x ** (2 * i - 1)

        def phi_double_prime(i, x):
            if x == 0 and i == 1:
                return -2.0
            term1 = 0.0 if (x == 0 and i <= 1) else (2 * i - 2) * (2 * i - 3) * x ** (2 * i - 4) * (1 - x ** 2)
            term2 = -4 * (i - 1) * x ** (2 * i - 2)
            term3 = -2 * x ** (2 * i - 2)
            return term1 + term2 + term3

        # Construct Galerkin system
        A = np.zeros((N, N))
        B = np.zeros(N)

        # Integrate using quadrature
        for j in range(N - 1):
            for i in range(N):
                integrand = lambda x: (phi_double_prime(i + 1, x) + p(x) * phi_prime(i + 1, x) + q(x) * phi(i + 1,
                                                                                                            x)) * phi(
                    j + 1, x)
                A[j, i] = quad(integrand, a, b)[0]
            integrand_b = lambda x: r(x) * phi(j + 1, x)
            B[j] = quad(integrand_b, a, b)[0]

        # Last row: derivative BC at x=b
        if yp_b is not None:
            for i in range(N):
                A[-1, i] = phi_prime(i + 1, b)
            B[-1] = yp_b

        # Solve linear system
        a_coeff = np.linalg.solve(A, B)

        # Evaluate solution at points
        x_values = np.linspace(a, b, 100)
        y_values = np.zeros_like(x_values)
        for i in range(N):
            y_values += a_coeff[i] * phi(i + 1, x_values)

        return x_values, y_values, a_coeff


# Example usage
p = lambda x: -2 * x
q = lambda x: 2
r = lambda x: x

gal = Galerkin()
x_values, y_values, coeffs = gal.solve(p, q, r, 0, 1, y_a=0, yp_b=1, N=5)

print(coeffs)
